# templates

각 PC의 `~/.claude/`에 들어가는 파일들의 **백업본**이다.

`~/.claude/`는 컴퓨터별 환경 설정이라 자동 동기화하지 않는다. 머신마다 경로·드라이브·설치 도구가 달라 충돌하기 때문이다. 대신 여기에 템플릿으로 보관하고, 새 PC에서 복사해 쓴다.

## 파일

| 템플릿 | 배치 위치 | 역할 |
|---|---|---|
| `CLAUDE.global.md` | `~/.claude/CLAUDE.md` | AI 코딩 행동 지침. 매 세션 자동 로드 |
| `android-vibe-coding-sop.md` | `~/.claude/android-vibe-coding-sop.md` | Android 프로젝트 착수 절차 |

**둘은 한 쌍이다.** `CLAUDE.global.md`의 5-B 섹션이 SOP 파일을 참조하므로 함께 복사한다.

## 새 PC 세팅

```bash
mkdir -p ~/.claude
cp templates/CLAUDE.global.md ~/.claude/CLAUDE.md
cp templates/android-vibe-coding-sop.md ~/.claude/
```

복사 후 **「글로벌 Claude Code 설정 > 실행 환경」 섹션을 새 PC에 맞게 고친다.** OS·WSL 여부·프로젝트 경로가 머신마다 다르다.

작업 폴더 분류(`Work` / `Work_Gon`)는 폴더명만으로 판정하므로 드라이브가 달라도 수정할 필요가 없다.

## 갱신 규칙

**원본은 항상 `~/.claude/`의 파일이다.** 여기는 사본이다.

지침을 바꿀 때는 파일을 먼저 고치고, **그 자리에서 바로** 동기화한다. "나중에"는 반드시 누락된다.

```bash
cp ~/.claude/CLAUDE.md ~/conventions/templates/CLAUDE.global.md
cd ~/conventions && git add -A && git commit -m "chore: 전역 CLAUDE.md 동기화 — <무엇을 바꿨는지>" && git push
```

## 어긋남 점검

연 1회 또는 의심될 때 실행한다. 출력이 없으면 동일한 것이다.

```bash
diff ~/.claude/CLAUDE.md ~/conventions/templates/CLAUDE.global.md
diff ~/.claude/android-vibe-coding-sop.md ~/conventions/templates/android-vibe-coding-sop.md
```
