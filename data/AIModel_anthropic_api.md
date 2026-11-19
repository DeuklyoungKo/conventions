# Anthropic (Claude) 모델 스펙·가격·추론량 요약

> 📅 **기준일: 2026-11-19** — 가격·모델 라인업은 바뀐다. 쓰기 전에 아래 공식 문서로 다시 확인한다.
>
> 출처: [Models overview](https://platform.claude.com/docs/en/about-claude/models/overview) ·
> [Choosing a model](https://platform.claude.com/docs/en/about-claude/models/choosing-a-model) ·
> [Claude Code model config](https://code.claude.com/docs/en/model-config) ·
> [Sub-agents](https://code.claude.com/docs/en/sub-agents)

> 📌 **여기는 사실만 둔다.** "어떤 업무에 어떤 모델을 쓸 것인가" 라는 **판단**은
> [`1_MODEL_SELECTION_CLAUDE_CODE.md`](../1_MODEL_SELECTION_CLAUDE_CODE.md)가 소유한다.

---

## 1. 현재 라인업

| | **Fable 5.2** | **Opus 5.5** | **Sonnet 5.5** | **Haiku 5.5** |
|---|---|---|---|---|
| 모델 ID | `claude-fable-5-2` | `claude-opus-5-5` | `claude-sonnet-5-5` | `claude-haiku-5-5` |
| 공식 용도 | 까다로운 추론 + 긴 호흡 에이전트 | 장시간 에이전트 코딩·지식 작업 | 속도와 지능의 최적 조합 | 대량·저지연 — 분류·추출·라우팅, **서브에이전트 작업** |
| 지연 | Moderate | Moderate | Fast | Fastest |
| **입력** (per MTok) | **$8** | **$4** | **$2** | **$0.10** 부터 |
| **출력** (per MTok) | **$40** | **$20** | **$10** | **$0.50** 부터 |
| API 기본 effort | `high` | `medium` | `high` | `medium` |
| 컨텍스트 | 1M tokens | 1M tokens | 1M tokens | 1M tokens |
| 최대 출력 | 128K tokens | 128K tokens | 128K tokens | 128K tokens |

* **출력 기준 비용 사다리 `80 : 40 : 20 : 1`** (Fable : Opus : Sonnet : Haiku).
  **Fable 은 Opus 의 정확히 2배**, **Haiku 는 Opus 의 1/40**.
* 제한 공개 모델로 **Claude Mythos 5.2**(`claude-mythos-5-2`)가 있다 — 인증된 조직만.
* 이전 세대(Opus 4.5 / Sonnet 4.5 / Haiku 4.5 등)는 컨텍스트 **200K**, 최대 출력 **64K**.

### 할인

| 항목 | 할인 |
|---|---|
| Batch API | **50%** |
| 프롬프트 캐시 읽기 | 입력가의 **10%** (Fable 5.2는 2.5%, Opus 5.5·Sonnet 5.5는 5%) |

---

## 2. 추론량(effort) — Adaptive thinking

단계는 **`low` · `medium` · `high` · `xhigh` · `max`** 이고 5.x 세대 전 모델이 지원한다.

* 모델이 effort에 따라 생각량을 **스스로 정한다**(Adaptive thinking).
* 수동 모드(`thinking.type: "enabled"` + `budget_tokens`)는 Opus 4.6·Sonnet 4.6에서
  **deprecated**, 이후 모델은 받지 않는다.
* ⚠️ **기본값이 맥락마다 다르다.** API 기본값은 위 표와 같고, **Claude Code 기준으로는
  5.x 모델이 모두 `medium`** 으로 보인다(요약 기반, 원문 미확인).

> 🔴 **공식 지침: "모델을 바꾸기보다 effort를 조절하는 편이 흔히 더 나은 조절 수단이다."**

---

## 3. 모델 선택에 대한 공식 권장

* **"어느 모델을 쓸지 모르겠으면 대부분의 작업은 Opus 5.5로 시작하라."**
* **효율 우선 경로**: Haiku 5.5로 시작해 부족할 때만 올린다 (프로토타이핑·저지연·대량 단순 작업)
* **능력 우선 경로**: Opus 5.5로 시작해 **부족하면** Fable 5.2로 간다
* 여러 모델을 섞는 전략(executor/advisor, orchestrator/worker)도 공식 문서가 소개한다

---

## 4. Claude Code 에서의 지정 (요약)

자세한 것은 [`1_MODEL_SELECTION_CLAUDE_CODE.md`](../1_MODEL_SELECTION_CLAUDE_CODE.md) §4.

**우선순위** — 위가 강하다.

1. 세션 중 `/model <alias>`
2. 시작 시 `claude --model <alias>`
3. 환경 변수 `ANTHROPIC_MODEL`
4. 설정 파일의 `model` 필드
5. 새 세션 기본값 `ANTHROPIC_DEFAULT_MODEL`

**별칭**: `fable` · `opus` · `sonnet` · `haiku` · `best`(=opus) · `default` ·
`sonnet[1m]` · `opus[1m]` · **`opusplan`**(계획 단계는 opus, 실행은 sonnet)

**서브에이전트 모델 우선순위**: 호출 시 지정 → 정의의 `model` →
`CLAUDE_CODE_SUBAGENT_MODEL` → 부모 대화의 모델

**주요 환경 변수**: `ANTHROPIC_MODEL` · `ANTHROPIC_DEFAULT_MODEL` ·
`ANTHROPIC_DEFAULT_{OPUS,SONNET,HAIKU,FABLE}_MODEL` ·
`CLAUDE_CODE_SUBAGENT_MODEL`(+`_FORCE`) · `CLAUDE_CODE_EFFORT_LEVEL` ·
`CLAUDE_CODE_MAX_CONTEXT_TOKENS`

---

## 5. 용어

| 약어 | 원어 | 뜻 |
|---|---|---|
| **MTok** | Million Tokens | 100만 토큰. 가격 표기 단위 |
| **effort** | — | 추론량 단계. 모델이 얼마나 생각할지 |
| **Adaptive thinking** | — | effort에 따라 생각량을 모델이 스스로 정하는 방식 |
| **Batch API** | — | 비동기 일괄 처리. 50% 저렴하고 지연이 길다 |
| **프롬프트 캐시** | Prompt Caching | 같은 앞부분을 재사용해 입력 비용을 크게 낮추는 기능 |
