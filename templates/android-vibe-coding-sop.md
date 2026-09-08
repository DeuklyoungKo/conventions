# Android 바이브 코딩 표준 절차서 (SOP)
> Android 앱을 처음부터 개발할 때 AI가 자동으로 수행하는 절차
> 작성일: 2026-06-04 | TextReader 프로젝트 경험 기반

---

## 이 문서의 사용 방법

새 Android 프로젝트 시작 시, 사용자가 AI에게 다음과 같이 요청한다:

```
"android-vibe-coding-sop.md 절차대로 [앱 이름] 프로젝트를 준비해줘.
앱 개요: [한 줄 설명]
수익 모델: [광고/구독/유료/없음]
타겟 사용자: [설명]
저장 경로: [프로젝트 폴더 경로]"
```

AI는 **Phase 0 → Phase 5** 순서대로 모두 자동 처리한다.
사용자가 직접 해야 하는 항목은 `🙋 사용자 직접` 으로 표시한다.

---

## Phase 0. 시작 전 정보 수집 (AI가 사용자에게 확인)

아래 항목이 제공되지 않은 경우, 코딩 시작 전에 한 번에 모아서 질문한다.
(항목별로 따로 묻지 않는다 — 한 번에 묻는다)

### AI가 확인해야 할 정보

```
1. 앱 이름 (한글/영문)
2. 앱 한 줄 설명
3. 핵심 기능 (3~5개)
4. 타겟 사용자 (연령대, 특성)
5. 수익 모델 (AdMob 광고 / 인앱 구독 / 유료 앱 / 없음)
6. 1차 MVP 범위 (최소한으로 동작하는 기능만)
7. 프로젝트 저장 경로
8. Android 패키지명 (예: com.myapp.name)
9. Notion Tips 게시판에 발행할지 여부 (Y/N)
```

### 앱 카테고리별 Seed 색상 추천표 (정보 없으면 AI가 선택)

| 앱 카테고리 | 추천 Seed | 색상 코드 | 이유 |
|------------|----------|----------|------|
| 독서 / 노안 친화 | 따뜻한 갈색 | `#795548` | 눈에 편안, 피로감 적음 |
| 생산성 / 비즈니스 | 인디고 | `#3F51B5` | 신뢰감, 집중력 |
| 건강 / 웰니스 | 딥 그린 | `#2E7D32` | 자연스럽고 안정적 |
| 금융 / 가계부 | 딥 블루 | `#1565C0` | 안전감, 전문성 |
| 엔터테인먼트 | 보라 | `#6A1B9A` | 창의적, 생동감 |
| 식음료 / 레시피 | 오렌지 | `#E65100` | 식욕 자극, 따뜻함 |
| 소셜 / 커뮤니티 | 티얼 | `#00695C` | 신선하고 친근함 |
| 기본값 (불명확) | 인디고 | `#3F51B5` | 무난하고 범용적 |

---

## Phase 1. 기획 문서 작성 — `1_PRD.md`

**AI가 자동 생성한다.** 사용자 입력 없이 Phase 0 정보만으로 작성.

### 필수 포함 섹션

```markdown
# [앱명] 서비스 PRD
> Product Requirements Document v1.0 | [날짜]

## 1. 제품 개요
  1.1 서비스 한 줄 정의
  1.2 핵심 가치 제안 (3가지)
  1.3 목표 사용자 (1순위/2순위/3순위)
  1.4 수익 목표 (수익 방식, 월 목표, 필요 DAU, 목표 다운로드)

## 2. 플랫폼 및 기술 스택 (표)
  - 플랫폼, 언어, TTS/DB 등 핵심 결정사항

## 3. 1차 — 프로토타입 (MVP)
  - 기능 목록 [F-01] ~ [F-0N]
  - 제외 기능 (의도적 제외 명시)
  - 화면 구성 (ASCII 다이어그램)
  - 완료 기준 체크리스트 [ ]

## 4. 2차 — 프로덕트 (정식 버전)
  - 추가 기능 목록
  - 완료 기준

## 5. 3차 — 고도화
  - 추가 기능 목록
  - 완료 기준

## 6. 비기능 요구사항 (표)
  - 앱 시작 시간, 로딩 속도, 메모리, 오프라인 동작, APK 크기, 크래시율

## 7. UX 원칙 (타겟 사용자 특성 기반)

## 8. 수익 모델 상세
  - AdMob 수익 추정표 (DAU × eCPM 역산)

## 9. 출시 전략 (단계별 기간/목표 표)
  - ASO 키워드 목록

## 10. 디자인 가이드 작성 방향
  - Material Theme Builder 사용법
  - 선택 Seed 색상 및 이유
  - M3 컴포넌트 목록 표

## 11. 리스크 (표)
```

---

## Phase 2. 설계 문서 작성 — `2_PDP.md`

**AI가 자동 생성한다.** PRD를 기반으로 상세 설계 작성.

### 필수 포함 섹션

```markdown
# [앱명] 개발 계획서 (PDP)
> Product Design Phase v1.0 | [날짜]
> 프로젝트 분류: Private / Official

## 1. 개발 환경 (표)
  - IDE, 언어, 빌드, Min/Target SDK, 아키텍처, DB, 상태 관리

## 2. 프로젝트 구조 (폴더 트리)
  - ui/ data/ tts/ ad/ util/ 기준으로 구성
  - 각 파일명까지 명시

## 3. 의존성 라이브러리 (libs.versions.toml 코드블록)
  - Room, Coroutines, Lifecycle, AdMob, 인코딩 감지 등

## 4. 데이터 모델
  - Room Entity 코드블록 (Kotlin)
  - SharedPreferences 키 목록 코드블록

## 5. 화면 명세
  - 각 Activity/Fragment별:
    - 역할 설명
    - 레이아웃 ASCII 다이어그램
    - 버튼 정의 표
    - ViewModel 책임 목록

## 6~8. 핵심 구현 상세 (코드블록 포함)
  - TTS 구현 (TtsManager 클래스 뼈대)
  - 파일 처리 (SAF + 인코딩 감지)
  - AdMob 설정 (보안 처리 포함)

## 9. 화면 흐름 (ASCII 다이어그램)

## 10. 개발 태스크 체크리스트 ← 핵심
  > 상태 표기: [ ] 미완료 / [x] 완료 / [-] 진행중 / [!] 블로킹

  ### Week 1 — 기반 세팅
  - [ ] **T01** 설명 `예상시간`
  ...

  ### Week 2 — 핵심 기능
  - [ ] **T08** ...

  ### Week 3 — 마무리 + 출시
  - [ ] **T15** ...

## 11. 2차 개발 태스크
  - [ ] **T22** ...

## 12. 테스트 체크리스트
  카테고리별 - [ ] 목록 (코드블록 아닌 실제 마크다운 체크박스)

## 13. Play Store 등록 준비
  - 앱 정보 표
  - [ ] 등록 전 완료 체크리스트

## 14. 향후 설계 노트 (3차 대비)
```

### 태스크 구성 기준

| Week | 내용 | 태스크 수 |
|------|------|---------|
| Week 1 | Gradle + DB + 기본 화면 + 파일 처리 | 7개 |
| Week 2 | 핵심 기능 화면 + 주요 로직 | 7개 |
| Week 3 | 보조 기능 + 광고 + 출시 준비 | 7개 |

---

## Phase 3. 디자인 가이드 + M3 테마 파일 생성

**AI가 자동 생성한다.** 총 4개 파일.

### 3-A. `3_DesignGuide.md` 작성

```markdown
# [앱명] 디자인 가이드
> 기반: Material Design 3

## 1. 디자인 시스템 개요 (표)
  - Seed 색상, 선택 이유, 테마 파일 위치

## 2. 색상 시스템
  - Seed 색상 선택 이유 (HCT 설명)
  - Light Theme 색상표 (역할 / 코드 / 설명)
  - Dark Theme 색상표

## 3. 독서/콘텐츠 화면 전용 배경 테마 (해당 시)
  - 테마명 / 배경색 / 텍스트색 / 설명

## 4. 타이포그래피
  - M3 Type Scale 적용 표
  - 폰트 크기 조절 단계 (사용자 조절 가능한 경우)

## 5. 컴포넌트 스펙
  - 버튼 종류별 스타일명
  - 버튼 최소 크기 (dp)
  - 상단바 / 하단바 스펙

## 6. 간격 & 레이아웃 (표)

## 7. 아이콘 (표)
  - 사용처 / Material Symbols 이름

## 8. 접근성 체크리스트
  - 색상 대비, 터치 타겟, 텍스트 크기
```

### 3-B. `res/values/colors.xml` 생성

Phase 0에서 결정된 Seed 색상 기준으로 M3 HCT 알고리즘을 적용해 생성.

**Light 토큰 25개 + Dark 토큰 25개 = 총 50개** 색상 토큰을 포함한다.

필수 포함 네이밍 패턴:
```
md_theme_light_primary / onPrimary / primaryContainer / onPrimaryContainer
md_theme_light_secondary / onSecondary / secondaryContainer / onSecondaryContainer
md_theme_light_tertiary / onTertiary / tertiaryContainer / onTertiaryContainer
md_theme_light_error / onError / errorContainer / onErrorContainer
md_theme_light_background / onBackground
md_theme_light_surface / onSurface / surfaceVariant / onSurfaceVariant
md_theme_light_outline / outlineVariant
md_theme_light_shadow / scrim
md_theme_light_inverseSurface / inverseOnSurface / inversePrimary
(+ dark 버전 동일)
```

앱 전용 색상이 있으면 하단에 추가:
```xml
<!-- 앱 전용 (예: 독서 화면 배경) -->
<color name="reader_bg_ivory">#FAF3E0</color>
```

### 3-C. `res/values/themes.xml` 생성

```xml
<style name="Theme.[AppName]" parent="Theme.Material3.Light.NoActionBar">
    <!-- 색상 25개 토큰 연결 -->
    <!-- Status Bar 설정 -->
</style>
<style name="Theme.[AppName].Splash" parent="Theme.SplashScreen">
    <!-- Splash 설정 -->
</style>
```

### 3-D. `res/values-night/themes.xml` 생성

```xml
<style name="Theme.[AppName]" parent="Theme.Material3.Dark.NoActionBar">
    <!-- Dark 색상 25개 토큰 연결 -->
    <item name="android:windowLightStatusBar">false</item>
</style>
```

---

## Phase 4. 프로젝트 컨텍스트 파일 생성

**AI가 자동 생성한다.** 총 1개 파일.

### `.claude/CLAUDE.md` 생성

```markdown
# [앱명] — 프로젝트 컨텍스트 (AI 참조용)
> 작성일 | 작업 시작 전 반드시 이 파일을 참조할 것

## 프로젝트 분류 (표)
  - 분류, 플랫폼, 패키지명, 아키텍처, Min SDK, 디자인 시스템

## 핵심 문서 위치 (표)
  - 문서명 / 경로 / 내용 요약
  > 개발 태스크 진행 상황은 2_PDP.md 섹션 10 기준

## 기술 스택 (코드블록)
  - 언어, 빌드, DB, 상태 관리, 주요 기능 API, 광고, 기타 라이브러리

## 프로젝트 구조 (폴더 트리)

## 보안 규칙 (절대 위반 금지)
  - AdMob ID는 local.properties에만
  - .gitignore 확인 항목

## Android 개발 주의사항
  - 프로젝트 특성에 맞는 주의사항

## 현재 개발 단계
  - [완료] 문서 작업
  - [대기] Android Studio 프로젝트 생성 (사용자 직접)
  - [대기] T01부터 개발 시작

## 1차 MVP 완료 기준
  - [ ] 핵심 기능별 체크리스트
```

---

## Phase 5. Notion Tips 게시판 발행 (선택)

Phase 0에서 Notion 발행 여부가 Y인 경우 수행.

1. Notion MCP로 `💡 Tips` 게시판 하위 페이지 생성
2. 페이지 제목: `🎨 [주제] — [부제]` 형식
3. 내용 구성: gonsuit.com/lab 페이지 양식 참고
   - 인트로 (문제 제기)
   - --- 구분선
   - ## 섹션별 설명 (H2/H3 계층)
   - 코드블록, 표, 인용구(>) 활용
   - 핵심 정리 섹션으로 마무리
4. 생성 후 URL 사용자에게 전달

---

## Phase 6. 사용자 인계 🙋

AI가 처리할 수 없는 항목. 사용자가 직접 수행.

### 즉시 해야 할 것 (개발 시작 전)

- [ ] 🙋 **Google Play Console 계정** 생성 — $25 1회 결제
  → https://play.google.com/console
- [ ] 🙋 **Google AdMob 계정** 생성 → 앱 등록 → 광고 Unit 생성
  → https://admob.google.com
- [ ] 🙋 발급받은 **AdMob App ID**, **Banner Unit ID** 메모

### Android Studio 프로젝트 생성 (스캐폴딩)

```
1. Android Studio → New Project
   - Template: Empty Views Activity
   - Name: [앱명]
   - Package: [패키지명]
   - Language: Kotlin
   - Min SDK: API 26

2. 생성된 프로젝트에 AI가 만든 파일들 복사:
   - res/values/colors.xml
   - res/values/themes.xml
   - res/values-night/themes.xml
   - .claude/CLAUDE.md

3. gradle/libs.versions.toml → 2_PDP.md 섹션 3 내용 붙여넣기

4. AndroidManifest.xml → AdMob App ID 추가
   <meta-data android:name="com.google.android.gms.ads.APPLICATION_ID"
              android:value="ca-app-pub-XXXX~XXXX"/>

5. local.properties → AdMob ID 추가 (git 미포함 확인)
   ADMOB_APP_ID=ca-app-pub-xxxx~xxxx
   ADMOB_BANNER_ID=ca-app-pub-xxxx/xxxx

6. .gitignore에 local.properties 포함 여부 확인
```

### 완료 후 AI에게 전달할 말

```
"프로젝트 세팅 완료. T01부터 시작해줘."
```

---

## Phase 7. 개발 시작 (AI 코딩)

사용자가 "T01부터 시작해줘" 라고 요청하면:

1. `.claude/CLAUDE.md` 로 프로젝트 컨텍스트 확인
2. `2_PDP.md` 섹션 10 체크리스트에서 첫 번째 `[ ]` 항목 확인
3. 태스크 순서대로 구현 → 완료 시 `[x]` 체크 업데이트
4. 각 Week 완료 시 사용자에게 진행 상황 보고

### 태스크 진행 원칙

- 한 번에 한 태스크씩 완료 확인 후 다음으로 이동
- 코드 작성 후 해당 태스크의 **검증 기준** 확인
- 불명확한 요구사항은 코딩 전에 질문 (코딩 후 수정 방지)
- `2_PDP.md` 화면 명세·데이터 모델·구현 상세를 반드시 참조

---

## 전체 파일 생성 목록 요약

| Phase | 파일 | 경로 | 생성 주체 |
|-------|------|------|---------|
| 1 | PRD | `1_PRD.md` | AI 자동 |
| 2 | 개발 계획서 | `2_PDP.md` | AI 자동 |
| 3 | 디자인 가이드 | `3_DesignGuide.md` | AI 자동 |
| 3 | M3 색상 토큰 | `res/values/colors.xml` | AI 자동 |
| 3 | Light 테마 | `res/values/themes.xml` | AI 자동 |
| 3 | Dark 테마 | `res/values-night/themes.xml` | AI 자동 |
| 4 | 프로젝트 컨텍스트 | `.claude/CLAUDE.md` | AI 자동 |
| 5 | Notion 팁 페이지 | Notion Tips 게시판 | AI 자동 (선택) |
| 6 | Android 프로젝트 | Android Studio | 🙋 사용자 직접 |

---

## 체크리스트 — AI 자동 처리 완료 기준

```
[ ] 1_PRD.md 생성 (기능 3단계, 수익 모델, 리스크 포함)
[ ] 2_PDP.md 생성 (화면 명세, 코드 구조, 체크리스트 T01~T21 이상)
[ ] 3_DesignGuide.md 생성 (색상표, 컴포넌트 스펙, 접근성 체크리스트)
[ ] res/values/colors.xml 생성 (Light 25개 + Dark 25개 토큰)
[ ] res/values/themes.xml 생성 (Light, Splash 포함)
[ ] res/values-night/themes.xml 생성 (Dark)
[ ] .claude/CLAUDE.md 생성 (스택, 보안 규칙, 현재 단계 포함)
[ ] 사용자에게 인계 사항 전달 (Play Console, AdMob, Android Studio 절차)
```

---

## 버전 히스토리

| 버전 | 날짜 | 변경 내용 |
|------|------|---------|
| v1.0 | 2026-06-04 | TextReader 프로젝트 경험 기반 최초 작성 |
