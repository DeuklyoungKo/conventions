# 5. RPG 밸런스 설계 가이드

> **게임에 무관한 보편 가이드다.** 특정 프로젝트의 수치·결정은 여기 적지 않는다 —
> 그것은 각 저장소의 `CLAUDE.md` 와 번호 문서가 소유한다.
>
> 이 문서는 **출처를 직접 읽어 확인한 것**으로만 쓴다. 각 항목에 등급을 붙인다:
> 🟢 공식·1차(개발사 문서·개발자 발언) · 🟡 비공식(커뮤니티·언론·팬 전사본) ·
> ⚠️ 확인하지 못함.
>
> ⚠️ **이 파일은 여기 하나만 둔다 — 복사하지 않는다.** 다른 저장소는 링크로 가리킨다.

---

## 0. 쓰는 법

밸런스는 "숫자를 잘 고르는 일" 이 아니라 **숫자들의 관계를 먼저 정하는 일**이다.
순서가 있다 — 아래 §1 → §8 이 그 순서다. 뒤 단계부터 손대면 앞 단계가 계속 흔들린다.

| 단계 | 정하는 것 | 안 정하면 생기는 일 |
|--:|:--|:--|
| 1 | **중심 자원** | 무엇이 얼마인지 물을 기준이 없다 |
| 2 | **수치 관계의 종류** | 성장과 보상이 어긋나 중후반이 정체된다 |
| 3 | **비용 곡선** | 어떤 것은 공짜고 어떤 것은 아무도 안 쓴다 |
| 4 | **합성 규칙과 순서** | 수식어를 더할 때마다 설계 안 한 상호작용이 생긴다 |
| 5 | **방어의 형태와 상한** | 피해가 1 이 되거나 무한 방어가 된다 |
| 6 | **장비와 스탯의 결합 방식** | 장비를 바꿔도 체감이 없다 |
| 7 | **아이템이 지닐 축의 수** | 아이템이 "화살표 보고 푸는 산수 문제" 가 된다 |
| 8 | **수치의 자릿수 상한** | 후반에 숫자가 읽히지 않는다 |

---

## 1. 중심 자원을 하나 정한다

> 🟢 Ian Schreiber, 「Game Balance Concepts」 Level 2 (2010, 공개 블로그)
>
> "Numbers in games don't exist in a vacuum. They only have meaning in relation to
> each other."

Schreiber 는 Dragon Warrior 를 예로 든다 — 방어·공격·MP·조우 빈도가 **전부 HP 로
환산된다.** 그리고 이것을 기법으로 명명한다:

> "This is a common technique, making a single resource central to all of the others."

**절차**

1. 게임의 모든 이득을 **하나의 자원**으로 환산할 수 있는지 본다(보통 HP 또는 피해량).
2. 환산표를 적는다 — "방어 1 = HP n", "이동속도 1% = HP n".
3. 그 뒤 새로 들어오는 모든 것에 **"중심 자원으로 얼마인가"** 를 묻는다.

**흔한 실패** — 중심 자원이 사실상 존재하는데 **선언되지 않은** 경우. 그러면 새 수식어의
값을 매길 기준이 없고, 설계자마다 다른 자를 쓴다.

---

## 2. 수치 관계의 종류를 고르고, 섞일 때를 안다

> 🟢 Schreiber, Level 2

교환비가 양에 따라 어떻게 변하는가로 가른다.

| 종류 | 뜻 | 예 |
|:--|:--|:--|
| **identity** | 두 값이 똑같이 움직인다 | 1:1 환전 |
| **linear** | 교환비가 상수다 | MP 5 ↔ HP 50 |
| **exponential** | "하나를 더하면 다른 하나는 곱한다" | 1·2·4·8·16 |
| **triangular** | 차분이 선형이다 | 1·3·6·10·15·21 |

**섞일 때의 규칙**

* 선형 둘이 겹치면 **곱해진다** — 1A→2B 와 1B→5C 가 겹치면 1:10.
* 삼각형 둘은 **서로 상쇄**되어 선형이 될 수 있다.
* 🔴 **"an exponential relationship will dominate a triangular one."**
  지수가 섞이면 다른 것은 결국 무의미해진다.

**절차** — **성장 비용**과 **수확**이 같은 종류인지 본다.
경험치 요구가 지수인데 처치 경험치가 선형이면, 앞은 폭발하고 뒤는 정체된다.
둘 다 선형이거나 둘 다 2차식이면 층마다 고르게 오른다.

**되먹임 경고** (같은 글)

> "this would be a positive feedback loop that would cause the player to gain high
> levels of power very fast."

---

## 3. 비용 곡선 — 값을 매기는 절차

> 🟢 Schreiber, Level 3 "Transitive Mechanics and Cost Curves"
>
> "How do you know how much each resource is worth? That is what we call a **cost curve**."

비용 곡선은 **비용과 이득 사이의 수치 관계**다. 목표는 하나다 —
"We want the costs and benefits to be equal, numerically."

**절차 네 단계**

1. **비용을 넓게 센다** — "any kind of drawback or limitation" 전부.
   재료·시간·쿨다운·위험·기회비용이 모두 비용이다.
2. **전부 하나의 자원으로 환산한다** — "Put everything in terms of the resource cost."
   (+1 공격이 25금이면 +10 짜리 무기는 250금)
3. **한 가지만 하는 물건부터 값을 매긴다** —
   "identify those objects that only do one thing and nothing else."
   그다음 **뺄셈으로** 미지수를 하나씩 분리한다.
4. 조합 효과의 값은 따로따로의 합보다 **클 수도, 작을 수도, 같을 수도** 있다 —
   시너지가 있으면 크고, 상황이 겹치면 작다.

**진단 용어**

| 용어 | 뜻 | 고치는 법 |
|:--|:--|:--|
| **above the curve** | 너무 좋다 | 값을 올리거나 이득을 줄인다 |
| **below the curve** | 너무 약하다 | 값을 내리거나 이득을 늘린다 |
| 🔴 **overpowered** | "I win" 급 | **값으로는 못 고친다 — 이득 자체를 줄여야 한다** |
| **underpowered** | 이미 공짜인데도 안 쓴다 | **이득을 늘려야 한다** |

판정은 간단하다 — "if the costs are less than the benefits, it's too good."
그리고 설계자는 **무엇을 고정하고 무엇을 바꿀지**를 먼저 골라야 한다.

---

## 4. 합성 규칙 — **가산 풀 하나 + 이름 붙인 곱셈 몇 개**

수식어가 수백 개여도 터지지 않게 하는 규칙이다.

> 🟢 Grinding Gear Games 직원(Mark_GGG), 공식 포럼, 2014-04-18
>
> "'increased' signifies that all such modifiers **to the same value** stack additively,
> not simply all modifiers."
>
> 같은 글: "this is an additive modifier, not a multiplicative one, and that
> distinction is important."

> 🟡 "more"/"less" 는 **각각 별도의 곱셈**이라는 것은 공식 포럼의 숙련 플레이어들이
> 2016·2017·2024년에 걸쳐 일관되게 말한다("Each More-type modifier is an entirely
> separate multiplier"). ⚠️ **개발사 공식 진술은 확인하지 못했다.**

**핵심은 두 가지다**

1. **같은 값에 대한 수식어는 한 풀에 더한다.** 그래서 101번째 수식어를 더해도
   **새로운 상호작용이 생기지 않는다.**
2. **곱셈은 소수만, 이름을 붙여서 둔다.** 어떤 것이 곱셈인지 목록으로 적어 둔다.

**🔴 그리고 순서를 함께 정한다 — 이것이 빠지면 규칙이 반쪽이다**

곱셈이 **방어 적용 앞**에 있으면 **방어를 통째로 건너뛴다.**
방어 100 을 공격 101 로 때리면 1 이지만, `101 × 1.5` 로 때리면 51 이다.
→ 곱셈은 **방어 적용 뒤**에 두는 것이 기본값이다. 앞에 둘 이유가 있다면
그 누출량을 **실측해서 적는다.**

**적용 — 새 수식어를 더하기 전에 답을 적는다**

1. 중심 자원 기준으로 얼마인가(§3)
2. **가산 풀인가, 이름 붙인 곱셈인가** — 기본값은 가산 풀
3. 곱셈이면 **방어 적용 앞인가 뒤인가** — 기본값은 뒤

세 질문에 답하지 못하면 그 수식어는 아직 더할 준비가 안 된 것이다.

---

## 5. 방어 — 형태를 고르고 **상한을 먼저 적는다**

> 🟢 Blizzard 공식, The Arreat Summit (디아블로2 매뉴얼)
>
> "Each character has a default maximum resistance of 75%, although certain items
> can raise that number as high as 95%."

같은 문서가 하한도 적는다 — 최저 −100%, 그리고 저항만으로 **완전 면역은 불가능**하다.

**형태별 성질**

| 형태 | 식 | 성질 |
|:--|:--|:--|
| **뺄셈** | `max(1, 공격 − 방어)` | 절벽에 붙이면 **벽이 선다**. 대신 수치대가 좁아져 조금만 어긋나도 1 이 되거나 과잉이 된다 |
| **비율** | `공격 × (1 − 경감률)` | 매끄럽고 넓은 수치대를 허용한다. 대신 **벽이 잘 안 선다** |
| **나눗셈** | `공격 × k / (k + 방어)` | 비율과 같은 성질. 후반 수치 폭주를 흡수한다 |

🔴 **어느 쪽을 쓰든 상한과 하한을 먼저 적는다.** 비율에 상한이 없으면 무적이 나오고,
뺄셈에 하한이 없으면 피해 0 이 나온다. 디아블로2가 **75% / 95% / −100%** 를 명시한
이유가 이것이다.

📌 **"장비가 없으면 못 간다" 를 피해 공식만으로 세우려 하지 않는다.** 전통적인 ARPG 는
그 벽을 **콘텐츠 접근**(지역 입장·난이도 단계)과 **생존**(맞으면 죽는다)으로 세운다.
피해 공식에 벽을 넣으면 수치대가 좁아지고, 거기서 모든 숫자가 아슬아슬해진다.

---

## 6. 장비와 스탯 — **결합 방식이 비중을 정한다**

> 🟢 Blizzard 공식, The Arreat Summit (디아블로2 근접 피해)
>
> ```
> Final_Min_Damage = Weapon_Min_Damage * (Str + 100) / 100
> ```
>
> 그리고 "Strength affects the amount of damage your attacks inflict and the type of
> armor and weapons you can equip." — **힘은 피해와 착용 조건 둘 다**이다.

여기서 배울 것은 "스탯이냐 장비냐" 가 아니라 **더하느냐 곱하느냐**다.

| 결합 | 좋은 무기를 들면 | 티어 사다리가 |
|:--|:--|:--|
| 무기 × (1 + 스탯) | 쌓아 둔 **스탯 전체가 함께 커진다** | 저절로 선다 |
| 무기 + 스탯 + 강화 + … (가산 형제) | **그 항목의 숫자만** 커진다 | 억지로 세워야 한다 |

🔴 **가산 형제 구조에서 장비 비중을 키우는 길은 "장비 숫자를 크게 하는 것" 뿐이다.**
그러면 스탯이 상대적으로 무의미해진다. 곱셈 결합이면 둘 다 의미를 가진다.

**관문(requirement)도 설계 도구다** — 디아블로2는 착용에 힘·민첩을 요구해서
"이 장비를 쓰려면 이만큼 키워야 한다" 를 **피해 공식 밖에서** 강제한다.
같은 문서가 상한도 적는다 — 어떤 장비도 힘 253 을 넘게 요구하지 않는다.

---

## 7. **아이템이 지닐 축의 수를 고정한다** (가장 최신 사례)

> 🟢 Blizzard 공식, 디아블로4 시즌 4 "Loot Reborn" (2024-05)
>
> "We reduced the number of affixes on items (down to 3 on Legendary items,
> 2 on Rare items)"
>
> 그리고 값으로 보상했다 — "We've also increased the overall values of these affixes,
> so they should feel more powerful!"

같은 글이 **드롭 수도 줄였다**고 적는다:

> "By making items more individually impactful, we've significantly decreased the
> number of items that drop when slaying Monsters."

**조건부 수식어를 평범한 수식어로 바꿨다** — "+10% damage on non-injured Elites" 같은
것 대신 이동속도·최대생명·스킬 랭크처럼 **조건 없는** 값을 준다. 이유를 이렇게 적는다:

> "One of our several goals for the Itemization changes is to make it easier to
> understand which items are upgrades when they drop."

그리고 **복잡도를 버리지 않고 옮겼다** — "we've moved their complexity and
customization to our new crafting systems"(Tempering·Masterworking).

> 🟡 같은 방향의 더 이른 사례: 디아블로3 BlizzCon 2013 패널(팬사이트 전사본)에서
> "less is more" 와 아이템당 primary/secondary **개수 고정**, 접사 난수 폭 축소를 말한다.
> 목표도 같다 — 아이템이 "math problems that you have to look at arrows to figure out"
> 가 되지 않게 하는 것.

**절차**

1. 아이템 등급마다 **수식어 칸 수를 숫자로 고정**한다.
2. 칸을 줄이면 **값을 올려** 총량을 유지한다.
3. **조건부 수식어를 기본값으로 삼지 않는다.** 비교가 어려워진다.
4. 늘리고 싶으면 **칸(축)이 아니라 깊이**로 늘린다 — 제작·강화·재련 같은 **별도 계층**.

---

## 8. 수치 인플레이션 — 처음부터 자릿수를 정한다

> 🟡 Jonathan Rogers(Grinding Gear Games 게임 디렉터), Path of Exile 2 관련 인터뷰
> 보도(2024). 숫자 폭주를 피하는 것이 목표이고, 뒤늦은 **"숫자 스쿼시"** 는 단기 처방일
> 뿐이라는 취지로 말한다("I don't think we'll ever have to do a number squish").
> ⚠️ 1차 영상·원문이 아니라 **언론 보도**를 통해 확인했다.

**절차**

1. **최종 레벨에서 한 방 피해의 자릿수**를 먼저 정한다(예: 세 자리).
2. 거기서 거꾸로 성장 배율을 정한다 — 곱셈 수식어가 몇 개까지 겹칠 수 있는지 센다(§4).
3. 곱셈이 겹치는 상한이 없으면 자릿수는 반드시 터진다.

---

## 9. 점검 목록

**새 수식어를 더할 때**
- [ ] 중심 자원 기준으로 얼마인가 (§1·§3)
- [ ] 가산 풀인가, 이름 붙인 곱셈인가 (§4)
- [ ] 곱셈이면 방어 적용 앞인가 뒤인가 (§4)
- [ ] 비용 곡선 위인가 아래인가 — overpowered 면 **이득을 줄인다** (§3)

**새 장비·등급을 더할 때**
- [ ] 수식어 칸 수가 등급별로 고정돼 있는가 (§7)
- [ ] 조건부 수식어를 기본값으로 쓰고 있지 않은가 (§7)
- [ ] 장비와 스탯이 **곱해지는가 더해지는가** — 의도한 쪽인가 (§6)

**새 지역·난이도를 더할 때**
- [ ] 방어의 상한·하한이 적혀 있는가 (§5)
- [ ] 벽을 피해 공식으로 세우고 있지는 않은가 — 접근·생존으로 세울 수 있는가 (§5)
- [ ] 성장 비용과 수확이 **같은 종류의 곡선**인가 (§2)

**수치를 적을 때**
- [ ] 문서의 표가 **생성기·코드와 같은가** — 손으로 옮긴 표는 반드시 어긋난다
- [ ] 최종 자릿수 상한을 넘지 않는가 (§8)

---

## 10. 출처

| 등급 | 자료 | 쓰인 곳 |
|:--|:--|:--|
| 🟢 | **The Arreat Summit** (디아블로2 공식 매뉴얼) — `classic.battle.net/diablo2exp/` | §5 저항 상한·하한, §6 근접 피해 공식·착용 조건 |
| 🟢 | **Blizzard, "Galvanize your Legend in Season 4: Loot Reborn"** (2024-05) — `news.blizzard.com/en-us/article/24077223` | §7 접사 칸 수·값 인상·드롭 감소·조건부 제거·복잡도 이전 |
| 🟢 | **Mark_GGG**(GGG 직원), Path of Exile 공식 포럼 (2014-04-18) — `pathofexile.com/forum/view-thread/892570` | §4 "increased 는 같은 값에 대해 가산" |
| 🟢 | **Ian Schreiber, 「Game Balance Concepts」** (2010) — `gamebalanceconcepts.wordpress.com` Lv1·2·3 | §1 중심 자원, §2 수치 관계, §3 비용 곡선 |
| 🟡 | PoE 공식 포럼 플레이어 글 다수 (2016·2017·2024) | §4 "more 는 각각 곱셈" — **개발사 진술 아님** |
| 🟡 | BlizzCon 2013 디아블로3 패널 전사본 (팬사이트) | §7 "less is more", 개수 고정 |
| 🟡 | Jonathan Rogers 인터뷰 보도 (2024) | §8 숫자 스쿼시 |
| 🟡 | Schreiber & Romero, 『Game Balance』 (Routledge) | 미열람 — 목차만 확인 |

### ⚠️ 확인하지 못한 것

* **"more" 가 곱셈이라는 개발사 공식 진술** — 커뮤니티 일관 진술만 있다.
* **피해 계산 순서를 명시한 공식 문서** — 어느 쪽에서도 확인하지 못했다.
* "장비가 피해의 주된 출처" 라는 디아블로2의 **명시적 문장** — 공식에서 유도할 수는
  있지만 그런 문장은 없다.
* 디아블로3 자료의 **개발사 공식 페이지** — 확보한 것은 팬사이트 전사본이다.
* 일반적인 "가산 대 곱셈" 설계 지침의 **권위 있는 2024~2025년 출판물** — 찾지 못했다.
  검색에 걸리는 것은 포럼·블로그 수준이라 이 문서에 인용하지 않았다.
