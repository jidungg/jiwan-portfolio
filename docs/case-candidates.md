# 사례 후보 목록

`Cases/*.md`로 쓸 수 있는 문제 해결 사례 후보를 프로젝트별로 모아둔 목록이다.
특정 JD를 위한 문서가 아니라, **다음에 `/new-case`를 돌릴 때 "뭘 쓸지" 고르는
출발점**으로 쓴다.

## 이 문서를 읽는 법

- 여기 적힌 것은 대부분 **커밋 로그·파일 구조에서 확인되는 사실**뿐이다. 왜 그렇게
  짰는지, 무엇이 아쉬웠는지, 어떤 대안을 고민했는지는 **적혀 있지 않다** — 그건
  사용자만 안다. 사례를 쓸 때 사용자에게 물어서 채운다. (CLAUDE.md 불변 규칙 2)
- **예외 1: Shipgend(26·40~46번).** 사용자가 블로그에 15편짜리 구조 설명 + 자가
  피드백을 직접 썼다.
- **예외 2: CopyMaple2·PluckySquire(1~8·24·25·35~39·47~56번).** 기술소개서
  원본 pptx(`Sources/포트폴리오_통합_0911_제출용/ion.pptx`, 75슬라이드)에
  **항목별 `요구 사항`과 일부 항목의 `문제점`·`설계 이유`**가 적혀 있다.
  아래 항목의 `출처: 기술소개서 슬라이드 N`이 그것이다.
- 두 경우 모두 **사용자 본인이 쓴 문장이므로 판단·의도·회고를 그대로 근거로 쓸 수
  있다.** 사례를 쓰기 전에 반드시 해당 슬라이드·글을 먼저 읽는다
  → [`Sources/Portfolios.md`](../Sources/Portfolios.md)
- Dogong(13~23번)은 devlog·glossary·memory-bank가 커밋에 함께 있어 부분적으로
  같은 성격을 갖는다.
- 남은 `확인 필요`는 대부분 **기술소개서에도 안 적힌 것**이다. 물어봐야 한다.
- 수치는 하나도 없다. 프로파일링 기록이 남아 있는 항목만 `[계측 있음]`으로 표시했다.
  나머지는 측정하지 않았거나 기록을 못 찾은 것이다.
- `⚠ 팀`은 협업 프로젝트다. 사례로 쓸 때 본인 담당 범위를 본문에 명시해야 한다.
- `? 확인 필요`는 본인 작성 범위나 소재의 실체가 불확실해서, 쓰기 전에 사용자
  확인이 필요한 항목이다.

## 후보 요약

| # | 후보 | 프로젝트 | 유형 |
|---|---|---|---|
| 1 | 그리드 큐브맵 Raycast 3D DDA | CopyMaple2 | 최적화 |
| 2 | 지형 컬링 모드 3종 비교·계측 | CopyMaple2 | 최적화 |
| 3 | 옥트리 프러스텀 컬링 도입 | CopyMaple2 | 최적화 |
| 4 | CBaseModel 추상화 → GPU 인스턴싱 | CopyMaple2 | 설계·최적화 |
| 5 | FBX/NIF 원본 에셋 → 자체 바이너리 변환기 | CopyMaple2 | 툴 |
| 6 | ~~빌드 아이템 아이콘 오프스크린 렌더 생성~~ (35번에 흡수) | CopyMaple2 | 자동화 |
| 35 | 하우징(건축) 시스템 — **작성 완료** | CopyMaple2 | 콘텐츠·시스템 |
| 36 | **JSON 기반 데이터 주도 설계** | CopyMaple2 | 설계 |
| 7 | 인벤토리/퀘스트/대화 UI 시스템 | CopyMaple2 | 콘텐츠 |
| 48 | **UI 프레임워크 (Pivot·Anchor·9 Slice·List)** | CopyMaple2 | 설계·렌더링 |
| 49 | **오브젝트 관리 (프로토타입·레이어·매니저)** | CopyMaple2 | 설계 |
| 47 | **길찾기 (A\*)** | CopyMaple2 | 알고리즘 |
| 57 | **충돌 처리 & 캐릭터 블로킹** | CopyMaple2 | 알고리즘·콘텐츠 |
| 8 | 디퍼드 렌더링 + 스킬 이펙트 파이프라인 | CopyMaple2 | 렌더링 |
| 9 | 클라 예측 + 서버 승인 기력 시스템 | RTChess | 네트워크 |
| 10 | EOS 세션 광고·발견 + 전용 서버 로비 | RTChess | 네트워크 |
| 11 | 기물 명령 체계 + 의존성 해제 리팩토링 | RTChess | 설계 |
| 12 | 기물 정의 DataAsset + 서브시스템 | RTChess | 데이터 주도 |
| 13 | 단일 월드 지역 스트리밍 + 서버 권위 텔레포트 | Dogong ⚠ | 네트워크 |
| 14 | seamless travel 후속 버그 2건 | Dogong ⚠ | 디버깅 |
| 15 | CommonUI 4레이어 UI 아키텍처 전환 | Dogong ⚠ | 설계 |
| 16 | WidgetController 인터페이스 주입 리팩토링 | Dogong ⚠ | 설계 |
| 17 | Run 통계 시스템 (서버 누적 + Multicast) | Dogong ⚠ | 네트워크·설계 |
| 18 | 세이브/로드 서브시스템 | Dogong ⚠ | 시스템 |
| 19 | enum·구조체 키 → FGameplayTag 전면 전환 | Dogong ⚠ | 리팩토링 |
| 20 | GraphMap 스테이지 진행 시스템 | Dogong ⚠ | 시스템 |
| 21 | 상호작용 시스템 통합 + 피드백 프로파일 | Dogong ⚠ | 설계 |
| 22 | 멀티플레이 로딩 스크린 | Dogong ⚠ | 시스템 |
| 23 | 장르 전환에 따른 시스템 제거 | Dogong ⚠ | 리팩토링 |
| 37 | **애니메이션 툴 (Tool_Animation)** | PluckySquire ⚠ | 툴 |
| 38 | **애니메이션 이벤트 시스템** | PluckySquire ⚠ | 툴·설계 |
| 39 | **2D 스프라이트 모델·애니메이션 파이프라인** | PluckySquire ⚠ | 툴·렌더링 |
| 52 | **3D 스켈레탈 애니메이션** | PluckySquire ⚠ | 렌더링 |
| 51 | **상호작용 시스템 + 오브젝트 (포탈·들기·밀기/당기기)** | PluckySquire ⚠ | 설계·콘텐츠 |
| 53 | **플레이어 상태 머신 (36종)** | PluckySquire ⚠ | 설계·콘텐츠 | — 작성 완료
| 54 | **플레이어 장비 5종 (검·도장·라이플·제트팩·건틀릿)** | PluckySquire ⚠ | 콘텐츠 |
| 55 | **플레이어 모드 — 플랫포머 / 보스전 (보스 FSM 16종)** | PluckySquire ⚠ | 콘텐츠·설계 |
| 56 | **Defender 미니게임** | PluckySquire ⚠ | 콘텐츠 |
| 24 | 플레이어 이동 예외 처리 다발 | PluckySquire ⚠ | 디버깅 |
| 25 | 2D↔3D 전환 플레이어 상태 구현 | PluckySquire ⚠ | 콘텐츠 |
| 46 | **엔진 기반 구조 (솔루션 3계층 + Scene/Layer/Object/Component)** | Shipgend ⚠ | 설계 |
| 40 | **2.5D 배 구현 (부모-자식 Transform)** | Shipgend ⚠ | 콘텐츠·설계 |
| 26 | **항해 시스템 (육각 CellMap)** | Shipgend ⚠ | 콘텐츠·알고리즘 |
| 41 | **상호작용 시스템** | Shipgend ⚠ | 설계 |
| 42 | **충돌 처리 시스템 (Check Matrix + Collision ID)** | Shipgend ⚠ | 설계·알고리즘 |
| 43 | **이벤트 시스템 (프레임 말 지연 처리 + 옵저버)** | Shipgend ⚠ | 설계 |
| 44 | **멀티 쓰레드 로딩 시스템** | Shipgend ⚠ | 최적화·멀티스레드 |
| 45 | **아이템 시스템** | Shipgend ⚠ | 콘텐츠 |
| 27 | WinAPI 라인 기반 지형·충돌 | CopyTrickster | 콘텐츠 |
| 28 | WMI/ETW 시스템 자원 로깅 도구 | ResourceMonitor | 툴 |
| 29 | 자료구조 템플릿 라이브러리 직접 구현 | MyTemplateLibrary | 알고리즘 |
| 30 | 직접 만든 컴파일러·언어 | MyCompiler ? | 알고리즘 |
| 31 | 코어 키퍼 맵·오브젝트 에디터 | CoreKeeperTool ⚠ | 툴 |
| 32 | Unity C# 원카드 게임 | OneCard ? | C# |
| 33 | IOCP 게임 서버 | IOCPServer / Chat ? | 네트워크 |
| 59 | **팀에 배포한 가이드 문서 (4건)** | Shipgend·PluckySquire | 협업 |
| 34 | 생성형 AI 개발 워크플로우 구축 | 3개 프로젝트 공통 | 프로세스 |

---

## CopyMaple2 (메이플스토리2 모작, DirectX11 자체 엔진, 1인)

가장 소재가 많은 프로젝트다. 자체 엔진이라 "엔진이 해주는 것"이 없어서, 설명할 거리가
전부 본인 코드 안에 있다.

### 1. 그리드 큐브맵 Raycast에 3D DDA 도입 `[계측 있음]` — 작성 완료

`Cases/raycast-3d-dda.md`. 근거: `c4abf02`, Notion 최적화 문서 2.2절.

### 2. 지형 컬링 모드 3종(NONE / PER_CELL / OCTREE) 비교·계측 `[계측 있음]`

- 근거: `795de61`(컬링 모드 분기 및 성능 계측 추가), `0dd3d89`(콜라이더·컬링
  마이크로벤치 계측), `9d967c4`(컬링 벤치에 전체 프레임 타임/FPS 계측 추가)
- 세 방식을 런타임 분기로 전환 가능하게 만들어 놓고 비교한 구조라, `대안 비교`
  섹션이 통째로 나온다. 사례 1과 짝을 이룬다.
- 확인 필요: 계측 결과 수치가 어디 남아 있는지 (콘솔 로그? Notion?)

### 3. 옥트리 + 절두체 컬링 `[본인 회고 있음]`

- 출처: 기술소개서 슬라이드 14(Octree), 15(FrustumCulling)
- 근거: `61e917a`(OctoTree FrustumCulling Added), `50d683c`(OctoTree 중복 제거)
- 내용:
  - Octree 리프 노드 하나가 큐브 맵의 셀 하나에 대응한다. 8분할을 축별 키워드로
    이름 붙였다(LBN/LBF/LTN/LTF/RBN/RBF/RTN/RTF). 자식 생성 시 부모가 최소
    인덱스(LBN)와 최대 인덱스(RTF)를 지정한다.
  - 도입 이유가 적혀 있다: 플레이어가 있는 공간과 주변만 남기고 나머지를 걸러내기
    위해서.
  - 절두체 컬링은 최종적으로 Octree와 **연계해서** 판단한다.
  - **좌표 하나로 판정하면 큰 물체가 화면에 보여야 하는데 컬링되는 문제**가 있어,
    물체보다 약간 큰 구를 정의해 그 구와 절두체를 충돌 검사한다.
- **`문제점`이 본인 문장으로 있다** — *"이 게임에서는 Octree의 적용으로 인해
  성능적 이득을 보기에는 너무 작습니다. 맵의 크기가 훨씬 커져야 이득을 볼
  것입니다."* **장단점의 '단점'과 회고가 이미 확보됐다.**
- 사례 2(컬링 3종 계측)와 합쳐 쓴다 — 도입 동기(3) + 실측 비교(2) + 본인이
  내린 판정(3의 문제점)이 한 편이 된다. **"넣었지만 이 규모에선 이득이 없었다"로
  끝나는 최적화 사례는 흔치 않다.**

### 4. CBaseModel 추상화 → GPU 인스턴싱 모델 파생

- 근거: `50c4be0`(CBaseModel 추상 기반 클래스 신설) → `99b624c`(CModel이 상속하도록
  리팩토링) → `5b9ae76`(INSTANCE_DATA 구조체 추가) → `5a9f70b`(CInstancedStaticModel
  엔진 구현) → `9d35b02`(HLSL 셰이더 + Loader 등록)
- 설계 문서와 구현 플랜이 커밋에 함께 있다: `a9792ab`, `b3974c0`.
- **동기가 확인됐다 — 포트폴리오 슬라이드 18 `맵 오브젝트 구조 변경`.** 맵
  오브젝트 대부분이 큐브 형태인데 큐브형과 비큐브형을 동일하게 취급하고 있었다.
  이를 ① 큐브 충돌로 처리 가능한 것 ② 동일 큐브 메시로 인스턴싱 가능한 것으로
  나눴고, 결과로 **드로우콜·필요 리소스 대폭 감소 + 충돌을 Mesh에서 AABB로 강등**
  두 가지를 함께 얻었다.
- **렌더링 최적화와 충돌 최적화가 같은 구조 변경에서 동시에 나온 사례다.**
  "자료구조를 나눴더니 두 군데가 같이 좋아졌다"는 이야기가 되어, 단순 인스턴싱
  적용기보다 강하다.
- 리팩토링이 먼저 있고 그 위에 신규 기능이 올라간, 흔치 않게 깔끔한 커밋 라인이다.
  객체지향 설계 이야기를 하기에 가장 좋은 소재.
- RTChess에도 같은 기법을 다시 썼다(포트폴리오 슬라이드 16 — 체스 보드에
  Instanced Static Mesh 적용). **두 프로젝트에 걸친 반복 적용**으로 쓸 수 있다.
- 확인 필요: 드로우콜 수치를 측정했는지.

### 5. FBX/NIF 원본 에셋 → 자체 바이너리 포맷 변환기

- 근거: `FBXConverter/`(assimp 사용), `NIFToBinary/`(niflib 사용) 별도 vcxproj.
  `bf00370`(FBXConverter project added), `cf6cab7`(nif Binary read .effmodel files)
- 메이플2 원본 리소스가 `.nif`라 직접 파서를 붙여야 했던 것으로 보인다.
- 확인 필요: 왜 런타임 로딩이 아니라 사전 변환을 골랐는지, 로딩 시간 차이를
  측정한 적이 있는지.

### 6. 빌드 아이템 아이콘을 오프스크린 렌더로 생성 — **35번에 흡수됨**

`Cases/housing-map-serialization.md`의 "건설 아이템 489종과 아이콘" 절에 들어갔다.
문제 정의("489종을 UI에서 구분·선택하게 해야 한다")가 하우징과 이어져서 따로
떼면 배경이 사라진다. **단독 사례로 다시 쓰지 않는다.**

- 근거: `c9f460b`(Auto making HomeDialog item icon img), `89da48b`(BuildItem 모델
  파일을 읽어 BuildItemData 생성), `3614a1f`(BUILD_ITEM_ID enum 값 입력)
- 확인된 사실: `CItemDataBase::Initialize()`가 300×300 렌더 타겟에 건설 아이템
  모델을 하나씩 그려 `<모델명>_icon` 텍스처 프로토타입으로 등록한다. **실행할
  때마다 다시 굽고 캐시하지 않는다.** 아이템 데이터 자체도 `resources/FBXs/MAP`
  아래 `.model` 489개를 재귀 스캔해 파일명 규칙으로 분류한 것이라, 자동화 전에
  손으로 넣던 단계는 없다(모델 파일이 없는 스포너·포탈만 json에 수기 등록).

### 35. 하우징(건축) 시스템 — 작성 완료

`Cases/housing-map-serialization.md`. 6번(아이콘 오프스크린 렌더)을 흡수했다.
아래는 작성 당시의 조사 메모.

- 근거: `17db49a`(맵 피킹, BuilderBird 소환), `38cebca`(블록 설치),
  `88e1372`(BuildItemReadByFile 브랜치 머지), `89da48b`, `8018208`(HomeDialog
  ScrollBar)
- 파일: `Builder`(CPawn 파생 — 건축 모드 조작 주체), `BuildPreview`(CTerrainObject
  파생 — 설치 미리보기), `InvenBuildSlot`(CInvenSlot 파생 — 좌/우클릭 오버라이드),
  `Level_Home`, `UIHomeDialog`, `Item.h`의 `BUILD_ITEM_DATA`
- 구현에서 확인되는 것:
  - `CBuilder`가 `CTerrain`(그리드 큐브맵) 참조를 들고 미리보기 오브젝트와
    새(`m_pBird`) 모델을 각각 오프셋을 두고 따라다니게 한다.
  - `m_bBuildable` 플래그와 **설치 가능/불가 마커 두 개**(`m_pCubeMarkerEnable` /
    `m_pCubeMarkerDisable`)를 따로 들고 있다 — 설치 가능 여부를 플레이어에게
    시각적으로 되돌려주는 구조.
  - `BUILD_ITEM_DATA`는 `TERRAINOBJ_BLOCK_TYPE`과 `BUILD_ITEM_TYPE`을 갖는다.
    지형 오브젝트 타입 체계와 아이템 체계가 이 지점에서 만난다.
- **맵 데이터 직렬화가 이 사례의 핵심이다** (기술소개서 슬라이드 10). 맵을 json으로
  파싱·언파싱하며, 셀마다 `Direction`(4방) · `Index`(셀 인덱스) · `ItemId` ·
  `Iteration` · `ParentIndex` · `IntData` · `FloatData` 속성을 갖는다.
  - **`Iteration`은 본인이 고안한 압축이다.** 같은 블록이 연속되는 횟수를 적어
    json 객체 수를 줄인다 — 예시로 블록 '90'이 0~100번까지 연속 존재하는 경우가
    객체 하나로 저장된다. **포트폴리오 슬라이드 7에서 본인이 이를 RLE라고 부른다.**
  - 같은 슬라이드에 **"셀 좌표 단일 정수화"**가 나란히 적혀 있다 — 3D 좌표를
    인덱스 하나로 접는 것(6번 슬라이드의 `x + X*z + X*Z*y`)이 저장 포맷을
    단순하게 만든 근거다.
- 조작(기술소개서 슬라이드 11): `B`로 건설 모드 진입 → 건설 메뉴에서 자재 선택 →
  방향키·WS로 Builder 이동 → `SPACE` 배치 · `R` 회전 · `E` 삭제.
- 포트폴리오 슬라이드 7은 이걸 **UGC 제작 컨텐츠**로 규정하고, `맵 제작 툴`,
  `런타임 맵 데이터 수정`, `런타임 동적 UI 아이콘 생성`(6번)을 함께 묶는다.
- **그리드 큐브맵 위에 오브젝트를 놓는 시스템이라, 1번(Raycast/맵 피킹)·
  3번(컬링)·47번(A*)과 같은 지형 구조를 공유한다.** 최적화 사례들과 배경을 나눠 쓸
  수 있어 문서 전체의 일관성이 좋아진다.
- **`자료구조·알고리즘`을 요구하는 JD에서 의외의 카드다** — 압축 저장 포맷을
  직접 설계한 이야기라, 라이브러리 구현(29번)보다 실전 근거가 된다.
- 확인 필요: 설치 가능 판정을 무엇으로 하는지(셀 점유? 충돌?), `Iteration` 도입
  전후 파일 크기를 비교해봤는지, BuilderBird가 왜 필요했는지.

### 36. JSON 기반 데이터 주도 설계

- 근거(파일): `Item`, `Monster`, `NPC`, `Quest`, `Skill`, `Conversation`,
  `DropTable`, `Spawner`, `Status`, `TerrainObject`, `Effect`, `PortalTerrainObject`,
  `Player` — **13개 이상의 헤더가 `json&`을 받는 생성자를 갖고 있다.**
  `ItemDataBase` / `MonsterDataBase` / `NPCDataBase` / `QuestDataBase` 싱글톤 4종이
  타입별 `map<_uint, *_DATA*>`으로 들고 있다가 키로 내준다.
- `ITEM_DATA`를 기반으로 `BuildItemData` / `EquipItemData` 등이 상속으로 갈라진다.
- **콘텐츠를 코드 밖으로 뺀 이야기.** 12번(RTChess DataAsset)과 같은 계열인데
  이쪽은 자체 엔진이라 로더까지 직접 만들었다.
- 확인 필요: JSON을 손으로 썼는지 툴로 뽑았는지, 원본 게임 데이터를 추출한 건지.

### 7. 인벤토리 / 퀘스트 / NPC 대화 UI 시스템

- 근거: `aec76b6`(Inventory Completed), `af929f7`(Inventory Scrolling),
  `fde54c6`(Quest system), `2283d33`(NPCConversationDialog), `42b0777`(퀘스트 포기),
  `b20a4ad`(QuestGuide), `6c4f47b`(UIContainer의 자식들은 겹쳐도 되도록 수정),
  `bc8314b`(UIDrag), `8018208`(ScrollBar)
- 자체 엔진에 UI 프레임워크를 직접 얹은 이야기. 컨테이너·스크롤·드래그를 손으로
  만든 건 UI 툴킷 없는 환경에서만 나오는 소재다.
- 확인 필요: 어떤 컨테이너 모델을 택했는지, 왜 그 구조였는지.

### 48. UI 프레임워크 — Pivot & Anchor, 9 Slice Scaling, UI List

- 출처: 기술소개서 목차 6장 "UI"(p.17) — UI Manager / Pivot & Anchor /
  9 Slice Scaling / UI List
- 근거: `08e4eb9`(UI9Grid Shader Added), `6c4f47b`(UIContainer의 자식들은 겹쳐도
  되도록 수정), `b46e3f6`·`af929f7`(Inventory Scroll/Scrolling), `bc8314b`(UIDrag),
  `8018208`(ScrollBar)
- 파일: `UIContainer`, `UIPanel`, `UIList`, `UIListItemEntry`, `UIListSelector`,
  `UIScroller`, `UIScrollButton`, `UIVerticalFill`, `UIBundle`, `UISlot`
- **엔진에 UI 툴킷이 없는 상태에서 상용 엔진의 UI 개념을 직접 구현한 이야기다.**
  기술소개서에 **무엇을 모방했는지 본인이 밝혀놨다** — Pivot & Anchor와 9Slicing은
  Unity, UI List는 Unreal의 UI List View.
- 기술소개서 슬라이드 17~21 내용:
  - 요구사항 6개: UI도 게임 오브젝트여야 함 / 자식 UI가 부모에 부착 / **테두리가
    있는 UI는 스케일링해도 테두리 크기가 변하면 안 됨** / 화면 크기가 달라지면
    비율에 맞춰 위치 조정 / **시각적으로 가장 위에 있는 UI가 우선 상호작용** /
    일부는 드래그로 이동.
  - `CUIManager`는 **정수형 우선순위**로 마우스 입력을 받을 UI를 판별한다.
    Focused / Pressed / Drag 중인 UI 포인터를 각각 들고 있고, **클릭되거나 새로
    생성될 때 가장 높은 우선순위를 새로 부여**한다.
  - Pivot(자신의 기준점) / Anchor(부모 또는 화면 내 기준 위치)를 중앙 + 8모서리를
    뜻하는 `CORNOR_TYPE` enum으로 설정한다. **부모의 Pivot 위치 = 자식의 Anchor
    위치**라는 규칙이 명시돼 있다.
  - 9Slicing은 픽셀 셰이더로 처리한다. LEFT·RIGHT는 Y축만, TOP·BOT은 X축만
    스케일링한다.
  - UI List는 데이터 목록만 넘기면 UI가 자동 생성·배치된다. **보이지 않는 행·열은
    Deactive로 관리해 성능 부담을 줄인다**고 장점에 적혀 있다. 사용처는
    HomeDialog와 Inventory.
- 7번(인벤토리/퀘스트/대화)이 이 프레임워크 위에 올라간 콘텐츠다. **48이 기반,
  7이 응용.** 둘을 합치면 길고, 나누면 48 쪽이 기술 사례로 강하다.
- 포트폴리오 슬라이드 4가 이걸 **"공통 UI 컴포넌트 조합 / 게임 특화 UI"** 2층
  구조로 요약한다. 사례의 도입부로 쓸 수 있다.
- 확인 필요: 9 Slice를 셰이더로 푼 이유(버텍스 분할 대신), UI List의 Deactive
  처리로 무엇이 얼마나 좋아졌는지 측정했는지.

### 49. 오브젝트 관리 — 프로토타입 · 레이어 · 매니저

- 출처: 기술소개서 목차 1장 "오브젝트 관리"(p.5) — **문서 맨 앞에 놓았다는 건
  본인이 이걸 기반 구조로 봤다는 뜻이다.**
- 근거: 클래스마다 `static constexpr _tchar m_szProtoTag[]`와 `Clone(void* pArg)`
  가 있다(예: `CBuilder`, `CBuildPreview`). `Loader`, `Level_Loading`이 프로토타입
  등록을 담당. `7254017`(레퍼런스 관리 코드 추가 — AddChild, AddToLayer)
- 파일: `Loader`, `RenderObject`, `ModelObject`, `GameObject` 계층
- 기술소개서 슬라이드 5~6에 구조가 정리돼 있다:
  - **레벨 → 레이어 → 오브젝트 → 자식 오브젝트**의 계층 구조. 부모-자식 관계는
    재귀적이며, 순회도 세 단계로 내려간다.
  - **큐브 맵**: 3차원 공간을 정육면체 단위로 분할하고 자식 오브젝트를 **1차원
    배열**로 관리한다. 셀 인덱스 계산식이 명시돼 있다 — `x + X*z + X*Z*y`,
    최대 인덱스는 `X*Z*Y-1`.
  - 이 구조를 고른 이유가 넷 적혀 있다: 인덱스로 임의 접근, 맵 저장·불러오기
    유리, 셀 단위 컬링·Octree·Voxel Traversal에 유리, 셀 크기가 일정해 월드
    좌표↔셀 인덱스 변환이 쉬움.
- **이 하나의 결정에서 1·3·35·47·57번이 전부 파생된다.** 문서 앞에 이걸 놓고
  나머지를 그 위에 얹으면 사례들이 흩어지지 않는다. 기술소개서도 이 순서다.
- **프로토타입 패턴 + 레이어 관리 + 참조 카운트**가 한 덩어리. Shipgend 46번
  (Scene/Layer/GameObject/Component + Base 참조 카운트)과 **같은 문제를 몇 달 뒤에
  다시 푼 것이다.** 두 개를 나란히 놓으면 무엇이 달라졌는지 말할 수 있다.
- 확인 필요: 왜 프로토타입 방식을 골랐는지, Shipgend 때와 무엇을 바꿨는지.
  (Shipgend 쪽은 블로그에 답이 있으니 비교가 가능하다)

### 57. 충돌 처리 & 캐릭터 블로킹

- 출처: 기술소개서 슬라이드 22~24
- 파일: `Engine`의 `ColliderBase` 파생들, `Client`의 `Terrain`, `Player`
- 내용:
  - `CColliderBase`가 포함·겹침·레이캐스트 인터페이스를 정의하고, 모양별
    하위 클래스(AABB / Sphere / Frustum / Mesh)가 구현을 채운다. 내부적으로
    DirectX11의 `Bounding___` 구조체와 `ID3D11Buffer`를 쓴다.
  - **큐브 맵을 이용한 추려내기**: 캐릭터가 현재 위치한 셀의 인덱스를 기준으로
    주변 셀 인덱스 범위를 계산해, 그 범위만 순회하며 충돌 검사한다.
  - **캐릭터 블로킹**이 이 항목의 핵심이다. 이동량으로 다음 위치를 구하고 →
    머리 높이에서 전방 Raycast로 벽 감지 → 실패 시 수동 AABB 검사 →
    **`Clamp` 함수로 충돌 깊이를 계산** → 캐릭터와 셀의 위치 관계로 어느 방향에서
    충돌했는지 판정 → 방향과 깊이로 다음 위치를 수정해 **슬라이딩**시킨다.
  - 슬라이드에 X-, X+, 가운데 충돌 세 경우의 그림이 있다.
- **1번(3D DDA)과 같은 Raycast를 쓰지만 목적이 다르다** — 1번은 "무엇에 맞는가",
  57번은 "맞았을 때 어디로 밀어내는가". 묶어 쓰면 캐릭터 이동 한 편이 된다.
- PluckySquire 24번(StepAssist·벽 타기)이 **PhysX로 같은 문제를 푼 버전**이다.
  자체 구현 vs 물리 엔진 비교가 가능하다.
- 확인 필요: 머리 높이 Raycast를 먼저 하고 실패 시 AABB로 폴백하는 이유.

### 47. 길찾기 (A*)

- 출처: 기술소개서 목차 8장 "길찾기(A*)"(p.25)
- 근거: `8fb1691`(몬스터 WayFinder 버그 수정)
- 파일: `Client/Public/WayFinder.h` — `CComponent` 파생
- 구현에서 확인되는 것:
  - `ASTARCELL` 구조체가 `iIdx` / `iPIdx`(부모) / `fG` / `fH` / `fF`를 갖는다.
    표준 A* 그대로다.
  - `unordered_map<_int, ASTARCELL>`으로 셀을 들고, `MakeAStarRoute`가 경로를
    만든 뒤 `list`에 저장한다. `Get_NextStation` / `Get_FirstStation` /
    `Is_LastStation`으로 이동 주체가 한 칸씩 뽑아 쓴다.
  - `FindWay(vStart, vGoal, iSearchRange, bXZOnly)` — **탐색 범위 상한과 XZ 평면
    한정 옵션**이 인자로 있다. 그리드가 3D 큐브맵이라 Y축을 뺄 수 있게 해둔 것.
- **1번(3D DDA Raycast)·2번(컬링)과 같은 그리드 지형 위에서 도는 알고리즘이다.**
  세 개를 묶으면 "그리드 큐브맵이라는 자료구조 하나에서 파생된 알고리즘 3종"이
  되어 문서 구성이 깔끔해진다.
- 기술소개서 슬라이드 25가 요구사항과 핵심 아이디어를 적어놨다:
  - 요구사항 — 몬스터가 조작 없이 주변 적을 공격해야 하고, 지형에 막히면 스스로
    길을 찾아야 하며, **평지뿐 아니라 상하 이동도 가능해야 한다.**
  - 큐브 맵의 각 셀을 노드로 하는 그래프를 만들어 A*를 돌린다.
  - **몬스터가 이동 중 다른 셀에 진입할 때마다 경로를 다시 계산한다.**
  - 다음 경로에 높이 차가 있으면 점프한다.
- **`자료구조·알고리즘`을 요구하는 JD에서 26번(Shipgend 육각 CellMap)과 함께 쓴다.**
- 확인 필요: 휴리스틱을 무엇으로 잡았는지(맨해튼? 유클리드?), `iSearchRange`를
  둔 이유(성능? 몬스터 인지 범위?), 셀마다 재계산하는 비용을 재봤는지.

### 50. 렌더링 (DirectX 11) — 8번 참조

기술소개서 목차 9장 "렌더링(DirectX 11)"(p.26)이 별도 장으로 있다. 8번(디퍼드
렌더링 + 스킬 이펙트 파이프라인)과 겹치므로 **별도 후보로 세지 않는다.** 사례를
쓸 때 기술소개서 26쪽을 먼저 읽고 8번을 보강할 것.

### 8. 디퍼드 렌더링 + 스킬 이펙트 파이프라인

- 근거: `e7713d3`(Deffered Shader & Skill Effect, Skill func), `8822910`(Particle
  Buffer, Particle class), `e21babc`(Effect Billboard Node),
  `c2a310a`(EffTextureTransform Control), `6e189fb`(FlipController),
  `468d07f`(Billboard logic 수정), `f6daa6c`(EffBone의 루트 본 매트릭스에 월드
  매트릭스를 곱하는 게 문제인 듯 — 원인 추적 중 상태로 남은 커밋)
- `f6daa6c` 커밋 메시지가 추적 중인 상태 그대로라, **디버깅 사례로 풀 여지가 있다.**

### 그 밖에 (짧아서 단독 사례는 어려운 것)

- `8fb1691` 몬스터 WayFinder 버그 수정 — 길찾기. 내용 확인 필요.
- `c88e5db` Player Statemachine 버그 수정
- `7632959` Layer ID 기반 CollisionMgr — 충돌 레이어 설계
- `209e068` 레벨 전환 시 멈추는 버그 / `a377595` 메모리 누수
- `b8fdccb` StateMachine OnStateChange 콜백 / `0437b22` 애니메이션 종료 알림

---

## RTChess (Hyper Chess 모작, Unreal 5.7, 1인)

Unreal + 멀티플레이 소재의 본진.

### 9. 클라이언트 예측 + 서버 승인 기력(Energy) 시스템

- 근거: `4421da6`(Energy 시스템 추가), `b40072e`(클라이언트 기력 예측 로직 추가.
  클라이언트 기력 소비 즉시 적용 후 서버 승인 로직 추가)
- 파일: `UI/EnergyBarWidget`, `UI/EnergyCountWidget`
- 실시간 체스라 기력이 곧 행동 자원이고 입력 지연이 바로 체감되는 구조.
- 확인 필요: 예측이 빗나갔을 때 어떻게 되돌리는지(롤백? 스냅?), 승인 실패 케이스를
  실제로 만들어봤는지.

### 10. EOS 세션 광고·발견 + 전용 서버 로비

- 근거: `54c7f52`(게임 세션 시스템 추가 — EOS, 전용 서버, 로비), `c0c9451`(세션
  광고 및 발견)
- 파일: `Lobby/LobbyGameMode`, `Lobby/MainMenuPlayerController`,
  `UI/SessionListEntryWidget`
- 확인 필요: 리슨 서버가 아니라 전용 서버를 고른 이유.

### 11. 기물 명령 체계 + ChessBoard 의존성 해제 리팩토링

- 근거: `4c6a9af`(기물 명령 체계 구축), `cc1d7c9`(RPC로 명령 내리기),
  `f5fd833`(기물 Ownership 구현), `3457da4`(멀티플레이어 각자 자기 Pawn 소유),
  `1789c09`(Piece, PC → ChessBoard 의존성 해제)
- 파일: `Components/PieceMovementComponentBase`, `PieceJumpMovementComponent`,
  `SelectorComponent` / `SelectableComponent`, `Board/BoardRulesComponent`
- 컴포넌트 분리 + 소유권 모델 + RPC가 한 덩어리로 묶인다. JD가 OOP를 우대하면
  4번(CopyMaple2)과 이것 중 하나를 고른다.

### 12. 기물 정의 DataAsset + PieceDefinitionSubsystem

- 근거: `37aa92e`(게임 데이터 DataAsset으로 설정하기)
- 파일: `Data/PieceDefinitionDataAsset`, `Core/PieceDefinitionSubsystem`,
  `Data/BoardSetupDataAsset`, `Data/RTChessVFXSettingsDA`
- 하드코딩된 기물 규칙을 데이터로 뺀 이야기. 짧다.
- 확인 필요: 1인 프로젝트인데 데이터로 뺀 이유. "기획자가 만질 수 있게"는 추측이라
  쓰면 안 된다.

---

## Dogong (Unreal, 팀 프로젝트 ⚠, Untitled-Forge)

기여 규모: 전체 커밋 중 사용자(`jidungg` + `Codal`) 약 428커밋으로 1위.
PR 기반 협업(#96~#124 구간 확인). **팀 프로젝트이므로 사례마다 본인 담당을
명시해야 한다.**

이 프로젝트는 `devlog`·`glossary`·`memory-bank` 문서가 커밋에 함께 남아 있어서,
**"왜 그렇게 했는가"의 근거를 유일하게 문서로 확인할 수 있는 프로젝트다.**
사례 쓸 때 `.claude/docs/`와 devlog를 먼저 읽을 것.

### 13. 단일 월드 지역 스트리밍 + 서버 권위 텔레포트 (삽입/추출)

- 근거: `a09f1057`(리슨 서버 단일 월드 채택 기록), `5ad6c935`(기지↔약탈 이동을
  per-client 트래블로 전환), `87cf21b2`(서버·레벨 구조 4.3→4.1 번복 기록,
  DL-20260819-01), `ac5d2b4f`(단일 월드 전환 및 텔레포트 통일 — 번복),
  `42f13ff0`(최종 구현), `02a3bb38`(데디케이티드 서버 빌드 타겟 추가)
- **설계를 채택했다가 되돌린 기록이 devlog에 두 번 남아 있다.** 포트폴리오에서
  보기 드문 소재고, 회고 섹션이 자연스럽게 채워진다.
- 확인 필요: 4.3안이 왜 안 됐는지 (devlog에 있을 가능성이 높다).

### 14. seamless travel 후속 버그 2건

- 근거: `ed8ee126`(seamless travel 후 클라 GAS 입력 무시 수정),
  `1a5732de`(seamless travel 시 클라 로딩 스크린 미종료 수정)
- 둘 다 "서버는 멀쩡한데 클라만 깨지는" 유형. 13번의 후속이라 묶어 써도 되고,
  분량이 필요하면 독립 디버깅 사례로 떼도 된다.

### 15. CommonUI 기반 Lyra식 4레이어 레이아웃 전환

- 근거: `daf0f956`(CommonUI 기반 Lyra식 4레이어 레이아웃 + MainMenu 팝업 스택 전환),
  `c403644d`·`253d47b8`(RunResult/GraphMap을 PrimaryGameLayout 레이어로 전환),
  `4476b14b`(PrimaryLayout 소유권을 ADogongHUDBase로 이전), `a6429017`(레벨별 HUD BP
  신설 및 GameMode/PC 재배선), `18c7b0b5`(ActivatableWidget 입력 모드·포커스·Back
  처리 정합성 보강), `adead01e`(위젯 델리게이트 바인딩을 AddUniqueDynamic으로 —
  중복 발화 버그)
- 설계 문서가 같이 있다: `27321110`(systemPatterns에 결정 D1~D6 기록),
  `7d084e34`(UI-Architecture-v3 실무 가이드), `48685e41`(UI Stack 입력/Back/Focus 표
  + 풀링·AddDynamic 함정 기록), `4d02005c`·`808fb6d3`(다이어그램 HTML)
- **결정 6건에 번호가 붙어 문서화돼 있고, 그중 `3f4f8f49`에서 WP-2를 되돌렸다.**
  13번과 함께 "설계 판단" 계열 사례의 최상급 소재.

### 16. WidgetController 오너 주입을 인터페이스로 분리

- 근거: `c6f45d2f`(위젯 컨트롤러·오너 주입을 인터페이스로 분리, WP-4/D5),
  `4efcc5a7`(WidgetController를 Base(PC-only)/AttributeBase(ASC)로 분리),
  `07bb44c1`(컨트롤러를 BP 지정형으로 + 미사용 Status 멤버 제거),
  `3f4f8f49`(WidgetController ASC 분리 WP-2 되돌리기)
- 15번의 하위 항목. 분리해서 쓰면 OOP 전용 사례가 된다.

### 17. Run 통계 시스템 — 서버 전용 누적 후 Multicast

- 근거: `94b85ef0`(GES에 DamageApplied 이벤트 추가), `f05205cd`(데미지 적용 시 GES
  broadcast), `41d1677e`(데미지 통계 필드 추가 + 서버 전용 누적, **런중 복제 제거**),
  `3085c8db`(통계 스냅샷 타입 + run-global 카운터), `599d1136`(런 종료 시 통계
  최종화 + Multicast 전달), `a3065e83`(FDogongPlayerStatEntry가 FDogongRunStatistics를
  합성하도록 변경), `cf6d588a`(사망 시 Killer 폴백 — 마지막 데미지 공격자 캐시)
- **"매 프레임 복제하지 않고 종료 시점에 한 번 보낸다"는 판단이 커밋에 명시돼 있다.**
  네트워크 대역 이야기를 할 수 있는 몇 안 되는 소재.
- 설계 문서: `b65efa29`(RunStatistics 스펙 및 설계 결정 문서)
- 검증 흔적: `4c7e90da`(통계 스냅샷 플레이어별 값 로그 덤프), `9de9fa8a`(테스트
  DataAsset 축소 — GraphMap 3x3, Stage 1개)

### 18. 세이브·로드 서브시스템

- 근거: `3e940d23`(Run 세이브 페이로드 struct 정의) → `81dd9a1f`(USaveGame 파생
  UDogongRunSaveGame) → `19c3068a`(SaveLoad GameInstance 서브시스템 stub) →
  `caad538a`(ADogongRun 저장/복원 시접 stub) → `afb0b8ee`(디스크 I/O 구현) →
  `33d3102f`(ADogongRun 저장/복원 + 방 경계 저장 트리거) → `cf6891c3`(클리어 상태
  복원 시 전투 스폰 억제) → `950e971c`(이어하기 분기 + 메뉴 진입점),
  `509a10aa`(MainMenu 이어하기/새로하기 팝업)
- stub부터 단계별로 쌓아 올린 커밋 라인이 그대로 남아 있다. **"큰 기능을 어떻게
  쪼개서 미는가"를 보여주기 좋다.**
- 확인 필요: 저장 시점을 왜 방 경계로 잡았는지.

### 19. enum·구조체 키를 FGameplayTag로 전면 전환

- 근거: `8d24bf39`(Location.Weighted.* / Location.Fixed.* native 태그 등록),
  `13e3f90a`(FDogongRoomKey / EDogongWeighted|FixedLocation 제거, FGameplayTag 통일),
  `38c4154c`(GraphMap Cell·Settings 전환), `b305c118`(GraphMap UI 전환),
  `c4b7a1e2`(테스트 DataAsset을 태그 키 모델로 재입력), `50303010`(ClassDiagram +
  StageSystem-guide 갱신), `e49cffe1`(systemPatterns.md 갱신)
- 타입 하나를 바꾸느라 C++·에셋·문서까지 연쇄로 고친 리팩토링. **범위가 큰 변경을
  어떻게 쪼개서 밀었는지**를 보여줄 수 있다.
- 확인 필요: enum으로 시작했다가 바꾼 이유.

### 20. GraphMap 스테이지 진행 시스템

- 근거: `43918fe1`(RoomBase, BattleRoom 클래스), `8a9cf4a6`(EventRoom 클래스 +
  ELocationEventType), `7c749604`(Stage 인스턴스 교체 방식으로 전환),
  `0985b4a4`(UDogongStage를 ADogongRun으로 흡수하고 단일 스냅샷 복제로 전환),
  `02f25640`(Server RPC 기반 방 이동 + RoomClearCondition GC 크래시 수정),
  `6d50d99c`(Weighted/Fixed Location 분리 + Server RPC를 PC로 이전),
  `17b6206a`(TeleportPlayersToRoomStart 다중 PlayerStart 분산 스폰),
  `c62fb50f`(두 번째 스테이지부터 Start Sublevel이 비-Start Room에 잔존하는 버그),
  `e0a6865a`·`410cccb6`(GraphMap 노드 스타일·레이아웃 하드코드 외부화),
  `566c195e`(패키징 빌드에서 GraphMap UI 미초기화/크래시 수정),
  `e130eb5e`(스테이지 클리어 후 보스 방 노드 표시 버그)
- 파일: `Systems/GraphMapSystem/DogongGraphMap`, `GraphMapSettings`, `GraphMapTypes`
- 사용자가 가장 오래 붙든 시스템. **`0985b4a4`의 "Stage를 Run으로 흡수"는 클래스
  2개를 1개로 줄인 판단이라 단독 사례가 된다.**

### 21. 상호작용 시스템 통합 + 상태별 피드백 프로파일

- 근거: `4606e969`(IInteractable 인터페이스 추가), `db42ceeb`(포탈 인터랙트 PoC),
  `ee6c35ff`(InteractComponent로 통합 + 머리 위 스택 패널 UI),
  `413ba77c`(InteractComponent state별 FeedbackProfile 시스템 도입),
  `ad4a4609`(InteractableNameWidget를 범용 DisplayNameWidget으로 분리 + owner
  주입용 DogongWidgetComponent), `469befc1`(인터랙터블 포커스 시각 피드백)
- PoC → 인터페이스 → 컴포넌트 통합 → 데이터화 순서가 커밋에 그대로 보인다.

### 22. 멀티플레이 지원 로딩 스크린

- 근거: `27dd33d4`(UDogongLoadingScreenManager 추가 및 Lobby 토글 테스트),
  `7db9e41a`(멀티플레이어 지원 로딩 스크린 시스템 구축),
  `ca09b971`·`2b4cea44`(로딩 텍스트 + 점 루프 애니메이션, visibility 전환으로
  자동 시작·정지)
- 14번(로딩 스크린 미종료 버그)과 직결. 묶어 쓰면 "만들고 → 깨지고 → 고쳤다"가 된다.

### 23. 장르 전환에 따른 시스템 제거

- 근거: `ad049041`(로그라이트 시스템 및 WaveSystem 제거 — 익스트랙션 전환),
  `0d00d616`(로그라이크 스테이지 맵·ExternalActors 삭제),
  `1dbfaabf`·`af80b005`(레거시 어트리뷰트셋 4종을 Legacy로 분리 후 제거),
  `d411804f`(메모리뱅크·docs·commands·skills 정리)
- **만든 걸 지우는 작업**이라 포트폴리오에 잘 안 나오는 소재. 팀 방향 전환에
  코드베이스를 맞춘 이야기로 쓸 수 있다.
- 확인 필요: 장르 전환 결정에 본인이 얼마나 관여했는지. 관여 안 했으면 "대응"으로만
  써야 한다.

### 그 밖에

- `54f94bb5` 플레이어 대시 어빌리티(모션 워핑 기반) + `c13cbb51` 설계 스펙 문서
- `b0801011` Enemy 피격 반응 시스템(UDogongHitReact) + `01822e83` 피격 시 공격자 바라보기
- `1cae119f` Dogong prefix 일괄 rename + `d0b0ac6f`·`5d44470b` CoreRedirects 정리,
  `3e2388c3` StructRedirects 손실 복구 — **대규모 rename을 에셋 참조 안 깨고 미는 작업**
- `8dcd5736` 격한 움직임·회전 시 클로딩 이상 동작 수정
- `95b49247` GameEventSubsystem 초기 구현 → `b426096a` WorldSubsystem에서
  GameInstanceSubsystem으로 변경 (수명 범위 판단)
- `3ae30748` 도메인 언어 glossary 도입, `2254825b` 등급·품질 용어 정리
- `09aa29db` 패키징 로그 에러·경고 정리

---

## Project_DX11_PluckySquire (견습기사모험기 모작, DX11 자체 엔진, 7인 팀 ⚠)

기여 규모: 사용자 762 + 32커밋으로 팀 내 2위.

**주의 — 이 프로젝트에서 눈에 띄는 커밋 상당수는 본인 것이 아니다.** PhysX
simulate→fetchResults 시점 분리(`0fabaf5a5`), 메모리 릭 전수 해결(`466c6d15d`),
Frustum Culling 버그(`2d77ca90b`), Level Light Tool(`3e7eec602` 등), NewRenderer
리팩토링(`af93c7bf4`)은 전부 `smileJiro` 커밋이다. 엔진의 `ThreadPool`도
`smileJiro`, `Compute_Shader`·`Json_Manager`는 `nyongking`이다.

**본인 담당 범위는 기술소개서 목차(p.31~73)가 확정해 준다.** 사용자가 자기
기술소개서에 자기 작업으로 실은 항목들이므로, 커밋 작성자 통계보다 이쪽이
우선한다. 11개 장 전부가 아래 후보에 대응한다.

| 기술소개서 | 쪽 | 후보 |
|---|---|---|
| 1. 상호작용 시스템 | 31 | 51 |
| 2. 상호작용 오브젝트 (포탈 / 물건 들기 / 밀기·당기기 / 그 외) | 34 | 51 |
| 3. 애니메이션 (3D 스켈레탈 / 2D 스프라이트 / 애니메이션 이벤트) | 41 | 52, 39, 38 |
| 4. 캐릭터 이동 보조 | 49 | 24 |
| 5. 플레이어 상태 | 50 | 53 |
| 6. 벽 타기 | 52 | 24 |
| 7. 플레이어 장비 (검 / 도장 / 라이플 / 제트팩 / 건틀릿) | 55 | 54 |
| 8. 플레이어 모드 (플랫포머 / 보스전) | 65 | 55 |
| 9. Defender (미니게임) | 68 | 56 |
| 10. 애니메이션 툴 | 70 | 37 |
| 11. 그 외 컨텐츠 | 73 | — |

커밋으로도 교차 확인된다: `Tool_Animation` 파일별 커밋 1위(`Level_AnimTool.cpp`
jiwan 29 + jidungg 3 / seul 3 / smileJiro 2, 최초 커밋 `22f0770eb`도 본인),
`AnimEventGenerator`·`AnimEventReceiver`(jiwan 5 / seul 2), `2DModel`(jiwan 39),
`Animation2D`(jiwan 23), `Player.cpp`(239) · `Player.h`(134) · `PlayerSword.cpp`(54).
사운드도 본인 작업이지만 기술소개서에는 없다.

### 51. 상호작용 시스템 + 상호작용 오브젝트

- 출처: 기술소개서 1장(p.31), 2장(p.34) — **두 장을 연달아 배치했다.** 본인이
  이 프로젝트의 대표 작업으로 봤다는 뜻이다.
- 파일: `Portal`(+ `Portal_Default`, `Portal_Arrow`, `Portal_Cannon`,
  `PortalLocker`, `PortalLocker_LayerCount`), `CarriableObject`, `TiltSwapPusher`,
  `PlayerState_PickUpObject` / `LaydownObject` / `ThrowObject` / `Drag` / `Pull`,
  `PlayerState_IntoPortal` / `ExitPortal` / `StartPortal` / `CannonPortal`
- 근거: `d5c10ffd5`(플레이어 포탈 타기), `5e28b3e21`(플레이어 2D 물건 들기),
  `f854e0a76`(당근 들고 포탈 타기 버그 해결), "CannonPortal 인터렉션 UI 버그 수정.
  CHARGE_UP 추가", "대포포탈 제자리 쏘기 버그 해결", "플레이어 Draggable
  SceneQuery 켜주기"
- 기술소개서 슬라이드 31~35 내용:
  - `IInteractable`을 상속하고 순수 가상 함수를 오버라이드하면 상호작용 오브젝트가
    된다. 하위 클래스가 `m_eInteractType`과 `m_eInteractKey`를 설정해 키와 종류를
    정한다.
  - **대상 선택 3단계**(확인 필요였던 항목): ① 상호작용 범위 **트리거**에 감지됨
    → ② `Is_Interactable()`로 **객체 종속적 조건** 만족 → ③ 그중 **가장 가까운 것**.
  - 객체 종속 조건 예시: 들 수 있는 물체는 "이미 물건을 들었는지", 도시락은
    "트리거 안에 들어왔는지", 책은 "글러브를 보유 중인지".
  - **상호작용 타입 4종** — 노말(누르는 즉시), 차지(일정 시간 이상 눌렀을 때),
    차지 업(눌렀다 뗐을 때), 홀딩(누르는 동안 계속). **동작 차이를 `Interact`
    함수의 호출 타이밍과 횟수로만 만든다.** 물건 들기=노말, 포탈=차지,
    대포 포탈=차지 업, 물건 끌기=홀딩.
  - 포탈 3종(기본·대포·화살표)은 각각 차지 / 차지 업 / 충돌 즉시 발동이고,
    기본 포탈은 **Start → Into → Exit 3개 상태**를 거친다. Into 단계의 점프에
    **포물선 발사 함수**를 쓰는데, 원하는 각도로 목표에 도달 가능한지를
    bool로 반환한다.
  - 밀기·당기기(슬라이드 39)는 **충돌체를 3개로 나눈다** — 몸체 / 주변 확인용
    트리거 / **플레이어 탈부착용**(상호작용 중 플레이어 몸체와 같은 위치·모양으로
    물체에 붙었다가 종료 시 제거).
  - 물건 들기(슬라이드 38)는 **애니메이션 진행도에 따라 위치를 3단계로 보간**한다
    — 원래 위치 → 정렬된 위치 → 머리 위. 내려놓기는 역순. 2D는 중력을 직접
    구현하고 3D는 PhysX로 던진다.
- **하나의 인터페이스 + 4가지 입력 타입으로 이질적인 오브젝트를 전부 흡수한
  설계다.** OOP 우대 항목에 그대로 쓰인다.
- Shipgend 41번(상속 사슬)·Dogong 21번(컴포넌트+인터페이스)과 **같은 문제의 세
  번째 답**이다. 셋을 나란히 놓으면 "상호작용을 세 번 다르게 설계한 사람"이 된다.
- **이 시스템도 가이드 문서를 배포했다**(포트폴리오 슬라이드 11). 링크는 아직
  미확보. → 59번
- 확인 필요: 상호작용 타입을 4개로 나눈 기준, 가이드 문서 링크.

### 52. 3D 스켈레탈 애니메이션

- 출처: 기술소개서 3장(p.41)의 첫 항목
- 파일: `Engine/3DModel`, `Animation3D`, `Bone`, `Channel`, `Keyframe_Module`,
  `Controller_Model`, `Controller_Transform`
- 기술소개서 슬라이드 41~43 내용:
  - 요구사항 6개: 키프레임 기반 재생 / **역재생** / 재생 속도 조절 /
    **전환 시 두 애니메이션의 부드러운 보간** / 진행도 파악 / 진행도를 0~1로 계산.
  - `CAnimation3D`(채널 정보로 매 프레임 뼈 상태 갱신) → `CChannel`(뼈 하나의
    키프레임 목록) → `CBone`(부모 인덱스 + 변환 행렬) → `KEYFRAME`(재생 거리 +
    회전·위치·크기).
  - 키프레임 보간: 진행 시간으로 인접한 두 키프레임을 찾고 → 비율 계산 →
    위치·회전·크기를 각각 보간해 `KEYFRAME`을 만들고 → 4x4 행렬로 변환.
    뼈의 합성 변환 행렬은 루트부터 뻗어 나가며 부모 행렬 × 자기 행렬로 계산.
  - **애니메이션 전환이 이 항목의 핵심이다.** 전환이 걸리면 현재 상태를 `KEYFRAME`
    목록으로 **저장해두고**, 그걸 왼쪽 키프레임, 새 애니메이션의 첫 키프레임을
    오른쪽 키프레임으로 삼아 고정 딜레이 동안 보간한다.
- 39번(2D 스프라이트)과 **한 장 안에 나란히 놓인 대칭 항목이다.** 요구사항 목록이
  둘 다 거의 같다(역재생·속도·진행도 0~1) — **두 파이프라인을 같은 인터페이스로
  맞춰놓은 것**이 38번(이벤트가 2D·3D 모두에서 발생)의 전제다. 셋을 묶어 쓰는
  근거가 여기서 확인된다.
- ⚠ **작성자 확인 필요.** 39번(`2DModel` jiwan 39커밋)과 달리 `3DModel`·
  `Animation3D`의 작성자를 아직 확인하지 않았다. 기술소개서에 실려 있고 담당
  파트가 "애니메이션 & 플레이어"이므로 본인 작업일 가능성이 높지만, 팀
  프로젝트이므로 파일별 `git log --format="%an"`을 돌려 확인한 뒤 쓴다.

### 53. 플레이어 상태 머신 (36종) — 작성 완료

- 출처: 기술소개서 5장 "플레이어 상태"(p.50)
- 파일: `CPlayerState` 파생 클래스 **36개** — `Idle`, `Run`, `JumpUp`,
  `JumpDown`, `JumpAttack`, `Attack`, `SpinAttack`, `Roll`, `BackRoll`, `Clamber`,
  `Drag`, `Pull`, `PickUpObject`, `LaydownObject`, `ThrowObject`, `GetItem`,
  `Stamp`, `ThrowSword`, `RetriveSword`, `Evict`, `TurnBook`, `TransformIn`,
  `CyberIdle`, `Bomber`, `Electric`, `LunchBox`, `Mojam`, `ErasePalmDecal`,
  `Die`, 포탈 4종, 보스전 진입 등
- 근거: `b025e6877`(플레이어 점프 공격 처리), `78b5e7430`(2D 회전공격),
  `84303e733`(2D 플레이어 점프), "IsAnimTransition 추가",
  "Remove OnAnimEndCallback 추가", "플레이어 점프상태로 멈추는 현상 완화"
- 구조(기술소개서 슬라이드 50~51): `CStateMachine`이 컴포넌트로 플레이어에 붙고,
  현재 상태에 해당하는 `CPlayerState` 객체를 돌린다. 각 상태는 `Start()` /
  `Update()` / `Exit()` / `On_AnimEnd()`를 오버라이드한다. **`설계 이유`가 네 개
  적혀 있다** — 각 상태 동작 모듈화, 코드 확장성(상속 후 추가만 하면 됨), 현재
  상태를 일관되게 관리, **플레이어와 상태 로직 분리(CPlayer가 깔끔하게 유지됨)**.

- ★ **슬라이드 52가 통째로 `문제점` 페이지다. 문제 4건 각각에 상황 예시와 개선
  방향이 붙어 있다. 이 문서 전체에서 회고 재료가 가장 좋은 항목이다.**

  1. **상태 간 공유 데이터 관리** — 상태가 전이되면 이전 상태 객체가 삭제되면서
     정보도 사라진다. 이를 유지하려고 플레이어 객체에 저장했더니 **`CPlayer`에
     getter·setter가 늘어 인터페이스가 지저분해졌다.**
     예: JumpDown → Clamber 전이 시 벽의 높이·방향을 넘기려고
     `Get_ClamberEndPosition()` 같은 함수가 추가됨.
     → 개선 방향: 공유 데이터를 관리하는 별도 클래스.
  2. **상태 구분 기준의 모호함** — 복합 상태를 어떻게 정의할지 기준이 없어서
     전이 조건이 불명확해지고 일부는 분기문에 의존하거나 중복 구현됐다.
     예: '점프 공격'을 *"JUMP 상태 중 공격 입력"*으로 볼지 *"ATTACK 상태에서
     점프 중인지 분기"*로 볼지 기준이 없었다.
     → 개선 방향: **'행동의 의도'와 '물리적 상태' 중 하나를 기준으로 정하고
     문서화**, 각 상태의 진입·탈출·유지 조건 명문화.
  3. **전이 로직이 각 상태 클래스에 분산됨** — 각 상태가 직접 다음 상태를
     판단해서 상태 간 결합도가 오르고 전체 흐름을 한눈에 보기 어려워졌다.
     → 개선 방향: 전이 조건을 상태 밖에서 관리. **상태는 "탈출 조건"만 판단하고
     "다음 상태"는 외부가 결정.** 슬라이드에 개선 코드 예시(전이의 클래스화)도 있다.
  4. **너무 많은 상태 클래스** — 기간이 지나며 수가 지나치게 늘고 일부는 중복
     구현됐다. 예: 점프에 JumpUp·JumpDown·JumpAttack 3개, 포탈에 Start·Into·Exit 3개.
     → 개선 방향: 포함 관계를 파악해 **MainState + SubState 구조** 또는 계층적
     상태 구조 도입.

- **35개는 관리 방식을 설명해야 하는 규모고, 본인이 그 대가를 이미 네 항목으로
  정리해뒀다.** 사례의 `장단점`·`회고`가 사실상 완성돼 있다.
- 38번(애니메이션 이벤트)·24번(이동 예외)과 직접 맞물린다 — 상태 전이가
  애니메이션 종료 콜백과 엮이면서 "점프 상태로 멈추는 현상" 같은 버그가 나왔다.
- Shipgend 46번, CopyMaple2 `MonsterAnimStateMachine`, 55번(보스 FSM 16종)까지
  합치면 **상태 머신을 네 번 짰다.** 그중 이 항목만 회고가 문서화돼 있다.
- **`Cases/player-state-machine.md`로 작성됨 (2026-08-27).** 코드에서 추가로 확인된 것:
  팀원(`smileJiro`)이 개발 막바지에 `BackRoll`·`Pull`(2025-03-17)·`Mojam`(2025-03-15)
  세 상태를 직접 추가했다(확장성 근거) / `CPlayer` 헤더의 `Get_`·`Set_`·`Is_` 접근자가
  80개를 넘는다 / `CTransition`·`Condition`이 `30525fcf2`(2025-01-17)에 구현돼 있으나
  **어디서도 생성되지 않는다.**
- ★ **`CTransition`·`Condition`의 출처가 밝혀졌다 (사용자 확인, 2026-08-27).**
  **CopyMaple2에서 실제로 쓰던 방식이다.** `CopyMaple2/Engine/Public/`의
  `StateMachine.h`·`Transition.h`·`Condition.h`가 그것이고, PluckySquire의
  `Client/Public/Transition.h`는 네임스페이스·DLL 매크로만 다른 **거의 동일한 복사본**이다.
  - CopyMaple2 쪽은 진짜로 쓰인다 — `Player`·`Monster`·`NPC`·`Bayar`·`Character`·
    `MonsterAnimStateMachine`이 사용. `Add_ConditionVariable(id, bool*/int*/float*)`로
    조건 변수 주소를 등록하고 `Add_Transition` + `Bind_Condition`으로 전이 규칙을
    선언적으로 쌓는 **유니티 애니메이터식** 구조다.
  - 사용자 진술: PluckySquire에서 *"그대로 할까 하다가 지난 프로젝트 할 때 디버깅이
    너무 힘들었던 기억이 있어서 다른 방식으로"* 했고, 하다 보니 *"MapleStory2 방식의
    장점만 가져오면 좋겠다"* 고 생각해서 옮겨 왔지만 **"그냥 하려다가 말았다."**
  - → **53번의 '대안 비교'가 상상이 아니라 두 프로젝트에 걸친 실제 경험이 됐다.**
    `Cases/player-state-machine.md`에 반영 완료(2026-08-27).
  - **디버깅이 어려웠던 이유 (사용자 확인, 2026-08-27) — 채워졌다.** 전이가 잘 되는지
    보려면 `CState::Check_Transition()` / `CState::Check_SubTransition()` /
    `CTransition::CheckConditions()`에 중단점을 걸어야 하는데, 이 함수들이
    **상태 머신을 쓰는 모든 객체의 Update마다** 불려서 *"내가 원하는 객체, 원하는
    타이밍을 포착해내기가 힘들었"*다. (세 함수명 모두 CopyMaple2 코드에서 확인.
    `CStateMachine::Late_Update`에서 호출된다.)
  - 동기의 정확한 순서(사용자 확인): Maple2 디버깅이 힘들었으니 **이번엔 더 단순한
    구조로 가자** → PluckySquire 진행 중 **클래스가 너무 많아져서** 결국 있으면
    좋겠다는 생각이 됐다. (전이 흐름 가시성이 아니라 **클래스 수**가 방아쇠였다.)
- ★★ **CopyMaple2의 `CStateMachine`에는 이미 MainState + SubState가 있다.**
  `m_iCurrentState`와 `m_iCurrentSubState`를 함께 들고,
  `Add_SubTransition()` · `Set_CurrentState(iMainState, iSubState)` ·
  `Register_OnSubStateChangeCallBack()`이 있다. `Initialize_Prototype(jsonFilePath)`로
  **상태 머신 정의를 json에서 읽는 경로**도 있다.
  - 즉 슬라이드 52 문제 4의 개선 방향 "MainState + SubState 구조 도입"은 새로 떠올린
    아이디어가 아니라 **직전 프로젝트에서 이미 만들어 쓰던 구조**다.
  - ⚠ **아직 사례에 쓰지 않았다.** 코드 사실은 확정이지만, 사용자가 그 개선 방향을
    적을 때 *앞 프로젝트 구조를 염두에 뒀는지*는 본인만 안다. **물어본 뒤에 쓴다.**
    (53-A에서 코드 모양만 보고 의도를 넘겨짚었다가 틀린 전례가 바로 위에 있다.)
- 사용자 확인(2026-08-27): 계층 구조는 **설계 시점의 후보가 아니었다.** 상태가 늘어난
  뒤에야 필요를 느꼈고, "PPT에 있는 내용 그대로"다. 사례에 그렇게 반영했다.
- ⚠ **개선 방향 4개 중 실제로 적용해본 것은 없다** (사용자 확인, 2026-08-26).
  → **"이렇게 개선했습니다"로 쓰면 안 된다.** 사실은 "진단까지 했다"이고,
  그 선에서 닫아야 한다. 이 항목이 1순위가 아니라 2순위인 이유이기도 하다.
- ~~Dogong에서 이 진단이 이어졌는지~~ — **아니다. 확인 결과 연결이 성립하지 않는다.**
  `a55ad484`(bool 3종→enum)는 *과분할*이 아니라 *미분할*을 고친 것이라 방향이 반대고,
  `0985b4a4`는 커밋에 동기가 "단일 스냅샷 복제"로 적혀 있어 네트워크 사유이며,
  GAS 채택은 UE 표준 선택이라 근거가 못 된다. **Dogong의 콤보 어빌리티는 애초에
  본인 작업이 아니다**(사용자 확인). 이 방향으로는 쓰지 않는다.

### 53-A. RTChess 연결 — 성립하지 않는다 (2026-08-27 확인)

**한때 "53번을 '진단까지 했다'로 닫지 않아도 되는 근거"로 적어뒀던 항목이다.
사용자 확인 결과 오독이었다. 이 방향으로는 쓰지 않는다.**

- 조사자가 이렇게 읽었었다: RTChess의 `EPieceAnimState { Idle, Moving, Dead }`(베이스
  컴포넌트)와 `EJumpPhase { None, Ready, Up, Down, Recover }`(나이트 파생 컴포넌트)가
  한 대상의 상위·하위 상태 축이므로, 슬라이드 52 문제 4의 개선 방향인
  "MainState + SubState 구조"가 실제로 적용된 것이다.
- **사용자 확인 (2026-08-27) — 둘은 같은 것의 두 축이 아니다.**
  - `EJumpPhase`는 **점프하는 방식으로 이동하는 기물의 이동 과정 단계**를 구분한다.
    애니메이션 상태와는 별개다.
  - `EPieceAnimState`는 **현재 기물의 애니메이션 상태**이고, 어떻게 보면 **기물에
    사용되는 텍스처의 종류**다. 만들어진 이유 자체가 *애니메이션 종류에 따라 사용되는
    텍스처가 달랐기 때문*이다.
- 코드도 사용자 설명 쪽이다. `UPieceTextueringComponent`가
  `TMap<EPieceAnimState, TObjectPtr<UTexture2D>> BaseTextureMap`을 들고
  `BindOnAnimStateChanged`로 상태 변경을 받아 `SetTextureParameterValue(TEXT("Base"), ...)`
  로 텍스처를 교체한다. **`EPieceAnimState`는 텍스처 선택 키다.**
- 따라서 **베이스/파생 컴포넌트 분리는 상태 계층 설계가 아니라 관심사가 다른 두
  기능(텍스처 교체 / 이동 단계)의 분리다.** 53번의 개선 방향과 연결되지 않는다.

**결론: 53번은 "문제를 진단하고 개선 방향까지 정리했다"까지가 사실이고, 그 선에서
닫는다.** `Cases/player-state-machine.md`도 그렇게 썼다(회고에서 RTChess 문단 제거,
2026-08-27).

⚠ **교훈 — 코드 모양이 비슷하다고 의도가 같지 않다.** 베이스/파생 + 두 개의 enum이라는
형태만 보고 "MainState + SubState"로 읽었는데, 실제로는 텍스처와 이동이었다.
[[fact-vs-authored-judgment]]의 전형적인 사례다.

### 53-B. RTChess 사례를 쓸 때 쓸 수 있는 재료 (별개 항목)

위 확인 과정에서 **사용자 본인의 판단**이 하나 나왔다. RTChess 사례를 쓰게 되면 쓴다.

- 사용자 진술(2026-08-27): *"지금 생각해 보니 enum 이름을 애니메이션 상태보다 텍스처
  종류를 강조해야 했나 싶기도 하네."*
- 즉 `EPieceAnimState`라는 이름이 실제 역할(텍스처 선택)보다 애니메이션 쪽을 강조한다는
  자가 피드백이다. **이름 짓기 / 관심사 명명에 대한 회고 재료**이고, JD가 "읽기 쉬운
  코드"를 우대할 때 쓸 수 있다.
- 관련 파일: `Components/PieceTextueringComponent`(텍스처 교체),
  `Components/PieceAnimationControlComponent`(상태 보유·복제),
  `Data/CommonDataHeader.h`(enum 정의).

### 54. 플레이어 장비 5종 — 검 · 도장 · 라이플 · 제트팩 · 건틀릿

- 출처: 기술소개서 7장(p.55~64) — **10쪽을 할애했다. 단일 장 중 가장 길다.**
- 파일: `PlayerSword`, `EvictedSword`, `PlayerRifle`, `BombStamp`, `StopStamp`,
  `ArrowForStamp`, `StampKey_1`, `BombStamp_UI`, `StopStamp_UI`,
  `PlayerState_Stamp` / `ThrowSword` / `RetriveSword`
- 근거: `PlayerSword.cpp` 54커밋(본인 파일 상위권), "플레이어 칼 이펙트 처음에
  끄기", "Carry 상태일 때 칼 숨기는 코드 삭제", `4670372d5`(ErasePalm 추가)
- **장비 5종이 각각 다른 조작 규칙을 갖는다.** 검은 던지고 회수하고, 도장은
  월드에 도장을 찍어 오브젝트를 만들거나 멈추며(`BombStamp`/`StopStamp` + 전용
  UI), 제트팩·건틀릿은 이동 규칙 자체를 바꾼다. **하나의 캐릭터에 이질적인
  능력 5개를 붙이는 설계 문제**다.
- 기술소개서 슬라이드 55~64가 답한 것(전부 `확인 필요`였던 항목):
  - 장비는 **`CPartObject` 파생**이다. 컨테이너(플레이어)의 **특정 뼈 또는 중심점에
    부착**된다. 상태가 아니라 오브젝트로 풀었다.
  - **주 장비 / 보조 장비 개념을 별도 클래스 없이 "포함 관계를 갖는 열거체"로
    구현했다.** `PLAYER_PART` ⊃ `PLAYER_MAIN_EQUIP` / `PLAYER_SUB_EQUIP`.
    주 장비는 한 번에 하나(검·라이플), 보조는 여러 개 동시 착용 가능(제트팩·
    바이저·기폭장치·도장 2종). 주 장비를 장착하면 다른 주 장비가 자동 해제된다.
    **"동시 착용 가능 관계"라는 요구를 enum 포함 관계 하나로 처리한 게 이 항목의
    설계 포인트다.**
  - **검** — 공격 트리거를 **애니메이션 이벤트로 켜고 끈다**(38번). 일반 공격·점프
    공격·투척용 트리거가 각각 따로 있다. 트리거가 검을 따라 움직여 타이밍이
    현실적이다. **중복 타격은 이미 때린 대상을 `set`에 넣어 막는다.**
    투척은 `HANDLING → OUTING → RETRIEVING → STUCK` 4상태로 돌아간다.
  - **도장** — `IStoppable`·`IBombable`을 **믹스인 인터페이스**로 두고 구현을
    하위에 위임한다. 멈춰 도장은 `CPalmDecal`(손바닥 자국)을 남기고, 자국과 충돌한
    대상의 `Stop()`이 호출된다. 자국 자체가 상호작용 오브젝트라 지우면 `UnStop()`.
    `CCharacter`는 **부모 `Update`를 호출하지 않는 방식으로** 멈춤을 구현했다.
    폭탄 도장은 지점에 설치 가능한 물체가 있으면 물체에, 없으면 지면에 폭탄을
    만들고 기폭 장치와 연결한다.
  - **라이플** — `Shoot(타겟)` 한 줄로 쓰게 만들었고, `m_fShootDelay`·
    `m_vBarrelOffset`으로 연사 속도와 총구를 조절한다. **총알은 오브젝트 풀링.**
  - **제트팩** — 연료 잔량에 따라 추진력이 달라진다. 공식이 명시돼 있다:
    `상승 힘 = 추진력 × 배율`, `배율 = 최소 + (최대-최소) × (현재연료-최소추진연료)
    / 최대연료`. 바닥에 닿으면 `ReFuel()`. **"원작과 흡사한 조작감"이 목표라고
    적혀 있다** — 수치를 공식으로 만든 이유가 여기 있다.
  - **건틀릿** — 넘기기·기울이기 두 종류이며, 책과의 상호작용에 필수다. 책은
    `BOOK_STATE` 7종(IDLE / CLOSED_LEFT / TURN_LEFT / TURN_RIGHT / TILT_LToR /
    TILT_RToL / OPEN_BOOK)을 갖고 **플레이어 상태와 복합 전환**된다.
- 53번(상태 머신)이 이걸 감당하느라 커진 것으로 보인다. 묶어 쓰면 인과가 선다 —
  특히 53번 문제점 4번(상태 클래스가 너무 많음)의 직접 원인이다.
- **38번(애니메이션 이벤트) 없이는 검이 성립하지 않는다.** 툴 → 이벤트 → 장비로
  이어지는 세 항목이 한 줄기이므로, 이 순서로 배치하면 서로를 설명해준다.
- 확인 필요: 제트팩 공식의 계수를 어떻게 정했는지(감? 원작 관찰?).

### 55. 플레이어 모드 — 플랫포머 / 보스전 (보스 FSM 16종)

- 출처: 기술소개서 8장(p.65~67)
- 파일: `FSM_Boss`, `BossState` + 상태 16종(`BossIdleState`, `BossMoveState`,
  `BossHitState`, `BossShieldState`, `BossDeadState`, `BossTransitionState`,
  `BossSceneState`, `BossWingSlamState`, `BossWingSliceState`,
  `BossRockVolleyState`, `BossEnergyBallState`, `BossHomingBallState`,
  `BossPurpleBallState`, `BossYellowBallState` 등), 투사체
  `Boss_EnergyBall` / `HomingBall` / `PurpleBall` / `YellowBall` / `Rock` /
  `TennisBall` / `WingSlam` / `WingSlice` / `Crystal`, `BossHP`, `BossHPBar`,
  `PlayerState_EngageBoss`
- 근거: `ed70b4e8b`(플레이어 3D 싸이버조트), "플레이어 보스전 커서 이동",
  보스 인트로·컷씬 사운드 타이밍 커밋들
- **같은 캐릭터가 모드에 따라 완전히 다른 규칙으로 움직여야 하는 문제.**
  플랫포머 모드와 보스전 모드에서 이동·카메라·입력이 달라진다("8챕터에서만
  카메라 방향 기준 이동" 커밋이 이 계열).
- 기술소개서 슬라이드 65~67 내용:
  - **모드는 4종이다** — SWORD(기본) / SNEAK(잠입: 무기 미장착, LShift가 구르기
    대신 잠입, 이동 느려지고 발소리 없음) / ZETPACK / CYBERJOT(보스전: 라이플 +
    제트팩 + 바이저 + 조준점). 전환 함수가 장비 장착과 Actor 상태 변경 등
    사전 작업을 수행한다.
  - **플랫포머는 위 4모드와 직교하는 별도 축이다.** "SWORD 모드 + 플랫포머 모드"가
    성립한다. 차이가 표로 정리돼 있다 — 이동(WASD 평면 ↔ AD 좌우), 중력(가상 Z축
    ↔ Y축), 점프 축, 공격(8방향 자동 추적 ↔ 좌우 2방향 + 적 밟기).
  - **보스전 구도**: 카메라는 고정이고 보스와 플레이어의 중간을 본다. 플레이어는
    카메라에서 일정 거리의 **평면 위에서만** 움직이고, 조준점도 별도 평면 위에서
    움직인다. 총알은 항상 조준점을 향한다.
- **"같은 캐릭터를 네 가지 규칙으로 굴린다"에 더해, 플랫포머라는 직교 축이 하나 더
  있다.** 모드 조합이 곱셈으로 늘어나는 구조를 어떻게 관리했는지가 사례의 핵심이다.
- 보스는 **패턴 9종 + 상태 16종의 별도 FSM**이다. 53번(플레이어 상태)과 짝을
  이루는 두 번째 상태 머신이라, 둘을 비교하면 "상태 머신을 두 번 다르게 짠"
  이야기가 된다.
- 확인 필요: 보스 패턴 선택 로직(랜덤? 페이즈? 체력 구간?), 모드 × 플랫포머
  조합이 늘어나며 겪은 문제.

### 56. Defender 미니게임

- 출처: 기술소개서 9장(p.68~69)
- 파일: `Minigame_Defender`, `DefenderPlayer`, `DefenderPlayerProjectile`,
  `DefenderMonster`, `Defender_Monster`, `DefenderSpawner`, `DefenderCapsule`,
  `DefenderSmShip`, `DefenderMedShip`, `DefenderPerson`
- 근거: `ec67fd6cc`(DefenderPlayer, Projectile 추가), "Defender 효과음",
  "Defender 디버그 키 제거"
- **본편 안에 들어가는 별도 규칙의 작은 게임을 혼자 통째로 만든 사례.** 스포너·
  적 2종·구조 대상(Person/Capsule)·투사체까지 갖춘 완결된 루프다.
- 기술소개서 슬라이드 68~69 내용:
  - **2D 횡스크롤 탄막 슈팅**이고, 목표는 적을 물리치며 **박사 9명 구조**.
  - 요구사항 8개 중 눈에 띄는 것: **스테이지가 좌우 순환형**(왼쪽 끝과 오른쪽 끝이
    연결), 몬스터 3종 이상 무한 반복 등장, 몬스터는 체력 0 또는 **수명 만료**로
    사라짐, 일정 시간마다 파괴 시 박사를 생성하는 Capsule 등장.
  - **`CDefenderSpawner`가 `SPAWN_DESC` 목록으로 자동 생성한다.** 구조체에 생성
    패턴·소환 횟수·생성 딜레이·위치·자동 생성 여부가 들어간다.
    **패턴 5종**: DOT(단일 지점) / ARROW(화살표 모양) / VERTICAL_UP /
    VERTICAL_DOWN / RANDOM.
  - `CDefenderPlayer`는 **`CPlayer`와 구분되는 별도 클래스**라고 명시돼 있다.
- **확인 필요였던 "본편을 재사용했는가"의 답: 플레이어·몬스터는 따로 짰다.**
  그러면 사례의 초점은 "왜 새로 짰는가"와 스포너 데이터 설계로 옮겨간다.
  `SPAWN_DESC`로 소환 패턴을 데이터화한 것이 이 항목에서 가장 설명할 만하다.
- 확인 필요: 본편 플레이어를 재사용하지 않은 이유(조작 규칙이 달라서? 시간?).

### 37. 애니메이션 툴 (Tool_Animation)

- 근거: `22f0770eb`(Feat : 모델 출력 — 이 툴 프로젝트의 첫 커밋), `80ee50de4`(애님툴
  줌 기능), `8f44ae7d9`(카메라 줌 기능 로직 변경), `2a08625dd`(애니메이션 툴 배경
  출력), `116f5e6b4`(텍스처 이름 겹치는 문제 해결), `fede12fd3`(안 보이는 버그 수정),
  `3767e6bab`(카메라 빌드에러 해결), `267fbb40b`(imgui debug lib 경로 추가),
  `4acf16493`(애니메이션 이름 출력), `c16d764ca`(애니메이션 마지막 프레임도 정상
  출력하게 변경), `0ad346ea3`(Convert SingleSprite2DModel 기능 추가),
  `5ecae26fb`(애니메이션 루프 & 속도 배율 정보 추가 바이너리화),
  `2b8e17720`(2DModel Binarize), `1327631bb`(애니메이션 이벤트 기능)
- 파일: `Tool_Animation/`(별도 vcxproj — `AnimTool_MainApp`, `Level_AnimTool`,
  `AnimTool_Function`, `AnimTool_Enum`), ImGui 기반
- **`툴 제작 및 자동화`를 요구하는 JD에서 가장 강한 카드다.** 본인이 만들기 시작해
  기능을 계속 얹었고, 팀원들이 쓴 흔적(다른 사람 커밋)도 남아 있다 — **"내가 만든
  툴을 팀이 썼다"가 커밋으로 증명되는 유일한 사례.**
- `c16d764ca`(마지막 프레임 미출력), `116f5e6b4`(텍스처 이름 충돌),
  `fede12fd3`(출력 안 됨)은 툴을 쓰다 나온 버그 수정이라 디버깅 소재도 겸한다.
- **기술소개서 슬라이드 70~72에 목적·기능·장점이 정리돼 있다.**
  - 본인 규정: *"클라이언트 개발 중 사용되는 모델 및 애니메이션 데이터를 시각적으로
    확인하고, 애니메이션 동작을 검토하며 이벤트 데이터를 편집·저장할 수 있도록
    지원하는 제작 보조용 툴."*
  - 기능 9개: `.model`/`.model2d` 로드·저장, **Raw 2D 모델 데이터(json 묶음)에서
    `.model2d` 생성**, 2D·3D 애니메이션 재생, 카메라 줌, 애니메이션 전환, 재생
    속도·반복 설정, `.animevt` 생성·수정, 논애님 스프라이트 모델 일괄 변환.
  - 장점 3가지를 본인이 표로 적었다: 시각적 피드백(실시간 확인) / 직관적 이벤트
    조정(타이밍을 정확히 지정) / **경량·도구화(게임 엔진·클라이언트와 무관하게
    리소스를 사전 검수)**.
  - 슬라이드 72는 **"프로젝트 진행 중 애니메이션 툴 사용법에 대한 가이드를 작성해
    팀원들과 공유했습니다"** 한 줄과 가이드 캡처다. → 59번
- **가이드 문서 실물이 있다** → [`Sources/Portfolios.md`](../Sources/Portfolios.md)의
  "애니메이션 툴 가이드". 기능 목록 → 화면 → 사용 방법 순으로 쓰였고, 폴더 구조
  제약 같은 **주의 사항이 번호로 붙어 있으며 버전 표기("2.09 추가됨")까지 있다.**
  가이드에는 **FModel로 원작 2D 리소스를 추출해 들여오는 절차**도 들어 있는데,
  이건 기술소개서에 없는 내용이다(39번과 연결).
- 확인 필요: 툴이 없을 때 팀이 어떻게 작업하고 있었는지, 무엇이 불편해서 만들었는지.
  **기술소개서에도 이 답은 없다. 물어봐야 한다.**

### 38. 애니메이션 이벤트 시스템

- 근거: `1327631bb`(Feat : 애니메이션 툴 애니메이션 이벤트 기능),
  `2b62c2cb4`(애니메이션 반복돼도 애님이벤트 호출되게 변경),
  `d8cddcbab`(애니메이션 이벤트 역재생 시에도 정상 작동하게 수정),
  `07c5894f0`(책 이동 시 플레이어도 이동하게 책 애니메이션 이벤트 추가, 트리거
  구조), `4aca91acc`(Slippery를 Stop)
- 파일: `Engine/Public/AnimEventGenerator.h`, `AnimEventReceiver.h`
- 구현에서 확인되는 것:
  - `ANIM_EVENT` 구조체가 `iAnimIndex` / `strFuncName` / `fProgress` /
    `bIsTriggered`를 갖고, **자기 자신을 읽고 쓰는 `WriteFile`·`ReadFile`을 직접
    갖고 있다.** 툴에서 찍은 이벤트가 바이너리로 저장되고 런타임이 그대로 읽는다.
  - `CAnimEventGenerator`는 `CComponent` 파생. `map<애님인덱스, vector<이벤트>>`로
    들고 있다가 진행도(`fProgress`)로 발동시킨다. `Reset()`이 `bIsTriggered`를
    전부 내린다 — `2b62c2cb4`(반복 재생 대응)의 실체.
  - `IAnimEventReceiver`는 `map<string, function<void()>>`에 함수를 이름으로
    바인딩하고 `Invoke(이름)`으로 부른다. **툴이 아는 건 문자열뿐이고, 무엇을
    실행할지는 받는 쪽이 정한다** — 툴과 게임 로직을 문자열 하나로 끊어놓은 설계.
  - `Export_AnimEvents`는 `#ifdef _TOOL`로 감싸 툴 빌드에만 들어간다.
- **툴 → 데이터 → 런타임 파이프라인 전체를 한 사람이 설계한 사례다.** 인터페이스
  분리(OOP), 직렬화, 툴 제작이 한 덩어리로 묶여서 이 목록에서 밀도가 가장 높다.
- `d8cddcbab`(역재생)과 `2b62c2cb4`(반복 재생)는 **진행도 기준 발동이 만든 구멍
  두 개를 각각 메운 수정**이다. 장단점 섹션의 '단점'이 이미 커밋으로 나와 있다.
- **`설계 이유`가 기술소개서 슬라이드 48에 통째로 있다 — 이벤트 데이터를 모델
  파일이 아니라 별도 파일(`.animevt`)로 뺀 이유 4가지:**
  1. 모델 파일을 쓰던 **다른 프로젝트의 모델 로드 코드 수정을 줄이기 위해**
  2. 다른 모델이라도 같은 이벤트 파일을 쓸 수 있고, 같은 모델에 여러 이벤트
     파일을 쓸 수 있음
  3. **모델 클래스(파일)의 응집도를 높이고 복잡도를 낮추기 위해**
  4. 이벤트 수정 시 모델 파일을 다시 열거나 고칠 필요가 없어 **작업 범위 최소화**
  → 제가 물어보려던 질문의 답이 전부 여기 있다. **"파일을 왜 나눴는가"에 대해
  응집도·재사용·작업 범위를 근거로 든 답변이라, OOP 우대 항목에 그대로 쓰인다.**
- 요구사항(슬라이드 46)은 **2D와 3D 애니메이션 모두에서 이벤트가 발생해야 함**을
  포함한다. 39번(2D)·52번(3D)을 공통 인터페이스로 묶은 것이 전제다.
- 실제 사용 예 3개가 적혀 있다(슬라이드 47): 검 휘두르기 모션 → 공격 충돌체 활성화,
  도장 찍기 모션 → 도장 효과 발동, 검 던지기 모션 → 검 발사. **54번(장비)이 전부
  이 시스템 위에 올라가 있다.**
- **가이드 문서 실물이 있다** → `Sources/Portfolios.md`의 "애니메이션 이벤트 가이드".
  팀원이 따라 할 수 있게 4단계 + 예시 코드로 쓰였고, `std::bind`가 처음인 팀원을
  위한 설명까지 들어 있다. → 59번
- 확인 필요: 문자열 키 방식의 대가(오타를 런타임까지 못 잡음)를 어떻게 봤는지,
  대안(enum·인덱스)을 고려했는지. **이건 기술소개서에도 없다.**

### 39. 2D 스프라이트 모델·애니메이션 파이프라인

- 근거: `2b8e17720`(2DModel Binarize), `0ad346ea3`(Convert SingleSprite2DModel),
  `5ecae26fb`(애니메이션 루프 & 속도 배율 정보 추가 바이너리화),
  `f0efd6abc`(2D 모델 텍스처 DDS로 변경), `c56385899`(2D모델 텍스처 프로토타입 우선
  로드), `d433cdcd5`(2DModel 로드 정상화), `dbf125fec`(2챕터·4챕터 2D 로드 분리),
  `678f57588`(SPRITE_ANIM 패스 이름 SPRITE2D로 변경)
- 파일: `Engine/2DModel`, `Animation2D`, `Transform_2D`, `SpriteEffect_Emitter`
- 원작이 책 안(2D)/밖(3D)을 오가는 게임이라 3D 모델 파이프라인과 별개로 2D
  스프라이트 파이프라인이 필요했다. 37번(툴)·25번(2D↔3D 상태)과 한 줄기다.
- **37·38·39를 하나로 묶어 "2D 애니메이션 파이프라인을 툴부터 런타임까지 만들었다"로
  쓰는 게 가장 강하다.** 나눠 쓰면 각각은 얇아진다.
- 확인 필요: DDS로 바꾼 이유(용량? 로딩?), 텍스처 프로토타입 우선 로드가 무슨
  문제를 푼 건지.

### 24. 플레이어 이동 예외 처리 다발 — 이동 보조 · 벽 타기

- 출처: 기술소개서 4장 "캐릭터 이동 보조"(p.49), 6장 "벽 타기"(p.52).
  **기술소개서는 이 둘을 별도 장으로 나눴다.** 커밋만 보고 "자잘한 버그 수정
  다발"로 묶었던 것이 잘못된 판단이었다 — 본인은 각각을 독립된 기능으로 본다.
  사례로 쓸 때 이 구분을 따른다.
- 파일: `PlayerState_Clamber`(벽 타기)
- 근거: `a19e08ab9`(캐릭터 StepAssist 리팩토링), `0a4c81cfa`(벽타기 코드 리팩토링),
  "플레이어 턱에 걸리는 현상 & 미끄럼틀 올라가기", "플레이어 점프상태로 멈추는 현상
  완화", "플레이어 쫒겨나는 방향 잘못된 버그 수정", "Draggable 떨어지면 터지는 현상
  수정", "포탈 홈런버그 수정", "당근 들고 포탈 타기 버그 해결",
  "플레이어 Draggable SceneQuery 켜주기"
- 기술소개서 슬라이드 49·53·54 내용:
  - **캐릭터 이동 보조(StepAssist)** — 요구사항은 "작은 턱과 충돌해도 별도 조작
    없이 부드럽게 넘어야 하고, **넘을 수 있는 높이와 경사도를 설정할 수 있어야**
    한다". 동작은 현재 Velocity로 다음 프레임 이동량을 **예측** → 넘을 수 있는
    턱과 충돌이 예상되면 → **Y축 속력을 추가**한다.
  - **벽 타기 조건** — Raycast로 **팔 길이 내**에 벽을 감지하고, Overlap으로 벽
    위에 충분한 공간이 있는지 확인한다. 핵심 판정은
    **"이전 프레임에는 벽이 팔보다 낮았고 현재 프레임에는 팔보다 높아졌는가"**다.
    조건을 이렇게 좁힌 이유가 적혀 있다 — *예기치 않은 동작이나 버그를 방지하고,
    조작의 직관성과 몰입도를 높이기 위해서.*
  - **벽 타기 동작** — 감지 지점을 끝 위치로 저장 → Look 방향 Raycast로 벽 법선을
    얻고 → 끝 위치·법선·팔 길이·팔 높이로 시작 위치를 역산 → 시작 위치로 이동시킨 뒤
    **애니메이션 재생도에 따라 시작→끝을 보간**한다.
- **두 기능 모두 "예측"과 "보간"으로 풀었다**는 공통점이 있다. 묶어 쓰면
  "물리 시뮬레이션에 맡기지 않고 연출을 직접 통제한 이유"가 주제가 된다.
- 물리 기반 캐릭터 컨트롤러의 코너 케이스 모음이기도 하다. 개별 버그 커밋들은
  **묶으면 "캐릭터 이동을 안정화한 과정"** 하나가 된다.
- CopyMaple2 57번(자체 구현 블로킹)과 대비된다 — 같은 문제를 PhysX 위에서 다시 푼
  버전이다.
- 확인 필요: 개별 버그의 원인. 커밋 메시지로는 증상만 알 수 있고 기술소개서에도
  버그 이야기는 없다.

### 25. 2D↔3D 전환 플레이어 상태 구현

- 근거: "플레이어 2D 아이템 얻기 상태 구현", "2D 스핀어택 구현",
  `PlayerState_ExitPortal.cpp`, `Animation2D.h/cpp`, `2DModel.h/cpp`,
  `PlayerState_Run/Idle/Attack/JumpDown.cpp`
- 원작의 핵심 기믹이 책 안(2D)↔밖(3D) 전환이다. 같은 캐릭터를 두 표현으로 다루는
  상태 설계 이야기.
- 확인 필요: 상태를 어떻게 나눴는지, 2D/3D에서 무엇을 공유하고 무엇을 분리했는지.

### 그 밖에

- "8챕터에서만 카메라 방향 기준 이동", "플레이어 카메라 보는 방향에 따라 이동방향
  달라지기" — 카메라 상대 이동
- `Minigame_Defender.cpp` — 미니게임 단독 구현
- "책 넘기는 소리 한 번만 들리게 수정", 보스 인트로·컷씬 사운드 타이밍 — 사운드 담당분
- "스킬 레벨에 따른 스킬 동작 구현", "CyberCursor 구현"

---

## Shipgend (Ship of Fools 모작, DirectX9 자체 엔진, 5인 팀 ⚠, 2024-09)

**이 저장소에서 소재가 가장 잘 정리된 프로젝트다.** 사용자가 프로젝트 종료 직후
블로그에 15편짜리 구조 설명 + 자가 피드백 시리즈를 썼다.
→ [`Sources/Portfolios.md`](../Sources/Portfolios.md)의 "Ship of fools 모작" 항목

- 개발 기간 4주, 5인, DirectX9 / C++ / VS2022
- **본인 역할: 팀장, 메인 프레임워크 담당** (개요 글에 명시)
- 본인이 만든 부분(개요 글에 나열): 씬·컴포넌트 구조, Transform, 배, 상호작용
  시스템, 항해 시스템, 충돌 처리 시스템, 애니메이션 시스템, 이벤트 시스템,
  UI 매니저, 아이템 시스템, 멀티 쓰레드 로딩 시스템, 강화 섬
- 기여 규모: 539커밋으로 1위. PR 기반 협업(#193, #194 확인)
- 결과물 영상: 개요 글에 유튜브 링크 있음

**다른 프로젝트와 달리 `확인 필요`가 거의 없다.** 판단·대안 검토·회고가 글에 다
적혀 있고, 그건 사용자 본인이 쓴 문장이므로 그대로 근거로 쓸 수 있다.

**단, 편집이 필요하다.** 아래 항목 중 여럿(46·40·42)이 **팀원과 의견이 갈려
본인 뜻대로 못 한 이야기**다. 블로그에선 솔직한 회고지만 포트폴리오에 그대로
옮기면 "설득하지 못한 사람"으로 읽힌다. 사례로 옮길 때 결론을 본인 판단 쪽으로
돌리거나, 트레이드오프를 이해한 근거로 쓴다.

### 46. 엔진 기반 구조 — 솔루션 3계층 + Scene/Layer/GameObject/Component

- 출처: 블로그 "솔루션 구조", "씬, 게임 오브젝트 구조", "Base 클래스",
  "Transform 컴포넌트"
- 솔루션을 **System(게임 무관: 수학·그래픽 디바이스·타이머) / Utility(게임 일반:
  Scene·GameObject·Texture·Collider) / Client(이 게임 전용)** 3계층으로 나눴다.
  경계가 애매한 클래스(Sound)가 있었다고 본인이 적어뒀다.
- `CBase`가 참조 카운트 + `Add_Reference`/`Release`를 갖는다. 댕글링 포인터·누수
  예방 목적.
- Scene은 한 번에 하나만 생성. **"모든 씬을 미리 만들어두는 안"을 검토했다가
  초기 로딩이 너무 길어질 것 같아 기각**했다고 적혀 있다 — 44번(멀티스레드 로딩)의
  전사(前史)다.
- Layer 컨테이너를 `map<문자열>` → 선형 자료구조로 바꾸려 했으나 **팀원이 문자열
  키의 디버깅 편의를 강하게 주장해 유지**. 대신 동적 생성되는 GameObject의 키 중복
  문제를 `unordered_multimap`으로 풀었다(정렬 불필요 + 기존 인터페이스 유지).
- Transform은 부모-자식·빌보드·월드 행렬 계산을 담당. **팀원 주장으로 Update와
  Late_Update에서 월드 행렬을 두 번 계산**하게 됐고, 빌보드에서 모든 부모의
  회전값을 재귀적으로 더하고 빼느라 **프레임 드랍이 있었다**고 본인이 적었다.
- **`대안 비교` 섹션에 넣을 재료(자료구조 선택 근거)와 `단점`이 이미 다 있다.**
  자료구조·알고리즘을 요구하는 JD에서 29번(라이브러리)보다 이쪽이 실전 근거다.

### 40. 2.5D 배 구현 — 부모-자식 Transform으로 흔들림 전파

- 출처: 블로그 "배 구현"
- 풀어야 했던 문제 셋이 글에 정리돼 있다: ① 원작은 2D인데 2.5D로 만들고 싶었다
  ② 배가 물에 **경계면 곡선을 따라** 잠겨야 하고 수위도 요동쳐야 했다 ③ 배가
  흔들릴 때 배 위 물체도 같이 흔들려야 했다.
- 해법: 배 Transform을 루트로 두고 부품을 **자식으로** 붙였다. 갑판은 XZ 평면에
  평행하게 둬서 플레이어·몬스터가 평면에서만 움직이고, 몬스터 포격은 3D 포물선을
  그리며 갑판에 탄착한다. **배에 올라온 오브젝트는 자동으로 자식이 되게** 만들어
  흔들림이 공짜로 전파된다.
- 배 몸체는 빌보드로 카메라를 보게 하고 기울여서 아랫부분이 잠기게 했다.
- ⚠ **물에 잠긴 효과의 그레이스케일 셰이더는 다른 팀원 작업이다.** 본인이 적어뒀다.
- 46번(Transform)과 한 줄기. **"부모-자식 하나로 흔들림 전파를 공짜로 얻었다"가
  이 사례의 핵심**이고, 그 대가가 46번의 재귀 빌보드 프레임 드랍이다. 묶으면
  장점과 단점이 한 사례 안에서 맞물린다.

### 26. 항해 시스템 — 육각 CellMap

- 출처: 블로그 "항해 시스템"
- 파일: `CellMap`, `CellGenerator`, `Cell` 파생들(`BattleCell`, `DriveCell`,
  `BossCell`, `DummyCell`, `IslandCell`)
- ⚠ **지도 UI는 다른 팀원이 만들었다. 본인은 CellMap 시스템만 담당.** 본인이 적어뒀다.
- 내용:
  - 7×8 육각 격자에서 **행마다 열 개수가 다르다.** 일반식
    `ColumnCount = m_iColCount + iCenterRow - abs(iCenterRow - row)`가 글에 있다.
  - 인접 칸 인덱스 규칙을 중앙 행 위/중앙/아래 세 경우로 나눠 정리했다.
  - 랜덤 생성: 고정 위치 칸을 먼저 채우고, 남은 칸 수만큼 `map<CELL_TYPE, int>`에
    적힌 개수대로 Cell을 만들어 list에 넣고 `shuffle` 후 앞에서 뽑아 채운다.
    **"일정 개수 보장 + 랜덤 배치"를 셔플로 푼 것.**
  - 칸 종류별 동작이 다른데 Scene에서는 일관되게 돌아가야 해서, `CCell`에
    `Update`/`Clear` 프레임워크를 두고 `On_Arrival` / `Update_Before_Arrival` /
    `Update_After_Arrival` / `Is_Cleared`를 순수 가상으로 파생에 위임했다.
    **템플릿 메서드 패턴.**
  - 직접 만든 `Interpolate` 함수로 배 가감속을 보간. 칸 종류마다 도착 후 속도와
    도착 지점이 달라 까다로웠다고 적혀 있다.
- 아쉬운 점(본인 서술): 마지막 열마다 의미 없는 `CBlackCell`이 하나씩 생성된다.
  하나만 있어도 됐을 것 같고, 실제로 방문하지 않는 Cell도 객체는 생성된다.
  줄일 수 있었을 것 같은데 마음이 급해서 못 했다.
- **JD가 `자료구조·알고리즘을 코드로 구현`을 요구할 때 이게 가장 좋다.** 격자
  인덱싱 일반식·인접 규칙·셔플 분배가 전부 본인이 유도한 것이고 글에 수식까지 있다.

### 41. 상호작용 시스템

- 출처: 블로그 "상호작용 시스템"
- 상속 사슬: `CGameObject` → `CInteractableObject` → `CHoldableObject` →
  `CPlaceableObject`, 그리고 받침대인 `CProp`.
- 계약은 순수 가상 두 개다: `Interact(...)`와 **오버로드된
  `Is_InteractionPossible`** — 하나는 상호작용 종류에 무관하게 "가능한가",
  다른 하나는 특정 종류(E / Space)로 "가능한가".
- 로직 4단계가 글에 정리돼 있다: 접근 시 가능 여부 확인 → 매 프레임 주변 후보 중
  **가장 가까운 것 하나** 선택 → 키 입력 시 해당 종류 가능 여부 재확인 → 실행.
- "플레이어 행동의 절반이 상호작용"이라 본인이 중요하게 봤다고 적혀 있다.
- Dogong의 21번(InteractComponent + IInteractable)과 **같은 문제를 상속 사슬 vs
  컴포넌트+인터페이스로 다르게 푼 사례다.** 두 개를 나란히 놓으면 "2년 사이에
  같은 문제를 다르게 풀게 된 이유"가 나온다 — 성장 서사를 만들 수 있는 조합.

### 42. 충돌 처리 시스템 — Check Matrix + Collision ID

- 출처: 블로그 "충돌 처리 시스템"
- 요구사항 6개를 먼저 나열하고 시작한다(범위, Enter/Stay/Exit 판별, 위치 확정 후
  검사, 레이어 필터, 오브젝트당 다중 충돌체, 충돌체별 검사 방식).
- 구현:
  - `Collider`는 Position/Offset/Scale. AABB 사용. `CLineCollider` 파생은 상대
    콜라이더의 중점이 선을 넘었는지 검사한다.
  - **Check Matrix**: 32×32 비트 행렬의 행·열이 레이어 ID. 켜진 칸의 레이어 쌍만
    검사한다. 대각선 반대쪽 절반은 무시(= 무방향 검사).
  - **Collision ID**: 충돌체마다 고유 ID를 주고 **두 ID를 union으로 합쳐 64비트
    키**를 만든다. 이 키가 씬에서 유일하므로 `map<LONGLONG, bool>`에 직전 프레임
    충돌 여부를 넣어두면 Enter/Stay/Exit를 판별할 수 있다.
- 아쉬운 점(본인 서술): **요구사항 5·6번을 못 풀었다.** 해결법까지 적어놨다 —
  Check Matrix의 나머지 절반을 써서 단방향 검사를 하면 6번이 풀리고, 검사 단위를
  Collider가 아니라 GameObject로 올리면 5번이 풀린다. **"코드를 상당수 고쳐야 하고
  시간이 오래 걸린다는 팀원의 만류로 못 했다"**고 끝난다.
- **`장단점`의 단점과 `회고`가 통째로 나와 있는 항목.** 다만 "팀원이 말려서 못
  했다"는 결말은 편집이 필요하다.

### 43. 이벤트 시스템 — 프레임 말 지연 처리 + 옵저버

- 출처: 블로그 "이벤트 시스템"
- 만든 이유가 명확하다: **오브젝트 생성·삭제가 프레임 중간에 일어나면 같은 프레임
  안에서 오브젝트들이 서로 다른 정보로 동작한다.** 이걸 막으려고 만들었다.
- 구현:
  - `EventMgr`가 한 프레임 동안 발생한 `CEvent` 객체들을 모아뒀다가 **렌더링 후
    `FinalUpdate`에서 한꺼번에 처리**한다.
  - `CEvent` 파생으로 이벤트 종류를 확장한다. 기본 3종: `CDeadObjEvent`,
    `CCreateObjEvent`, `CSceneChangeEvent`.
  - **삭제는 2프레임에 걸쳐 한다.** 삭제 이벤트는 `m_bDead`만 켜고, 다음 프레임
    Update에서 참조하던 오브젝트들이 이를 보고 참조를 해제한 뒤, Late_Update에서
    실제 Release. 댕글링 참조를 구조로 막았다.
  - 옵저버 패턴으로 구독. `CEventHandlerWrapper`에 자기 포인터와 콜백을 담아
    `EventMgr`에 등록하면 이벤트 처리 전/후에 불린다.
- 아쉬운 점(본인 서술): **구독 API가 너무 복잡해서 사용률이 저조했다.** 쉽게 만들
  방법을 고민했지만 답을 못 찾아서 **노션에 사용 설명서를 만들어 팀에 배포**했다.
  그리고 `EVENT_ID` enum이 Engine에 있어서 Client 전용 이벤트를 추가하기 어렵다,
  정수형 + `void*`로 받았으면 됐을 텐데 시간이 부족했다고 적혀 있다.
- **"내가 만든 시스템을 팀이 안 썼고, 그 이유가 내 API 설계였다"** — 자기 설계의
  실패를 원인까지 짚고, 문서 배포라는 차선책을 실행한 기록. 이 목록에서 회고의
  질이 가장 높다. **`다양한 직군과 협업`을 물어보는 JD에서 쓸 수 있는 소재이기도
  하다** (직군은 같지만, 남이 쓸 것을 만든 이야기다).

### 44. 멀티 쓰레드 로딩 시스템

- 출처: 블로그 "멀티 쓰레드 로딩 시스템"
- 만든 이유: **개발 중 로딩 시간 때문에 본인들이 불편을 겪어서.** 단일 스레드
  순차 로드라 느렸고, 당장 필요 없는 리소스까지 다 기다려야 했다.
- 구현:
  - `CLoading`에 씬별 로딩 함수(`Loading_For_TOWN`, `Loading_For_SAILING` 등)를
    두고, `CLoadMgr`가 프로그램 시작 시 **씬마다 스레드를 하나씩** 만들어 각
    함수를 `Thread_Main`으로 돌린다.
  - `CSceneChanger`가 페이드아웃 완료 후 `LOAD_MGR->Is_LoadFinished(다음 씬)`를
    확인하고, 다음 씬 Create까지 끝나야 페이드인한다.
  - 로딩 시간의 주범인 **보스 리소스만 `Loading_For_SAILING2`로 분리**하고,
    SailingScene 진입 시 그것만은 완료를 확인하지 않고 그냥 들어가는 꼼수를 썼다.
    "정상 진행이면 보스 칸 도달 전에 로드가 끝날 것이 자명"해서.
- 아쉬운 점(본인 서술): `SceneChanger`가 UI와 씬 전환 기능이 결합돼 있어 아쉽다.
  그리고 **보스 리소스 꼼수가 무용지물이 됐다** — 담당자가 보스 애니메이션 최초
  재생 시 프레임 드랍을 막으려고 미리 작게 재생하는 방식을 써서, 결국 진입 전에
  전부 로드돼 있어야 했기 때문이다.
- **본인 근거로 `멀티스레드`를 댈 수 있는 유일한 항목이다.** 33번(IOCP)이 강의
  기반일 수 있는 것과 달리 이건 출처가 명확하다.
- **"최적화를 넣었는데 다른 사람의 대응 때문에 효과가 사라졌다"**는 결말도 드문
  소재다. 협업하는 코드베이스에서 최적화가 어떻게 무력화되는지의 실례.

### 45. 아이템 시스템

- 출처: 블로그 "아이템 시스템" (인벤토리 UI는 제외한 범위)
- 문제 정의: 이 게임은 **아이템 상호작용이 곧 장착**이다. 유물을 화물칸에 실으면
  능력이 적용되고, 장신구는 상호작용으로 장착된다. 화물칸에 유물만 실리는 것도
  아니다.
- 구현: `CPlaceableObject`(41번 사슬의 끝)에 **상황별 훅 함수를 순수 가상이 아닌
  빈 가상 함수로 잔뜩 선언**했다 — `On_ItemEquip`, `On_PlayerPaddleAttack`,
  `On_PlayerCritBulletAttack`, `On_ShipTakeDamage`, `On_RepairShip`,
  `On_LoadBullet`, `On_MonsterDead` 등. `Inventory`가 상황 발생 시 장착 중인 모든
  아이템의 해당 훅을 호출한다. 스탯은 `CStat` 컴포넌트를 아이템에도 붙여
  장착/해제 시 더하고 뺀다.
- 아쉬운 점(본인 서술): **개발 후반에 시간에 쫓겨 만들어 아쉬운 게 많다.**
  `PlaceableObject`가 이름과 달리 구분용 enum과 효과 함수로 범벅됐고, 구분용
  enum이 난잡하게 늘었다(`CARGO_ID` 안에 Bullet Generator 구분이 있는데
  `BULLET_GENERATOR_ID`가 따로 또 있다). **원인을 "처음부터 면밀한 분석이 없었기
  때문"으로 짚고 다음엔 정확한 분석이 필요하다고 맺는다.**
- 41번과 묶어 쓰면 "상속 사슬이 잘 돌아가다가 어디서 무너졌는가"가 된다.

### 그 밖에

- **UI 매니저** (블로그 "UI 매니저") — `list<CUI*>` 관리 + 직교 투영(`D3DXMatrixOrthoLH`)
  전용 UI RenderGroup. **본인이 "UI매니저의 존재 가치가 별로 없다"고 결론짓는다.**
  다른 GameObject와 똑같이 Update 돌리고 RenderGroup에 넣을 뿐인데 왜 따로 관리하는가,
  Layer에서 관리하고 포인터만 들고 있어도 됐다는 것. 게다가 UI가 출력뿐 아니라 데이터
  조작까지 하게 돼서 **씬 전환을 하려고 UI 매니저의 SceneChange를 부르는 "기현상"**이
  벌어졌다고 적었다. 단독 사례로는 얇지만, **"내가 만든 걸 스스로 폐기 판정한
  기록"**이라 회고 소재로는 강하다.
- **애니메이션 시스템** (블로그 "애니메이션 시스템") — 넘버링 이미지 텍스처를 시간
  간격으로 전환. 끝 프레임에서 `On_AnimationEnd` 콜백. 본인도 "간단한 시스템"이라
  적었다. 아쉬운 점으로 **"특정 프레임에 원하는 동작을 실행시키는 기능이 있었으면"**을
  꼽는데, **이게 정확히 PluckySquire 38번(애니메이션 이벤트 시스템)에서 만든 것이다.**
  → 39·38번과 묶으면 **"한 프로젝트에서 아쉬웠던 걸 다음 프로젝트에서 만들었다"**는
  연결이 실제 기록으로 증명된다. **이 목록에서 가장 좋은 조합 중 하나.**
- **강화 섬** (블로그 "강화 섬") — `CIslandCell` 파생. 섬 / NPC(`Reinforcer`) /
  UI 패널을 생성·중계하는 구조. `Reinforcer`가 재화·최대 레벨을 확인하고 결과를
  섬에 알리면 섬이 UI에 연동한다. 아쉬운 점: 공격력·연사 속도만 올라 재미 요소가
  부족하다, 강화 존 전용 카메라를 구현 못 했다.

---

## CopyTrickster (트릭스터 모작, WinAPI, 2024-06)

⚠ **GitHub에 커밋이 단 1개("CopyTrickster First Commit")다.** 완성본을 통째로 올린
형태라 개발 과정이 전혀 남아 있지 않다. 사례를 쓰려면 코드 구조와 사용자 기억만
근거가 된다.

### 27. 라인 기반 지형·충돌

- 근거(파일): `Line.h`, `LineMgr.h`, `CollisionMgr.h`, `EventMgr.h`,
  `AbstractFactory.h`, `CharacterDataBase.h`, `CItemDataBase.h`, `CUIQuestWindow.h`,
  `CUISkillInventory.h`, `DropManager.h`, `MonsterSpawner.h`, `fmod.h`(FMOD 사운드)
- 2D 횡스크롤에서 발판을 선분으로 다루는 고전 기법. GDI만으로 게임을 굴린
  이야기라 "제약 안에서의 선택" 각도가 있다.
- 확인 필요: 전부.

---

## 툴·라이브러리·기타

### 28. WMI/ETW 기반 시스템 자원 로깅 도구 (ResourceMonitor, 2021.11~12) ★실무

- **⚠ 이 목록에서 유일하게 기업 소속으로, 업무 지시를 받아 한 작업이다.**
  다른 후보는 전부 개인·팀 포트폴리오 프로젝트다.
  **"실무 경험 없는 지원자"로 전제하고 문서를 구성하지 말 것.**

  | | |
  |---|---|
  | 기업 | HB 테크놀러지 |
  | 소속 팀 | 소프트웨어 개발 1팀 |
  | 고용 형태 | **일학습병행제** (인턴) |
  | **재직 기간** | **6~7개월** (정확한 시작·종료일은 사용자도 미확인) |
  | 프로젝트 기간 | **불명** — 포트폴리오의 `2021.11~12`는 기억이 흐려 대충 적은 값 |
  | 개발 경위 | **업무 지시로 개발** |
  | 실사용 여부 | **확인 불가** — 완성 직후 퇴사. 다만 **사내에서 쓰일 것이라고 전달받고 개발**했다 |

  출처: 포트폴리오 슬라이드 14 + 사용자 확인(2026-08-26).

  **표기 시 주의 3가지.**

  1. "실무 경험"을 헤드라인으로 앞세우지 않는다. 사실만 붙여 쓴다 —
     `HB 테크놀러지 소프트웨어 개발 1팀 / 일학습병행제 / 사내 요청으로 개발`.
     **일학습병행제라는 제도명을 숨기지 않는다.** 숨기면 면접에서 고용 형태를
     물었을 때 어색해지고, 밝히면 정식 훈련 과정을 거쳤다는 정보가 된다.
  2. **기간은 재직 기간(6~7개월)을 쓴다. 프로젝트 기간은 적지 않는다.**
     현재 포트폴리오의 `2021.11~12`는 부정확할 뿐 아니라 **6~7개월 재직을
     2개월로 보이게 만들어 스스로를 깎고 있다.** 정확한 날짜는 근로계약서,
     고용보험 피보험자격 이력내역서, 일학습병행제 수료증 중 하나로 확인 가능하다.
     확인 전까지는 연도만 쓰거나 비워둔다 — 추정치를 적지 않는다.
  3. **"사내에서 사용되었다"고 쓰지 않는다.** 확인된 사실이 아니다. 쓸 수 있는
     최대치는 **"사내 사용을 전제로 요청받아 개발"**이며, 이건 사실이고 무게도
     충분하다. 면접에서 실사용 여부를 물으면 *"완성 직후 퇴사해서 실제 사용
     여부는 확인하지 못했습니다"*가 정답이다. 모른다고 답하는 건 감점이 아니고,
     지어내는 것이 감점이다.
- 근거: 레포 README — 윈도우 기본 작업관리자·리소스 모니터에 **로그 기능이 없어서
  직접 만들었다**고 적혀 있다. MFC `CScrollView` 파생 뷰 4종(CPU/Memory/Disk/
  Network), WMI + ETW로 성능 데이터 수집, 실행 환경은 윈도우 7 상정,
  VS 2015/2008 환경. C++ 280KB.
**WMI / ETW 분담 (README 확인)**

README의 `Files` 절이 어느 지표를 어느 API로 뽑았는지 명시하고 있다.

| API | 담당 지표 | 클래스 |
|---|---|---|
| **WMI** | **CPU, 메모리** | `PerfDataManager`, `PerfData`(추상), `PerfDataPerProcess`, `PerfDataOS`, `PerfDataOSProcessor`(CPU 총 사용량) |
| **ETW** | **디스크, 네트워크** | `Etw` |

- 성능 데이터 클래스가 **추상 클래스 `PerfData` 아래 프로세스별/OS별로 파생**되고
  `PerfDataManager`가 관리하며 Doc과 통신한다. MFC Doc/View 구조 위에 얹었다.
- ⚠ **왜 이렇게 나눴는지는 어디에도 안 적혀 있다.** README에도, 블로그에도 없다
  (블로그 `ETW` 검색 결과 0건). **사용자에게 확인해야 하는 항목이다.**
- (조사자 가설 — 사용자 확인 전까지 사례에 쓰지 말 것) 윈도우에서 **프로세스별
  디스크·네트워크 I/O는 성능 카운터로 노출되지 않아** 통상 ETW가 필요하다.
  분담이 정확히 그 경계와 일치하고, README가 "기존 윈도우 리소스 모니터에 로그
  기능을 추가한 형태"를 목표로 적고 있는데 리소스 모니터 자체도 같은 구조다.
  **다만 이건 추론이므로, 사용자가 그렇게 판단했다는 근거는 없다.**

**README에서 추가로 확인된 것**

- **조건부 로깅.** 단순히 찍는 게 아니라 `Log Interval`(주기), **`Log threshold`
  (설정 값 이상의 데이터만 기록)**, `Log path`를 메뉴로 설정할 수 있다.
  로그가 목적인 도구였으니 이 부분이 핵심 기능이다.
- **버전 관리를 했다.** `Version_Dialog`가 변경 이력을 표시하고, README에
  v1.2.0 → v2.0.0 → v2.1.0(2022-01-07) 이력과 스크린샷이 남아 있다.
- **VS 2008과 2015 두 버전을 병행하다 2015를 중단**했다(README에 명시).
  실행 환경이 윈도우 7이라 구형 툴체인을 써야 했던 것으로 보인다 — 이유는 미확인.
- **알려진 한계를 문서화했다**: "Windows 10에서는 Disk 데이터 표시가 정확하지 않음"
  (2022-01-26 기준). 자기 도구의 결함을 README에 적어둔 것이라 **`장단점`의 단점이
  이미 확보돼 있다.**

**블로그의 관련 기록 — 디버깅 4건 (2021.10)**

ResourceMonitor 시기와 정확히 겹치는 짧은 디버깅 노트들이다. `벌레잡이`
카테고리(3편) + `카테고리 없음` 1편.

- **BSTR 포인터 별칭 문제** — 변수 하나를 고쳤는데 다른 변수가 같이 바뀌는 현상.
  원인은 `BSTR`이 사실상 `wchar*`라 같은 주소를 여러 변수가 참조하게 된 것.
  결국 `BSTR`을 버리고 `CString`으로 바꿔 해결. **COM/WMI를 쓰다 만난 문제다.**
- **메모리 누수** — *"Resource Monitor 프로젝트를 진행하다가 처음으로 메모리 누수
  현상을 겪었다"*고 적혀 있다.
- **`CFile::Write` 문자 사이 공백** (2021.10.30) — 유니코드/멀티바이트 차이 때문에
  글자 사이에 공백이 끼고 절반만 출력됨. `W2A`로 변환해 해결. (태그의
  `WBCS`/`MBCS`가 이 글이다)
- **LINK 2019** (2021.10.19) — 라이브러리 헤더 include와 `#pragma comment(lib, …)`
  순서 문제.

→ 짧지만 **실무 기간에 남긴 유일한 기술 기록**이고, 넷 다 "C++/윈도우 저수준에서
처음 만나는 함정"들이다. 사례 본문에 쓸 분량은 아니지만, 면접에서 이 프로젝트를
물었을 때 꺼낼 구체적 일화로는 충분하다.

**이 항목을 어떻게 쓸 것인가**

- **메인 사례로는 약하다.** 2개월, 5년 전, 게임 아님, 신입 지원. 이건 사실이다.
- **다만 두 가지 때문에 버리지는 않는다.**
  1. **ETW는 흔치 않다.** 학원·대학 과정에서 안 건드리는 영역이라, 짧게라도
     언급하면 "OS를 들여다본 적 있는 사람"이라는 신호가 된다. 게임 회사에서는
     프로파일링·성능 계측 감각으로 연결된다 — 실제로 1번 사례(3D DDA)가
     프로파일링으로 병목(12.98%)을 찾는 데서 시작한다.
  2. **"필요한데 도구가 없어서 만들었다"의 최초 사례다.** 이 사람의 반복
     패턴 — 5번(FBX/NIF 변환기), 6번(아이콘 자동 생성), 37번(애니메이션 툴),
     59번(가이드 문서 4건) — 이 2021년부터 2026년까지 이어진다는 근거가 된다.
     **JD에 `툴 제작 및 자동화`가 있으면 37·38번 사례의 도입부에 한 문장으로
     넣는다.** 단독 장을 주지 않는다.
- 시스템 프로그래밍·OS 이해를 요구하는 자리라면 순위가 완전히 달라진다.

- **확인 필요 (우선순위 순)**
  1. **재직 시작·종료 월.** 근로계약서 / 고용보험 피보험자격 이력내역서 /
     일학습병행제 수료증으로 확인된다. 지금 포트폴리오 표기가 실제보다
     불리하게 적혀 있으므로 이것부터 고친다.
  2. **WMI(CPU·메모리) / ETW(디스크·네트워크)로 나눈 이유.** 분담 자체는 README로
     확정됐지만 이유는 어디에도 없다. 위의 조사자 가설이 맞는지만 확인되면
     "라이브러리 두 개 써봤다"가 **"각각 뭘 잘하는지 알고 골랐다"**로 바뀐다.
     이 항목에서 값이 가장 크게 오르는 질문이다.
  3. 요청받은 요구사항이 무엇이었는지 (로그 기능만? 뷰 4종도 요구사항이었나?).
     업무 지시로 만든 것이므로 **요구사항의 출처가 남에게 있다** — 이게 개인
     프로젝트와의 결정적 차이라 사례의 '배경'에 들어가야 한다.
  4. 완성도 — 어디까지 만들고 끝냈는지.

### 29. 자료구조 템플릿 라이브러리 (MyTemplateLibrary, 2025-05)

- 근거: 레포 설명 "자료구조 & 알고리즘 라이브러리", C++ 40KB. 로컬
  `D:\Workbench\Projects\DataStructure`에도 있음.
- **JD가 "자료구조·알고리즘을 코드로 구현"을 조건으로 걸 때 직접 증빙이 된다.**
- 다만 학습 산출물이라 "문제 해결 사례" 형태로 쓰기 어렵다. **단독 사례보다
  다른 사례(1·2·4)의 근거로 붙이는 쪽을 권한다.**
- 확인 필요: 어떤 자료구조를 구현했는지, STL 대신 만든 이유.

### 30. 직접 만든 컴파일러와 언어 (MyCompiler, 2024-04)

- 근거: 레포 설명 "내가 만든 내 컴파일러와 언어". C++ 43KB.
- ⚠ README 인코딩이 깨져 상세 확인 불가. **소스를 열어봐야 실체를 안다.**
- 파서·AST 구현이 실제로 있다면 알고리즘 역량 증빙으로 강력하다. **확인 우선순위 높음.**

### 31. 코어 키퍼 맵·오브젝트 에디터 (CoreKeeperTool, 2024-07, 4차 팀과제 ⚠)

- 근거(파일): `CClientTerrain`, `CObjObstacle`, `ObjMgr`, `UIMgr`, `MultiTexture`,
  `SingleTexture`, `SceneMgr`, `ObjEditor시나리오.txt`, `rename_pngs.bat`
- 툴 제작 팀과제. `ObjEditor시나리오.txt`가 있는 걸 보면 사용 시나리오를 문서로
  정의하고 만든 것으로 보인다. `rename_pngs.bat`은 리소스 일괄 정리 자동화.
- 확인 필요: 팀 내 담당 범위 (커밋 이력 미확인).

### 32. Unity C# 원카드 게임 (OneCard, 2021)

- 근거: C# 1.5MB, ASP.NET 118KB, ShaderLab. 빌드 산출물(`onecard.exe`) 포함.
- ⚠ **현재 확인되는 유일한 C# 프로젝트다.** 2021년 작업이고 이후 5년간 C# 코드가
  없다. C#을 요구하는 JD에서는 이것밖에 댈 게 없다.
- 확인 필요: ASP.NET이 왜 들어가 있는지(서버가 있었나?), 완성도, 본인 단독인지.

### 33. IOCP 게임 서버 (IOCPServer / Chat / 로컬 GameServer-master)

- 근거(파일): `ServerCore/`, `GameServer/`(GameSession, GameSessionManager, Room,
  Player, ClientPacketHandler), `DummyClient/`, protobuf(`Protocol.pb.h`,
  `Struct.pb.h`, `Enum.pb.h`), `Common/Procedures/Templates/`,
  `Recv,SendBuffer.txt`, `실행흐름.txt`. `Chat`은 ChatServer/ChatClient 쌍.
- **JD가 소켓·멀티스레드를 요구할 때 유일하게 맞는 소재다.**
- ⚠ **그런데 IOCPServer README에 "using server core library"라고 적혀 있고, 로컬
  `GameServer-master`는 git 저장소가 아니다. 강의(루키스류) 코드를 따라간 것일
  가능성이 높다.**
- **확인 완료 (2026-08-27) — 사례로 쓰지 않는다.** 사용자 확인: "사실상 따라 친
  코드". 소켓·네트워크 우대 항목은 이것으로 대응하지 않는다.

---

## 59. 팀에 배포한 가이드 문서 (Shipgend / PluckySquire 공통)

- 출처: 기술소개서 슬라이드 72, 포트폴리오 슬라이드 11, 블로그 "이벤트 시스템",
  그리고 Notion 가이드 2편 (→ [`Sources/Portfolios.md`](../Sources/Portfolios.md))
- **세 프로젝트에 걸쳐 네 번 반복된다:**

  | 문서 | 프로젝트 | 실물 |
  |---|---|---|
  | 애니메이션 툴 가이드 | PluckySquire | Notion 링크 확보 |
  | 애니메이션 이벤트 가이드 | PluckySquire | Notion 링크 확보 |
  | 상호작용 시스템 가이드 | PluckySquire | 언급만 (링크 미확보) |
  | EventMgr 사용 설명서 | Shipgend | 언급만 (블로그에 링크 있음) |

- 내용의 질이 근거가 된다:
  - **애니메이션 툴 가이드** — 기능 목록 → 화면 → 사용 방법 순. 폴더 구조 제약
    같은 **주의 사항이 번호로 붙어 있고, 버전 표기("2.09 추가됨")까지 있다.**
    문서를 한 번 쓰고 만 게 아니라 갱신했다는 뜻이다.
  - **애니메이션 이벤트 가이드** — 팀원이 따라 할 수 있게 **4단계 + 예시 코드**.
    `std::bind`가 처음인 팀원을 위한 설명이 따로 들어 있다.
- **Shipgend 43번이 이 항목의 시작점이자 동기다.** 블로그에 *"이벤트 구독 시스템의
  사용법이 너무 복잡해서 사용률이 저조했다. 쉽게 만들 방법을 고민했지만 답을
  못 찾아서 대신 사용 설명서를 만들어 배포하기로 했다"*고 적혀 있다.
  → **"API 설계로 못 푼 문제를 문서로 메웠고, 다음 프로젝트에서는 처음부터
  문서를 냈다"**는 흐름이 실제 기록으로 이어진다.
- **JD의 `다양한 직군과 협업`에 댈 수 있는 가장 좋은 카드다.** 직군은 같지만
  "내가 만든 것을 남이 쓰게 만드는 일"을 반복했고 산출물이 남아 있다.
  `읽기 쉬운 코드를 작성하려 노력하는 분`이라는 우대 항목과도 직접 이어진다.
- 단독 사례로 쓰기엔 얇다. **37·38·43번 본문에 한 문단씩 넣고, 문서 말미나
  자기소개에서 한 번 묶어 언급하는 쪽이 낫다.**
- 확인 필요: 가이드를 쓰고 나서 팀의 사용률이 실제로 올랐는지, 질문이 줄었는지.
  상호작용 시스템 가이드 링크.

---

## 34. 생성형 AI 개발 워크플로우 구축 (CopyMaple2 / RTChess / Dogong 공통) — 작성 완료

> **작성 완료 (2026-08-27) → `Cases/build-verification-skill.md`**
> 범위를 **빌드 검증 스킬(build-test)** 중심으로 좁혀서 썼다.
>
> **⚠ 아래 근거 목록에 귀속 오류가 있었다.** `devlog` 시스템(README·FORMAT·CORE·
> log.sh·stats.sh·devlog 스킬)은 **팀원 smileJiro가 만든 것**이다
> (`chore(devlog): 개발 판단 기록 시스템 및 devlog 스킬 추가`, 2026-08-13).
> 사용자는 그 시스템의 사용자로 항목 5건 작성 + ID 충돌 재발번(`553dca95`) 기여.
> **devlog 번호 체계를 본인 설계로 쓰지 않는다.**
> 본인 작으로 확인된 것: build-test 스킬(`1732d2ed`), UE MCP(`d96c9b7a`),
> 에디터 Python 원격 실행(`e000c643`), 메모리뱅크(`7c6fea3e`·`d6b35a61`),
> glossary 최초 도입(`3ae30748`), Git 워크플로우 문서·브랜치 스킬(2026-04-27).
>
> **메모리 뱅크는 별도 사례로 분리했다 → `Cases/ai-memory-bank.md` (2026-08-27).**
> 실패 사례다. 블로그 https://ddukddaksudal.tistory.com/206 에 본인이 쓴 문제점
> 4가지가 있어 판단·회고를 그대로 쓸 수 있었다. 접은 이유는 "문제점이 많고 앞으로도
> 관리가 안 될 것 같아서"이고, 장르 전환은 계기일 뿐 이유가 아니다(사용자 확인).
> `.bak.20260526` 백업 4개가 왜 생겼는지는 사용자도 모른다 — 사례에 쓰지 않았다.

- 근거: Dogong `1732d2ed`(build-test 빌드 검증 스킬 추가), `d96c9b7a`(UE MCP 툴셋
  플러그인 활성화 및 Claude Code 서버 설정), `e000c643`(에디터 Python 원격 실행
  bRemoteExecution 활성화), `7c6fea3e`·`d6b35a61`(메모리 뱅크 스캐폴드),
  `3ae30748`(도메인 언어 glossary), devlog 번호 체계(DL-YYYYMMDD-NN),
  `553dca95`(devlog ID 충돌 해소를 위한 재발번) /
  RTChess `565e464`(CLAUDE.md 구조·아키텍처 문서화) /
  CopyMaple2 `7254017`(CLAUDE.md), `docs/01-아키텍처.md`~`04-리소스와데이터.md`
- **"AI로 코드를 짰다"가 아니라 "AI가 틀리지 않게 하는 장치를 만들었다"** 쪽 이야기다.
  빌드 검증 스킬, 용어집, 결정 로그, MCP로 에디터 직접 조작까지 있다.
- 게임 기술 사례가 아니라 프로세스 사례라, 문서 뒤쪽에 짧게 배치하는 용도.
- 확인 필요: 실제로 어떤 실패를 겪고 어떤 장치를 넣었는지. **이게 있어야 사례가 된다.**
  없으면 "이런 파일들을 만들었다"는 자랑에 그친다.

---

## 소재가 없는 영역

앞으로 JD에서 요구받을 수 있는데 **현재 프로젝트 전체에 근거가 없는** 항목이다.
지어내지 말고 공백으로 두거나, 사용자에게 다른 경험이 있는지 묻는다.

| 영역 | 상태 |
|---|---|
| **DB (MySQL 등)** | 6개 프로젝트 전체에서 DB 연동 코드 0건 |
| **C#** | **확정 (2026-08-27) — 없다.** 사용자 확인: OneCard(2021) 외 C# 경험 없음. 지어내지 말 것 |
| **라이브 서비스 운영** | 없음. 전부 개인·팀 포트폴리오 프로젝트 |
| ~~**다양한 직군과 협업**~~ | **일부 해소** — 59번(가이드 문서 4건)으로 "남이 쓸 것을 만들고 문서를 낸" 근거는 확보.<br>다만 여전히 프로그래머 대상이다. 기획·아트와 부딪힌 일화는 없음 |
| **모바일 / 콘솔 플랫폼** | 없음. 전부 PC |
| **CI/CD** | Dogong의 데디 서버 빌드 타겟(`02a3bb38`)과 빌드 검증 스킬 정도 |
| ~~**멀티스레드**~~ | **해소됨** — 44번(Shipgend 멀티 쓰레드 로딩)이 본인 작업으로 확인.<br>PluckySquire의 `ThreadPool`은 `smileJiro` 작성이므로 쓰지 않는다 |
| **셰이더 심화 (컴퓨트·GPGPU)** | PluckySquire에 `Compute_Shader`가 있으나 `nyongking` 작성. 본인 근거 없음 |
| **AI·길찾기 심화** | CopyMaple2 `8fb1691` WayFinder, Dogong BTTask 정도. 수준 미확인 |

## 유지보수

새 커밋이 쌓이면 후보도 늘어난다. `/audit`을 돌릴 때 이 문서도 같이 갱신하면
좋다. 확인이 끝난 항목은 `? 확인 필요`를 지우고, 사례로 쓴 항목은 `Cases/` 파일명을
적어둔다.

**조사 방법 주의.** 이 문서의 1차 조사는 커밋 로그 위주로 했다가 35~39번(하우징,
애니메이션 툴, 애니메이션 이벤트 시스템 등)을 통째로 놓쳤다. 커밋 메시지가
"임시 커밋"·"ㅇㅁㄴㄹ"인 프로젝트가 많아서 **로그만 보면 큰 시스템이 안 보인다.**
다음에 조사할 때는 반드시 이 순서로 한다.

0. **`Sources/Portfolios.md`의 블로그에 해당 프로젝트 카테고리가 있는지 먼저 본다.**
   있으면 거기서 시작한다 — 사용자가 직접 쓴 설계 의도와 회고가 있으므로, 코드에서
   추론할 필요 자체가 없어진다.
1. `ls <프로젝트>/Client/Public`, `Engine/Public`, `Tool_*/` — **클래스 이름 목록을
   먼저 훑는다.** 시스템은 커밋이 아니라 파일 이름에 남는다.
2. 별도 vcxproj/sln 프로젝트가 있으면 전부 확인한다 (툴이 여기 숨어 있다).
3. 팀 프로젝트는 파일별로 `git log --format="%an" -- <경로> | sort | uniq -c`를
   돌려 **작성자를 확인한 뒤에** 후보에 올린다.
4. 그다음에 커밋 로그로 시간 순서와 버그 수정 흔적을 붙인다.

Shipgend는 0번을 건너뛴 탓에 "커밋에 기술 판단 흔적이 거의 없어 사용자 기억에
의존해야 한다"고 잘못 적었었다. 실제로는 이 저장소에서 소재가 가장 잘 정리된
프로젝트였다.
