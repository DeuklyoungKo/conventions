# CLAUDE.md

Behavioral guidelines to reduce common LLM coding mistakes. Merge with project-specific instructions as needed.

**Tradeoff:** These guidelines bias toward caution over speed. For trivial tasks, use judgment.

## 1. Think Before Coding

**Don't assume. Don't hide confusion. Surface tradeoffs.**

Before implementing:
- State your assumptions explicitly. If uncertain, ask.
- If multiple interpretations exist, present them - don't pick silently.
- If a simpler approach exists, say so. Push back when warranted.
- If something is unclear, stop. Name what's confusing. Ask.

## 2. Simplicity First

**Minimum code that solves the problem. Nothing speculative.**

- No features beyond what was asked.
- No abstractions for single-use code.
- No "flexibility" or "configurability" that wasn't requested.
- No error handling for impossible scenarios.
- If you write 200 lines and it could be 50, rewrite it.

Ask yourself: "Would a senior engineer say this is overcomplicated?" If yes, simplify.

## 3. Surgical Changes

**Touch only what you must. Clean up only your own mess.**

When editing existing code:
- Don't "improve" adjacent code, comments, or formatting.
- Don't refactor things that aren't broken.
- Match existing style, even if you'd do it differently.
- If you notice unrelated dead code, mention it - don't delete it.

When your changes create orphans:
- Remove imports/variables/functions that YOUR changes made unused.
- Don't remove pre-existing dead code unless asked.

The test: Every changed line should trace directly to the user's request.

## 4. Goal-Driven Execution

**Define success criteria. Loop until verified.**

Transform tasks into verifiable goals:
- "Add validation" → "Write tests for invalid inputs, then make them pass"
- "Fix the bug" → "Write a test that reproduces it, then make it pass"
- "Refactor X" → "Ensure tests pass before and after"

For multi-step tasks, state a brief plan:
```
1. [Step] → verify: [check]
2. [Step] → verify: [check]
3. [Step] → verify: [check]
```

Strong success criteria let you loop independently. Weak criteria ("make it work") require constant clarification.

---

## 5. Project Initialization (Vibe Coding)

**Set up the foundation manually. AI coding starts after the scaffold is ready.**

> ⚠️ **Do NOT ask AI to handle project initialization** (folder structure, theme config, scaffold).
> Complete these steps yourself first. AI coding begins only after the scaffold is in place.

**이 원칙은 프로젝트 성격에 따라 유연하게 적용한다.**

규칙의 취지는 "**사람이 결정해야 할 선택을 AI가 임의로 정하지 못하게**" 하는 것이다. 테마 색상, 컴포넌트 라이브러리, 폴더 구조처럼 되돌리기 어렵고 취향이 개입하는 결정이 그 대상이다.

**결정할 것이 없는 프로젝트는 AI가 스캐폴딩해도 된다.**

| 상황 | 적용 |
| :--- | :--- |
| UI가 있는 프론트엔드 | 5-A 절차를 사람이 직접 수행 |
| Android 앱 | 5-B 절차를 사람이 직접 수행 |
| **UI 없는 API·CLI·스크립트·배치** | AI가 스캐폴딩해도 됨 (테마·컴포넌트 선택 자체가 없음) |
| 기존 프로젝트에 기능 추가 | 해당 없음 |

판단 기준: **"이 초기화 과정에서 사람이 골라야 할 선택지가 있는가?"** 없으면 AI에게 맡긴다.
예외를 적용했다면 그 프로젝트 `CLAUDE.md`의 "최근 결정 사항"에 이유를 남긴다.

---

### 5-0. 모든 프로젝트 공통 — `.gitignore` 먼저

**스캐폴딩 직후, 코드를 한 줄이라도 쓰기 전에 `.gitignore`를 세팅한다.** 비밀값이 한 번 커밋되면 히스토리에서 지우기 어렵다.

프로젝트 성격에 맞는 항목을 넣되, 아래는 반드시 포함한다.

- **비밀값 파일** — `.env*` (Node), `local.properties` (Android), `*.pem`, `credentials.json` 등. 템플릿(`.env.example`)만 예외로 커밋
- **의존성·빌드 산출물** — `node_modules/`, `.next/`, `build/`, `dist/`
- **OS·에디터** — `.DS_Store`, `Thumbs.db`, `.idea/`

세팅 후 **실제로 동작하는지 확인한다.**

```bash
echo "TEST=x" > .env.local && git status --short   # .env.local이 목록에 없어야 정상
rm .env.local
```

`.env.example` 같은 템플릿을 함께 만들어 **어떤 변수가 필요한지와 발급 방법**을 주석으로 남긴다.

> ⚠️ 커밋 전 `git status`에 비밀값 파일이 보이면 즉시 중단한다.

---

### 5-A. Web Frontend (Next.js / React)

Before starting AI-assisted coding on a new frontend project:

1. Go to https://ui.shadcn.com/create and design your theme
   - Component Library: **Base UI** (Radix UI is no longer actively maintained)
   - Icon Library: **Hugeicons** (recommended over Lucide for new projects)
   - Set base color, accent theme, font, and radius to taste
2. Click **Create Project** → select framework (Next.js / TanStack / Vite) → copy the command
3. Run the copied command in terminal — it scaffolds the project with your theme applied automatically
4. Write `CLAUDE.md` / `GEMINI.md` based on the generated project structure
5. **Then** start AI coding (vibe coding)

---

### 5-B. Android 앱 (Kotlin)

Before starting AI-assisted coding on a new Android project:

1. **Android Studio**에서 프로젝트 직접 생성
   - Template: **Empty Views Activity**
   - Language: **Kotlin**
   - Package name: 결정 후 직접 입력 (예: `com.myapp.name`)
   - Min SDK: **API 26** (Android 8.0, 전체 기기 95%+ 커버)
2. **Material Theme Builder**에서 Seed 색상 결정 → XML 추출
   - 접속: https://m3.material.io/theme-builder
   - Seed 색상 선택 → Export → Android Views (XML)
   - `colors.xml`, `themes.xml`, `values-night/themes.xml` 프로젝트에 복붙
   - 또는 AI에게 Seed 색상만 알려주면 파일 직접 생성 가능
3. `gradle/libs.versions.toml` 의존성 설정 (Room, Coroutines, AdMob 등)
4. `AndroidManifest.xml`에 AdMob App ID 추가, `local.properties`에 광고 Unit ID 추가
5. 프로젝트 루트에 `.claude/CLAUDE.md` 작성 (스택, 아키텍처, 태스크 체크리스트 위치)
6. **Then** start AI coding

**Android 프로젝트 핵심 규칙:**
- 광고 ID(`ADMOB_*`)는 반드시 `local.properties`에만 저장 — git 커밋 금지
- `local.properties`는 `.gitignore`에 포함되어 있는지 반드시 확인
- SAF(Storage Access Framework) 사용 시 `takePersistableUriPermission()` 누락 주의
- TTS 백그라운드 재생은 반드시 `ForegroundService`로 구현 (Android 8.0+ 정책)

> 📋 **전체 상세 절차**: `~/.claude/android-vibe-coding-sop.md` 참조
> 새 Android 프로젝트 시작 시 이 SOP를 따라 Phase 0~6을 자동 처리한다.

## 6. Apply Skills Before Coding (skills.sh)

**Once the project overview is ready, find and apply relevant skills before writing a single line of code.**

Skills are `SKILL.md` files that give AI agents domain-specific expertise. Install once per project — the AI will automatically reference them during relevant tasks.

### Installation
```bash
# Step 1: Install find-skills first (lets the AI discover relevant skills itself)
npx skills add vercel-labs/agent-skills

# Step 2: Run find-skills inside the project
# Tell Claude: "Run find-skills and apply any relevant skills to this project"
```

### Workflow
```
1. Project overview finalized
       ↓
2. npx skills add vercel-labs/agent-skills   # installs find-skills + core skills
       ↓
3. Ask Claude to run find-skills             # AI searches and installs relevant skills
       ↓
4. Verify .claude/skills/ folder contents
       ↓
5. Start AI coding with skills active
```

### Trusted skill sources
- `vercel-labs/agent-skills` — React best practices, web design guidelines
- `anthropics/skills` — frontend-design, skill-creator
- `remotion-dev/skills` — Remotion video production

> ⚠️ Only install skills from verified publishers. Review SKILL.md content on GitHub before installing unknown packages.
> Remove unused skills — accumulated skill files waste AI context and can cause unexpected behavior.

---

**These guidelines are working if:** fewer unnecessary changes in diffs, fewer rewrites due to overcomplication, and clarifying questions come before implementation rather than after mistakes.

---

# 📜 서비스 개발 프로토콜 및 비즈니스 규정 (SOP)

이 문서는 **Gon(사용자)**과 **Suit(OpenClaw AI 비서)** 간의 협업 체계 및 프로젝트 관리 표준 운영 절차(Standard Operating Procedure)를 정의합니다.

---

## 1. 프로젝트 분류 및 환경 정의

**분류는 업무의 성격으로 판정한다.** 사용하는 클라우드로 역추론하지 않는다.

* **공식 프로젝트 (Official):** 회사의 공식 업무. 인프라는 **주로 AWS**를 사용하는 편이다.
* **개인 프로젝트 (Private):** 외부(회사 등)에 노출되지 않는 개인 비즈니스. 인프라는 프로젝트마다 다르다.

> ⚠️ 위 인프라 표기는 **경향일 뿐 판정 조건이 아니다.** "AWS를 안 쓰니 Private", "GCP니까 Private" 식의 역추론 금지.
> 예: 고앤슈트(gonsuit)는 Private이지만 Vercel + Supabase + Cloudflare 구성이다.

**식별 방법:** 각 저장소 **`CLAUDE.md` 최상단 "프로젝트 개요"** 에 분류를 명시한다. 작업 시작 시 이를 최우선 확인하여 인프라·보안 혼선을 방지한다.

**작업 폴더 분류** — 드라이브 문자는 컴퓨터마다 다르므로 **폴더명만으로 판정**한다:

| 경로에 포함된 폴더명 | 분류 |
| :--- | :--- |
| `Work` | **Official** |
| `Work_Gon` | **Private** |

> 예: `E:\Work_Gon\260908_stock`, `D:\Work_Gon\...`, `C:\dev\Work\...` 모두 동일하게 판정한다.
> 두 폴더명이 모두 없으면 **분류를 추측하지 말고 사용자에게 확인**한다.

---

## 2. 문서 관리 체계 (Documentation Stack)

> 📘 **규약 원문 (SSOT)**: https://github.com/DeuklyoungKo/conventions/blob/main/0_DOC_CONVENTION.md
> 문서 구성(`1_PRD` · `2_PDP` · `3_DesignGuide` · `4_LRP` · `CLAUDE.md` · `dev.md`), SSOT 원칙, 갱신 트리거,
> 경로 표기 규칙, Notion↔GitHub 경계, 안티패턴은 **모두 그 문서가 소유한다. 여기서 반복하지 않는다.**
>
> 새 프로젝트에 이 체계를 적용하거나 기존 프로젝트를 정리할 때는 **먼저 그 URL을 읽고 따른다.**
> 레퍼런스 구현은 고앤슈트 저장소의 `CLAUDE.md`를 참조한다.

**목적**: 작업 컴퓨터가 바뀌어도 AI가 현재 상태와 다음 할 일을 즉시 파악할 수 있게 한다. 따라서 모든 기준 문서는 **git으로 추적되는 저장소 파일**이어야 한다.

| 단계 | 관리 위치 |
| :--- | :--- |
| **기획** | Claude Desktop에서 수행 후 **Notion**에 기록 |
| **설계·실행** | **GitHub** 저장소 (`CLAUDE.md`가 현재값 SSOT) |

> ⚠️ 규약 문서를 각 프로젝트에 **복사하지 않는다.** 원본은 conventions 저장소 하나뿐이며,
> 다른 프로젝트는 자기 `CLAUDE.md`의 "문서 관리 체계" 섹션에서 위 URL을 **링크로 가리킨다.**
> (컴퓨터별 환경 설정 `~/.claude/`도 동기화하지 않는다. **규약만 문서로 공유한다.**)

---

# 글로벌 Claude Code 설정

## 실행 환경

> ⚠️ **이 섹션은 머신 종속이다.** 새 PC에 복원했다면 이 부분을 그 PC에 맞게 고친다.

- **OS**: Windows 10/11 + WSL2 (Ubuntu) + Docker Desktop
- **프로젝트 파일**: Windows 측 `Work` / `Work_Gon` 폴더 (드라이브 문자는 PC마다 다름)
- **CLI**: PowerShell 기본. Linux 전용 도구가 필요할 때만 WSL 사용

**WSL에서 프로젝트에 접근할 때**

```bash
cd /mnt/d/Work_Gon/<프로젝트>   # 드라이브가 D인 경우
```

`/mnt/`를 경유하는 파일 I/O는 느리다. **`npm install`·빌드처럼 파일을 많이 건드리는 작업은 PowerShell에서 직접 실행**한다. WSL은 `jq`·`rg` 같은 Linux 도구가 필요할 때만 쓴다.

프로젝트를 WSL `/home/`으로 옮기면 I/O는 빨라지지만, Windows 쪽 편집기·도구와의 연결이 불편해진다. **현재는 Windows 폴더를 기준으로 한다.**

---

## 사용 가능한 CLI 도구

| 도구 | 용도 | 예시 |
|------|------|------|
| `gh` | GitHub 작업 (PR, 이슈, API) | `gh pr list`, `gh issue create`, `gh api /repos/:owner/:repo` |
| `curl + jq` | HTTP 요청 및 JSON 파싱 | `curl -s URL \| jq '.key'` |
| `docker` | 컨테이너 관리 | `docker ps`, `docker compose up -d` |
| `kubectl` | Kubernetes 클러스터 관리 | `kubectl get pods -n namespace`, `kubectl logs` |
| `aws` | AWS 리소스 관리 | `aws s3 ls`, `aws ec2 describe-instances` |
| `psql` / `mysql` | 데이터베이스 직접 쿼리 | `psql -U user -d dbname -c "SELECT ..."` |
| `find` / `rg` | 파일 검색 | `rg "패턴" --type py`, `find . -name "*.md"` |

> **Windows 호환 주의**
> - `jq`: WSL2 내 `sudo apt install jq`로 설치 (Windows 바이너리와 별개)
> - `curl`: WSL2 기본 내장, Windows의 `curl.exe`와 혼동 주의

---

## MCP vs CLI 선택 기준

### CLI 우선 사용 (단발성·조회 작업)
단순 조회, 파일 읽기, 단일 API 호출처럼 **명령 하나로 끝나는 작업**은 CLI 사용.

```bash
# 예: PR 목록 확인 → gh CLI
gh pr list --state open

# 예: REST API 호출 → curl + jq
curl -s https://api.example.com/data | jq '.results[]'
```

### MCP 사용 (연속 작업·판단 필요)
여러 단계를 거쳐야 하거나, Claude가 **컨텍스트를 유지하며 판단**해야 할 때 MCP 사용.

```
예: "이슈 내용 읽고 → 관련 코드 분석 → PR 자동 생성" 같은 연속 워크플로우
```

---

## MCP 서버 운영 원칙

### 유지 대상 (CLI 대체 불가)
| MCP 서버 | 유지 이유 |
|----------|-----------|
| **Notion** | 공식 API가 복잡하고 페이지 구조 탐색이 비정형적 |
| **Google Calendar** | OAuth 토큰 관리 부담, 이벤트 컨텍스트 유지 필요 |
| **Gmail** | 스레드 파악·판단이 필요한 연속 작업 |
| **Slack** (사용 시) | 채널 컨텍스트 유지, 멘션 파악 등 |

### 비활성화 검토 대상 (CLI로 충분)
| MCP 서버 | 대체 CLI |
|----------|----------|
| GitHub MCP | `gh` CLI |
| HTTP/API MCP | `curl + jq` |
| AWS MCP | `aws` CLI |
| Kubernetes MCP | `kubectl` |
| Docker MCP | `docker` CLI |
| Database MCP | `psql` / `mysql` |
| 파일 검색 MCP | `find`, `rg` |

> **정리 기준**: `/mcp`로 현재 목록 확인 후, **최근 1개월 미사용** 서버부터 비활성화

---

## 작업 규칙

- CLI로 가능한 작업에 MCP를 사용하지 않는다
- 민감한 정보(API 키, 비밀번호)는 환경변수로 관리, 코드에 하드코딩 금지
- 에러 발생 시 즉시 원인 파악 후 보고, 임의로 우회하지 않는다
- 대규모 파일 변경 전 반드시 확인 요청
