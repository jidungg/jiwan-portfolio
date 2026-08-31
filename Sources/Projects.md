# 프로젝트 소스 색인

프로젝트별 소스 위치 목록이다. **로컬 디렉토리가 있으면 그것을 우선 참고**하고,
로컬에 없으면(다른 PC에서 작업하는 경우 등) GitHub 원격 레포로 폴백한다.

## CopyMaple2 (메이플스토리2 모작)

- 로컬: `D:\Workbench\Projects\CopyMaple2`
- GitHub: https://github.com/jidungg/CopyMaple2 (public)
- 참고 문서: [`Portfolios.md`](Portfolios.md)의 "최적화 사례 (3D 큐브 맵 RPG,
  MapleStory2 모작)" (Notion) — 프로파일링·최적화 상세 기록

## RTChess (Hyper Chess 모작)

- 로컬: `D:\Workbench\Projects\UnrealProjects\RTChess_5_7`
- GitHub: https://github.com/jidungg/RTChess (public)

## CopyTrickster (트릭스터 모작)

- 로컬: `D:\Workbench\Projects\Trickster\CopyTrickster-main`
  ⚠ git 저장소가 아니라 압축 해제된 스냅샷 — 버전이 최신인지 불확실.
- GitHub: https://github.com/jidungg/CopyTrickster (public) — 실제 최신 출처

## Shipgend (Ship of Fools 모작)

- 로컬: 없음
- GitHub: https://github.com/jidungg/Shipgend (private)

## ResourceMonitor

- 로컬: 없음
- GitHub: https://github.com/jidungg/ResourceMonitor (private)

## Project_DX11_PluckySquire (견습기사모험기 모작)

- 로컬: `D:\Workbench\Projects\Project_DX11_PluckySquire`
- GitHub: https://github.com/smileJiro/Project_DX11_PluckySquire (private)
- ⚠ 협업자(팀원·외부인) 계정 레포. 사례 작성 시 본인이 담당한 부분을 명시할 것.

## Dogong

- 로컬: `D:\Workbench\Projects\UnrealProjects\Dogong`
- GitHub: https://github.com/Untitled-Forge/Dogong (private)
- ⚠ 팀 프로젝트. 사례 작성 시 본인이 담당한 부분을 명시할 것.

## NifSkope (개조본 — nif → .effmodel 익스포터)

- 로컬: `D:\Workbench\Libraries\NifSkope\nifskope`
- GitHub: 없음 (업스트림 오픈소스의 로컬 개조본)
- 개조 내용: `src/niftobinary.cpp`·`src/niftobinary.h` 추가,
  `src/nifskope.cpp`의 `NifSkope::load()` 후킹, `NifSkope.pro`에 등록
- CopyMaple2의 `.effmodel` 에셋을 생성하는 툴. 관련 사례: `nif-to-effmodel`
