# 김지완 포트폴리오 제작소

JD를 입력하면 그에 맞는 문제 해결 사례를 골라 포트폴리오 PDF로 조립해내는
작업장입니다. 설계 배경은 [docs/design.md](docs/design.md), 작업 규약은
[CLAUDE.md](CLAUDE.md)를 참고하세요.

## 새 PC에서 시작하기

```bash
gh repo clone jidungg/jiwan-portfolio
cd jiwan-portfolio
py -m pip install -r requirements.txt
```

비공개 저장소이므로 각 PC에서 `gh auth login`이 한 번 필요합니다.

Chrome 또는 Edge가 자동으로 안 잡히면 `CHROME_PATH` 환경변수로 실행 파일
경로를 지정하세요.

## 구성

```
Cases/                 문제 해결 사례 라이브러리 (핵심 자산)
Templates/             사례·포트폴리오 템플릿
Applications/          지원별 JD·manifest·완성 PDF, 과거 지원 이력(Archive/)
Assets/                사례에 들어가는 이미지
Sources/               원본 자료 (읽기 전용)
tools/build.py         조립·렌더·검증 스크립트
.claude/commands/      /new-case, /review-case, /audit, /build
```

## 빌드 도구

```bash
python tools/build.py index                        # Cases/INDEX.md 재생성
python tools/build.py validate                      # 전체 사례 형식 검증
python tools/build.py render <application-dir>      # manifest.yaml -> PDF
```

Claude Code에서 작업할 때는 스크립트를 직접 부르기보다 `/new-case`,
`/review-case`, `/audit`, `/build` 슬래시 커맨드를 쓰는 것을 전제로 합니다.
