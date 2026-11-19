# templates

각 PC의 `~/.claude/`에 들어가는 파일들의 **원본**이다.

`~/.claude/` 자체는 자동 동기화하지 않는다 — 머신마다 경로·드라이브·설치 도구가 달라 충돌하기 때문이다. 대신 **규칙은 여기서 원본으로 관리**하고, PC마다 다른 부분만 각 PC가 따로 채운다.

## 파일

| 템플릿 | 배치 위치 | 역할 |
|---|---|---|
| `CLAUDE.global.md` | `~/.claude/CLAUDE.md` | AI 코딩 행동 지침. 매 세션 자동 로드 |
| `android-vibe-coding-sop.md` | `~/.claude/android-vibe-coding-sop.md` | Android 프로젝트 착수 절차 |

**둘은 한 쌍이다.** `CLAUDE.global.md`의 5-B 섹션이 SOP 파일을 참조하므로 함께 복사한다.

---

## 🔴 무엇이 원본인가 — 두 조각으로 나눠 본다

예전에는 *"원본은 항상 `~/.claude/`의 파일"* 이라고 적어 두고 동시에 *"복사 후 「실행 환경」 섹션을 새 PC에 맞게 고친다"* 고 했다. **이 둘은 같이 설 수 없다.** 각 PC가 자기 값으로 고친 뒤 `~/.claude/` → 템플릿 방향으로 동기화하면, **마지막에 동기화한 PC의 머신 값이 템플릿을 덮는다.** 그리고 다음 PC가 그걸 받아 **자기 환경을 잘못 설명하는 지침**을 읽게 된다. 실제로 그렇게 어긋나 있었다.

그래서 조각을 나눈다.

| 조각 | 원본 | 동기화 |
|---|---|---|
| **규칙 전부** (1~6절, SOP, CLI·MCP 방침 등) | **이 저장소의 템플릿** | 템플릿 → 각 PC |
| **`실행 환경` 블록** (`MACHINE-SPECIFIC` 주석 사이) | **각 PC의 `~/.claude/CLAUDE.md`** | **하지 않는다** |

> 규칙을 바꾸고 싶으면 **템플릿을 고치고 커밋**한다. PC 파일을 먼저 고치지 않는다.
> PC 파일은 "템플릿 + 그 PC의 실행 환경" 일 뿐이다.

---

## 새 PC 세팅

아래 명령은 **이 저장소의 루트에서** 실행한다. 저장소를 어디에 클론했든 상관없도록 상대경로만 쓴다.

```bash
mkdir -p ~/.claude
cp templates/CLAUDE.global.md ~/.claude/CLAUDE.md
cp templates/android-vibe-coding-sop.md ~/.claude/
```

복사한 뒤 **`~/.claude/CLAUDE.md`의 `MACHINE-SPECIFIC` 블록을 그 PC의 실제 값으로 채운다.**

- OS와 기본 셸이 무엇인지 (PowerShell인지 bash인지)
- 어떤 보조 도구가 **실제로 설치돼 있는지**
- ⚠️ **드라이브 문자나 절대경로를 적지 않는다.** 작업 폴더는 폴더명(`Work` / `Work_Gon`)으로만 적는다

> 🔴 이 블록이 그 PC와 다르면 **AI가 틀린 전제로 움직인다.** "모든 명령을 Linux에서 실행"이라 적혀 있는데 실제로는 PowerShell로 돌아가고 있던 적이 있다.

---

## 규칙을 바꿀 때

```bash
# 1) 이 저장소의 템플릿을 고친다
#    (편집기로 templates/CLAUDE.global.md 수정)

# 2) 커밋·푸시
git add -A && git commit -m "chore: 전역 지침 수정 — <무엇을 바꿨는지>" && git push

# 3) 각 PC에서 받아 적용 — MACHINE-SPECIFIC 블록만 자기 값으로 다시 채운다
git pull
cp templates/CLAUDE.global.md ~/.claude/CLAUDE.md
```

**"나중에 동기화"는 반드시 누락된다.** 고친 그 자리에서 커밋한다.

---

## 어긋남 점검

연 1회 또는 의심될 때, **이 저장소 루트에서** 실행한다.

```bash
# MACHINE-SPECIFIC 블록을 뺀 나머지가 같은지 본다 (출력이 없으면 동일)
sed '/MACHINE-SPECIFIC:BEGIN/,/MACHINE-SPECIFIC:END/d' ~/.claude/CLAUDE.md > /tmp/a.md
sed '/MACHINE-SPECIFIC:BEGIN/,/MACHINE-SPECIFIC:END/d' templates/CLAUDE.global.md > /tmp/b.md
diff /tmp/a.md /tmp/b.md

diff ~/.claude/android-vibe-coding-sop.md templates/android-vibe-coding-sop.md
```

차이가 나오면 **템플릿 쪽이 옳다**(규칙의 원본이므로). 그 PC의 파일을 다시 받는다.

> 블록을 뺀 나머지에 차이가 없는데 그 PC의 동작이 이상하다면, 그때는 `MACHINE-SPECIFIC` 블록이 그 PC를 잘못 설명하고 있는지 본다.
