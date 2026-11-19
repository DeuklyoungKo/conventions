# conventions

**새 프로젝트를 시작할 때 AI 에게 "준비를 어떻게 하라" 고 알려 주는 가이드**이자,
여러 프로젝트가 **링크로 참조**하는 공통 규약 저장소다. 파일을 복사하지 않는다.

특정 프로젝트 저장소에 두면 그 저장소의 수명에 규약이 종속되므로 독립 저장소로 분리했다.

## 🚀 새 프로젝트를 시작한다면 — [`START_HERE.md`](./START_HERE.md)

AI 에게 이렇게 말하면 된다.

```
https://github.com/DeuklyoungKo/conventions 를 검토해서 이 프로젝트의 시작 준비를 해줘.
```

`START_HERE.md` 가 그 한 마디에 대한 **실행 순서**다 — 무엇을 먼저 묻고, 무엇을
**사람이** 해야 하고(테마·스캐폴딩), `.gitignore` 를 언제 두고, 어떤 문서를 만들고,
`CLAUDE.md` 에 무엇을 적는가.

## ⚠️ 이것은 가이드다 — 바꿔 써도 된다

번호·파일명·절차는 **매번 고민하지 않으려고 미리 정해 둔 기본값**이다. 프로젝트 성격에
맞게 바꾸면 된다(실제로 한 게임 프로젝트는 `3`·`4` 를 다르게 쓴다 —
[`0_DOC_CONVENTION.md` §1.4](./0_DOC_CONVENTION.md)).

바꾸지 말아야 하는 것은 **넷뿐**이다 — 현재값은 `CLAUDE.md` 만 소유 · 「현재 작업 상태」는
스냅샷 · 비밀값은 커밋 금지 · 사람 소유 파일(`dev.md`)은 AI 가 고치지 않는다
([`START_HERE.md` §6](./START_HERE.md)).

## 구성

| 경로 | 내용 |
|---|---|
| [`START_HERE.md`](./START_HERE.md) | 🚀 **새 프로젝트 시작 절차** — 묻기 → 사람이 할 일 → `.gitignore` → 문서 골격 → `CLAUDE.md` → 검증 명령 → 첫 커밋 |
| [`0_DOC_CONVENTION.md`](./0_DOC_CONVENTION.md) | 문서 관리 규약 — SSOT 원칙, 문서 구성(**기본값**), `dev.md` 의 용도, 작업 단위 기록 문서, Notion↔GitHub 경계 |
| [`1_MODEL_SELECTION_CLAUDE_CODE.md`](./1_MODEL_SELECTION_CLAUDE_CODE.md) | **Claude Code 전용** — 업무별 모델·추론량 배치표(A~K), 지정 방법, 컨텍스트 분리. §2·§5·§6 은 도구 무관 원칙이라 다른 에이전트에도 옮겨 쓸 수 있다 |
| [`2_DEV_PROTOCOL.md`](./2_DEV_PROTOCOL.md) | 개발·검증 프로토콜 — **완료의 정의**, Builder/QA 2중 피드백 루프, 단정 규율(**단정이 비껴가는 축 8가지**), 안전 가드레일 |
| [`3_WORKFLOW.md`](./3_WORKFLOW.md) | 작업 흐름 — **요청 → 머지까지의 단계와 순서**. 보드에 올리기 전 사실 확인, 묻는 자리 넷, **반증은 커밋 뒤에**, QA 를 언제 멈추는가 |
| [`data/`](./data/) | 벤더별 모델·API 레퍼런스 (가격·한도·모델 ID). **기준일 필수** |
| [`templates/`](./templates/) | 각 PC `~/.claude/`에 들어가는 파일의 **원본** |

## 규약 적용 방법

새 프로젝트의 `CLAUDE.md`에 아래를 넣는다. **파일을 복사하지 않는다.**

```
## 문서 관리 체계
> 📘 규칙 원문: https://github.com/DeuklyoungKo/conventions/blob/main/0_DOC_CONVENTION.md
> SSOT 원칙·갱신 트리거·경로 표기·안티패턴은 그 문서가 소유한다. 여기서 반복하지 않는다.

**이 프로젝트의 문서 구성**
- (이 프로젝트에 실제로 있는 문서와 각각의 상태만 적는다)
```

**모델·추론량 배치**·**개발·검증 프로토콜**·**작업 흐름**도 같은 방식으로 링크한다 — 각각
`1_MODEL_SELECTION_CLAUDE_CODE.md` §8, `2_DEV_PROTOCOL.md` §7, `3_WORKFLOW.md` §12 에 붙여 넣을 문구가 있다.

또는 AI에게 이렇게 지시한다.

```
https://github.com/DeuklyoungKo/conventions/blob/main/0_DOC_CONVENTION.md
읽고 이 방식으로 문서를 정리해줘.
```

## 새 PC 세팅

```bash
git clone git@github.com:DeuklyoungKo/conventions.git
cd conventions          # 아래 명령은 모두 저장소 루트 기준이다

mkdir -p ~/.claude
cp templates/CLAUDE.global.md ~/.claude/CLAUDE.md
cp templates/android-vibe-coding-sop.md ~/.claude/
```

복사한 뒤 **`~/.claude/CLAUDE.md` 의 `MACHINE-SPECIFIC` 블록만** 그 PC의 실제 값으로 채운다.
⚠️ 드라이브 문자나 절대경로를 적지 않는다 — 작업 폴더는 폴더명(`Work` / `Work_Gon`)으로만.

상세는 [`templates/README.md`](./templates/README.md) 참조.
