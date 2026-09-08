# conventions

프로젝트 공통 규약 저장소. 여러 프로젝트가 **링크로 참조**하며, 파일을 복사하지 않는다.

특정 프로젝트 저장소에 두면 그 저장소의 수명에 규약이 종속되므로 독립 저장소로 분리했다.

## 구성

| 경로 | 내용 |
|---|---|
| [`0_DOC_CONVENTION.md`](./0_DOC_CONVENTION.md) | 문서 관리 규약 — SSOT 원칙, 문서 구성, Notion↔GitHub 경계 |
| [`templates/`](./templates/) | 각 PC `~/.claude/`에 들어가는 파일의 백업본 |

## 규약 적용 방법

새 프로젝트의 `CLAUDE.md`에 아래를 넣는다. **파일을 복사하지 않는다.**

```
## 문서 관리 체계
> 📘 규칙 원문: https://github.com/DeuklyoungKo/conventions/blob/main/0_DOC_CONVENTION.md
> SSOT 원칙·갱신 트리거·경로 표기·안티패턴은 그 문서가 소유한다. 여기서 반복하지 않는다.

**이 프로젝트의 문서 구성**
- (이 프로젝트에 실제로 있는 문서와 각각의 상태만 적는다)
```

또는 AI에게 이렇게 지시한다.

```
https://github.com/DeuklyoungKo/conventions/blob/main/0_DOC_CONVENTION.md
읽고 이 방식으로 문서를 정리해줘.
```

## 새 PC 세팅

```bash
git clone git@github.com:DeuklyoungKo/conventions.git
mkdir -p ~/.claude
cp conventions/templates/CLAUDE.global.md ~/.claude/CLAUDE.md
cp conventions/templates/android-vibe-coding-sop.md ~/.claude/
```

상세는 [`templates/README.md`](./templates/README.md) 참조.
