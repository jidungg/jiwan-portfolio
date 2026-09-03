#!/usr/bin/env python3
"""
포트폴리오 제작소 빌드 도구.

이 스크립트는 판단하지 않는다. Cases/<slug>/<slug>.md와 manifest.yaml에 적힌 대로만
조립·검증·렌더링한다. 어떤 사례를 고를지, 왜 고를지는 여기서 결정하지 않는다
(그건 /build 커맨드 안에서 Claude와 사용자가 한다).

사용법:
    python tools/build.py index                        Cases/INDEX.md 재생성
    python tools/build.py validate                      전체 사례 형식 검증
    python tools/build.py render <application-dir>      manifest.yaml -> PDF

    <application-dir>는 Applications/ 아래 폴더 이름 또는 전체 경로.
    예: python tools/build.py render Applications/2026-08-26-넥슨-클라이언트
"""

from __future__ import annotations

import argparse
import platform
import re
import shutil
import subprocess
import sys
from dataclasses import dataclass, field
from pathlib import Path

if sys.platform == "win32":
    # Windows 콘솔 기본 코드페이지(cp949)에서 한글 출력이 깨지는 것을 방지
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")

try:
    import yaml
except ImportError:
    print("PyYAML이 필요합니다: pip install -r requirements.txt", file=sys.stderr)
    sys.exit(1)

try:
    import markdown as md
except ImportError:
    print("markdown 패키지가 필요합니다: pip install -r requirements.txt", file=sys.stderr)
    sys.exit(1)

REPO_ROOT = Path(__file__).resolve().parent.parent
CASES_DIR = REPO_ROOT / "Cases"
TEMPLATES_DIR = REPO_ROOT / "Templates"
APPLICATIONS_DIR = REPO_ROOT / "Applications"

REQUIRED_FIELDS = [
    "id", "title", "summary", "project", "role", "period",
    "engine", "lang", "domain", "skills", "sources",
]
# 없으면 경고하는 섹션. '회고'는 쓸 말이 있을 때만 넣는 선택 섹션이라 뺀다.
BODY_SECTIONS = ["배경", "구현", "장단점", "대안 비교"]
MD_EXTENSIONS = ["fenced_code", "tables", "sane_lists"]


# ---------------------------------------------------------------------------
# 사례 파싱
# ---------------------------------------------------------------------------

@dataclass
class Case:
    path: Path
    meta: dict
    body: str
    issues: list[str] = field(default_factory=list)


def parse_case_file(path: Path) -> Case:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return Case(path=path, meta={}, body=text,
                     issues=["frontmatter가 없습니다 (파일이 '---'로 시작해야 함)"])

    parts = text.split("---", 2)
    if len(parts) < 3:
        return Case(path=path, meta={}, body=text,
                     issues=["frontmatter 종료 '---'를 찾을 수 없습니다"])

    _, fm_text, body = parts
    try:
        meta = yaml.safe_load(fm_text) or {}
    except yaml.YAMLError as e:
        return Case(path=path, meta={}, body=body, issues=[f"frontmatter YAML 파싱 실패: {e}"])

    return Case(path=path, meta=meta, body=body.strip())


def load_all_cases() -> list[Case]:
    if not CASES_DIR.exists():
        return []
    cases = []
    for p in sorted(CASES_DIR.glob("*/*.md")):
        if p.name.upper() == "INDEX.MD":
            continue
        cases.append(parse_case_file(p))
    return cases


def load_case_by_id(case_id: str) -> Case:
    for c in load_all_cases():
        if c.meta.get("id") == case_id:
            return c
    raise SystemExit(f"사례를 찾을 수 없습니다: id={case_id}")


# ---------------------------------------------------------------------------
# 검증 (형식 점검 — 1층. 전략 점검은 /audit에서 Claude가 수행)
# ---------------------------------------------------------------------------

def extract_section(body: str, heading: str) -> str | None:
    """`## 상황` 같은 섹션의 본문만 뽑는다. 다음 '## '가 나오기 전까지."""
    pattern = rf"^##\s+{re.escape(heading)}\s*$"
    lines = body.splitlines()
    start = None
    for i, line in enumerate(lines):
        if re.match(pattern, line.strip()):
            start = i + 1
            break
    if start is None:
        return None
    end = len(lines)
    for i in range(start, len(lines)):
        if lines[i].strip().startswith("## "):
            end = i
            break
    return "\n".join(lines[start:end]).strip()


def find_image_refs(body: str) -> list[str]:
    return re.findall(r"!\[[^\]]*\]\(([^)]+)\)", body)


def validate_case(case: Case) -> tuple[list[str], list[str]]:
    """(errors, warnings)를 돌려준다.

    errors는 실제로 깨진 것만 — 빠진 frontmatter 필드, 파일명과 어긋난 id,
    존재하지 않는 이미지. 이것만 빌드를 막는다.
    warnings는 "아직 안 채웠네" 수준의 알림이라 아무것도 막지 않는다.
    """
    errors = list(case.issues)
    warnings: list[str] = []
    meta = case.meta

    for f in REQUIRED_FIELDS:
        if f not in meta or meta[f] in (None, "", []):
            errors.append(f"필수 필드 누락 또는 비어 있음: {f}")

    if "metrics" in meta:
        errors.append("frontmatter에 metrics 필드가 있습니다 — 숫자는 본문 '대안 비교' 섹션에만 적습니다")

    expected_id = case.path.stem
    if meta.get("id") and meta.get("id") != expected_id:
        errors.append(f"id({meta.get('id')})가 파일명({expected_id})과 다릅니다")
    if case.path.parent.name != expected_id:
        errors.append(f"사례 폴더명({case.path.parent.name})이 파일명({expected_id})과 다릅니다")

    for img in find_image_refs(case.body):
        if img.startswith(("http://", "https://", "data:")):
            continue
        img_path = (case.path.parent / img).resolve()
        if not img_path.exists():
            img_path2 = (REPO_ROOT / img).resolve()
            if not img_path2.exists():
                errors.append(f"이미지 파일을 찾을 수 없습니다: {img}")

    for heading in BODY_SECTIONS:
        if not extract_section(case.body, heading):
            warnings.append(f"'## {heading}' 섹션이 없습니다")

    comparison = extract_section(case.body, "대안 비교")
    if comparison:
        if len(comparison) < 30:
            warnings.append("'## 대안 비교' 섹션이 너무 짧습니다 (탈락시킨 대안이 적혀 있는지 확인)")
        elif not re.search(r"\d", comparison):
            warnings.append("'## 대안 비교' 섹션에 정량 근거(숫자)가 없습니다")

    pros_cons = extract_section(case.body, "장단점")
    if pros_cons and not re.search(r"단점|한계|트레이드오프|아쉬운", pros_cons):
        warnings.append("'## 장단점' 섹션에 단점·한계 서술이 안 보입니다")

    if "확인 필요" in case.body:
        warnings.append("본문에 '확인 필요' 표시가 남아 있습니다 (사용자에게 물어볼 것)")

    return errors, warnings


def cmd_validate(_args) -> int:
    cases = load_all_cases()
    if not cases:
        print("Cases/ 에 사례 파일이 없습니다.")
        return 0

    had_error = False
    for case in cases:
        errors, warnings = validate_case(case)
        cid = case.meta.get("id", case.path.stem)
        if not errors and not warnings:
            print(f"{cid} — 이상 없음")
            continue

        print(f"\n{cid} ({case.path.name})")
        for e in errors:
            print(f"  x {e}")
        for w in warnings:
            print(f"  ! {w}")
        if errors:
            had_error = True

    return 1 if had_error else 0


# ---------------------------------------------------------------------------
# INDEX.md 생성
# ---------------------------------------------------------------------------

def cmd_index(_args) -> int:
    cases = load_all_cases()
    lines = [
        "<!-- 이 파일은 tools/build.py index 로 자동 생성됩니다. 직접 수정하지 마세요. -->",
        "",
        "# 사례 색인",
        "",
        "| id | title | project | domain | skills |",
        "|---|---|---|---|---|",
    ]
    for c in sorted(cases, key=lambda c: c.meta.get("id", "")):
        m = c.meta
        domain = ", ".join(m.get("domain") or [])
        skills = ", ".join(m.get("skills") or [])
        lines.append(
            f"| {m.get('id', '?')} | {m.get('title', '?')} | {m.get('project', '?')} "
            f"| {domain} | {skills} |"
        )

    out = CASES_DIR / "INDEX.md"
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"작성됨: {out.relative_to(REPO_ROOT)} ({len(cases)}건)")
    return 0


# ---------------------------------------------------------------------------
# 렌더링
# ---------------------------------------------------------------------------

def rewrite_relative_srcs(html: str, base_dir: Path) -> str:
    """상대 경로 이미지 src를 절대 file:// URI로 바꾼다 (렌더 위치가 어디든 이미지가 뜨도록)."""

    def repl(m: re.Match) -> str:
        attr, quote, src = m.group(1), m.group(2), m.group(3)
        if src.startswith(("http://", "https://", "data:", "file:")):
            return m.group(0)
        candidate = (base_dir / src).resolve()
        if not candidate.exists():
            candidate = (REPO_ROOT / src).resolve()
        uri = candidate.as_uri()
        return f'{attr}={quote}{uri}{quote}'

    return re.sub(r'(src)=(["\'])([^"\']+)\2', repl, html)


def add_figure_captions(html: str) -> str:
    """단독 이미지를 <figure>로 감싸고 alt 텍스트를 캡션으로 노출한다.

    markdown은 `![설명](src)`를 <p><img alt="설명" ...></p>로만 만들어서
    alt가 화면에 안 보인다. 그림 밑에 설명이 찍히도록 바꾼다.
    """

    def repl(m: re.Match) -> str:
        img = re.search(r"<img[^>]*>", m.group(0)).group(0)
        alt_m = re.search(r'alt="([^"]*)"', img)
        alt = alt_m.group(1) if alt_m else ""
        caption = f"<figcaption>{alt}</figcaption>" if alt.strip() else ""
        return f"<figure>{img}{caption}</figure>"

    return re.sub(r"<p>\s*<img[^>]*>\s*</p>", repl, html)


def number_sections(html: str, index: int) -> str:
    """본문 섹션(<h2>)을 <h3>로 낮추고 'N.M' 번호를 붙인다."""
    counter = [0]

    def repl(m: re.Match) -> str:
        counter[0] += 1
        return f"<h3>{index}.{counter[0]} {m.group(1)}</h3>"

    return re.sub(r"<h2>(.*?)</h2>", repl, html, flags=re.DOTALL)


def render_case_html(case: Case, index: int, reason: str | None) -> str:
    m = case.meta
    body_html = md.markdown(case.body, extensions=MD_EXTENSIONS)
    body_html = rewrite_relative_srcs(body_html, case.path.parent)
    body_html = add_figure_captions(body_html)
    body_html = number_sections(body_html, index)

    tags = (m.get("domain") or []) + (m.get("skills") or [])
    tags_html = "".join(f"<span>{t}</span>" for t in tags)

    reason_html = f'<p class="case-reason"><em>{reason}</em></p>' if reason else ""

    return f"""
<div class="case">
  <div class="case-header">
    <h2>{index}. {m.get('title', m.get('id'))}</h2>
    <div class="case-meta">{m.get('project', '')} · {m.get('role', '')} · {m.get('period', '')}</div>
    <div class="case-tags">{tags_html}</div>
    {reason_html}
  </div>
  {body_html}
</div>
""".strip()


def find_browser() -> str:
    env_path = __import__("os").environ.get("CHROME_PATH")
    if env_path and Path(env_path).exists():
        return env_path

    system = platform.system()
    candidates: list[str] = []
    if system == "Windows":
        candidates = [
            r"C:\Program Files\Google\Chrome\Application\chrome.exe",
            r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
            r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
            r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
        ]
    elif system == "Darwin":
        candidates = [
            "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
            "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge",
            "/Applications/Chromium.app/Contents/MacOS/Chromium",
        ]
    else:
        for name in ("google-chrome", "chromium-browser", "chromium", "microsoft-edge"):
            found = shutil.which(name)
            if found:
                return found

    for c in candidates:
        if Path(c).exists():
            return c

    raise SystemExit(
        "Chrome/Edge를 찾을 수 없습니다. CHROME_PATH 환경변수로 실행 파일 경로를 지정하세요."
    )


def cmd_render(args) -> int:
    app_dir = Path(args.application_dir)
    if not app_dir.is_absolute():
        candidate = APPLICATIONS_DIR / app_dir
        app_dir = candidate if candidate.exists() else REPO_ROOT / app_dir

    manifest_path = app_dir / "manifest.yaml"
    if not manifest_path.exists():
        raise SystemExit(f"manifest.yaml을 찾을 수 없습니다: {manifest_path}")

    manifest = yaml.safe_load(manifest_path.read_text(encoding="utf-8")) or {}

    entries = manifest.get("cases") or []
    if not entries:
        raise SystemExit("manifest.yaml의 cases 목록이 비어 있습니다")

    case_htmls = []
    toc_items = []
    for index, entry in enumerate(entries, start=1):
        case_id = entry["id"] if isinstance(entry, dict) else entry
        reason = entry.get("reason") if isinstance(entry, dict) else None
        case = load_case_by_id(case_id)
        errors, warnings = validate_case(case)
        if errors:
            raise SystemExit(
                f"'{case_id}'가 검증을 통과하지 못했습니다:\n  x " + "\n  x ".join(errors)
            )
        for w in warnings:
            print(f"  ! [{case_id}] {w}")
        case_htmls.append(render_case_html(case, index, reason))
        toc_items.append(
            f'<li><span class="toc-num">{index}.</span>'
            f'<span class="toc-title">{case.meta.get("title")}</span></li>'
        )

    template = (TEMPLATES_DIR / "portfolio.md").read_text(encoding="utf-8")
    style = (TEMPLATES_DIR / "style.css").read_text(encoding="utf-8")

    html_body = template
    html_body = html_body.replace("{{TITLE}}", manifest.get("title", "포트폴리오"))
    html_body = html_body.replace("{{NAME}}", manifest.get("name", ""))
    html_body = html_body.replace("{{TARGET}}", f"{manifest.get('company', '')} {manifest.get('position', '')}".strip())
    html_body = html_body.replace("{{DATE}}", str(manifest.get("date", "")))
    html_body = html_body.replace("{{INTRO}}", md.markdown(manifest.get("intro", ""), extensions=MD_EXTENSIONS))
    html_body = html_body.replace("{{TOC}}", f'<div class="toc"><ul>{"".join(toc_items)}</ul></div>')
    html_body = html_body.replace("{{CASES}}", "\n<hr/>\n".join(case_htmls))

    # 골격 자체는 markdown이지만 위 치환으로 실질적으로 HTML이 섞인 상태이므로
    # 남은 순수 markdown 구간(제목·구분선 등)만 최종적으로 변환한다.
    final_html = md.markdown(html_body, extensions=MD_EXTENSIONS)

    full_html = f"""<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="utf-8">
<title>{manifest.get('title', '포트폴리오')}</title>
<style>{style}</style>
</head>
<body>
{final_html}
</body>
</html>"""

    html_out = app_dir / "_build.html"
    html_out.write_text(full_html, encoding="utf-8")

    pdf_out = app_dir / "portfolio.pdf"
    browser = find_browser()
    cmd = [
        browser,
        "--headless=new",
        "--disable-gpu",
        f"--print-to-pdf={pdf_out}",
        "--no-pdf-header-footer",
        html_out.resolve().as_uri(),
    ]
    result = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace")
    if result.returncode != 0 or not pdf_out.exists():
        print(result.stderr, file=sys.stderr)
        raise SystemExit("PDF 렌더링 실패")

    html_out.unlink(missing_ok=True)
    print(f"작성됨: {pdf_out.relative_to(REPO_ROOT)}")

    unmet = manifest.get("unmet") or []
    if unmet:
        print("\n미충족 요구사항 (JD 대비):")
        for u in unmet:
            print(f"  - {u}")

    return 0


# ---------------------------------------------------------------------------

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("index", help="Cases/INDEX.md 재생성").set_defaults(func=cmd_index)
    sub.add_parser("validate", help="전체 사례 형식 검증").set_defaults(func=cmd_validate)

    p_render = sub.add_parser("render", help="manifest.yaml -> PDF 렌더링")
    p_render.add_argument("application_dir", help="Applications/ 아래 폴더 이름 또는 경로")
    p_render.set_defaults(func=cmd_render)

    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
