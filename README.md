# conventions

프로젝트 공통 규약 저장소. 여러 프로젝트가 **링크로 참조**하며, 파일을 복사하지 않는다.

특정 프로젝트 저장소에 두면 그 저장소의 수명에 규약이 종속되므로 독립 저장소로 분리했다.

## 구성

| 경로 | 내용 |
|---|---|
| [`0_DOC_CONVENTION.md`](./0_DOC_CONVENTION.md) | 문서 관리 규약 — SSOT 원칙, 문서 구성, 작업 단위 기록 문서, Notion↔GitHub 경계 |
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
