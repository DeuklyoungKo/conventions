"""밸런스 수치표 생성기 — 설계 결정 몇 개를 넣으면 표가 나온다.

    py tools/balance_table.py                      # 기본값으로 표를 뽑는다
    py tools/balance_table.py --zones 8 --tiers 4
    py tools/balance_table.py --defense ratio --ratio-k 400

🔴 **이 스크립트는 「정답 수치」를 주지 않는다.** 보편적으로 옳은 몬스터 체력 같은 것은
없다 — 그 수는 ①중심 자원 ②합성 규칙(가산/곱셈) ③방어의 형태 ④TTK 목표 ⑤구역 수에서
**유도되는 것**이고, 그중 하나만 바꾸면 표 전체가 달라진다.

그래서 수치가 아니라 **유도 과정**을 준다. 입력을 바꿔 다시 돌리면 표가 다시 나온다.
📌 손으로 옮겨 적은 표는 **반드시 어긋난다.** 표가 필요하면 이것을 돌려서 쓴다.

근거가 되는 절은 `5_RPG_BALANCE_GUIDE.md` 의 번호로 주석에 달아 두었다.
"""
import argparse
import math


# ── §2 수치 관계 — 곡선 다섯 꼴 ─────────────────────────────────────────
#
# 📌 **기법: 모양을 0~1 로 정규화한 뒤 [최소, 최대] 에 얹는다.**
# 그러면 "양 끝을 먼저 정하고 가운데는 곡선이 채운다"(§3.1)가 그대로 구현된다.
# 곡선을 바꿔도 **양 끝은 움직이지 않는다** — 비교가 가능해지는 이유다.
#
# `a` 는 세기(강도)다. 지수는 클수록 뒤가 가파르고, 로그는 클수록 앞이 가파르다.
def shape(t, kind, a=1.0, steps=5):
    if kind == "linear":
        return t
    if kind == "geom":                      # 등비 — 비율이 일정하다
        return t                            # (요구값 자체를 등비로 깔 때 쓴다)
    if kind == "exp":                       # 뒤로 갈수록 가파르다
        return (pow(1 + a, t) - 1) / (pow(1 + a, 1) - 1)
    if kind == "log":                       # 앞이 가파르고 뒤가 눕는다
        return math.log(1 + a * t) / math.log(1 + a)
    if kind == "sigmoid":                   # 가운데가 가파른 S 꼴
        f = lambda x: 1 / (1 + math.exp(-a * (x - 0.5)))
        lo, hi = f(0.0), f(1.0)
        return (f(t) - lo) / (hi - lo)
    if kind == "step":                       # 구간으로 끊어 오른다
        return round(steps * t) / steps
    raise SystemExit("알 수 없는 곡선: %s" % kind)


def build(a):
    n = a.zones

    # ── §2 수치 관계 — 요구 공격력은 **등비**로 둔다 ─────────────────────
    # 선형으로 두면 뒤 구역에서 상대적 성장이 0 에 수렴해 "평평한 칸" 이 생긴다.
    if a.curve == "geom":
        # 등비 — 구역마다 **같은 비율**로 오른다. 뒤 구역에서도 상대 성장이 유지된다.
        g = (a.atk_last / a.atk_first) ** (1.0 / (n - 1)) if n > 1 else 1.0
        req = [a.atk_first * (g ** i) for i in range(n)]
    else:
        # 그 외는 모양을 0~1 로 정규화해 양 끝에 얹는다(§3.1).
        req = [a.atk_first + (a.atk_last - a.atk_first)
               * shape(i / max(1, n - 1), a.curve, a.curve_param, a.curve_steps)
               for i in range(n)]
    prev = [a.unarmed] + req[:-1]                          # 그 구역에 들고 오는 앞 구역 장비

    # ── 플레이어 쪽 성장 (선형 가정 — 게임마다 다르므로 입력으로 뺀다) ──
    php = [a.hp_first + (a.hp_last - a.hp_first) * i / max(1, n - 1) for i in range(n)]
    pdef = [a.def_first + (a.def_last - a.def_first) * i / max(1, n - 1) for i in range(n)]

    rows = []
    for i in range(n):
        # ── §5 방어 — 벽을 세우는 자리 ──────────────────────────────────
        # 뺄셈: 앞 구역 장비가 딱 `wall_dmg` 만 내도록 DEF 를 절벽에 붙인다.
        # 비율: 경감률을 풀어 앞 구역 피해가 요구 장비의 `wall_ratio` 이하가 되게 한다.
        if a.defense == "subtract":
            mon_def = max(0.0, prev[i] - a.wall_dmg)
            dmg_req = max(1.0, req[i] - mon_def)
            dmg_prev = max(1.0, prev[i] - mon_def)
            # 보스는 **벽이 아니라 기울기**다 — 앞 구역 장비도 `slope_dmg` 는 긁어야 한다.
            boss_def = max(0.0, prev[i] - a.slope_dmg)
            dmg_boss = max(1.0, req[i] - boss_def)
        else:
            k = a.ratio_k
            mon_def = k * (req[i] * a.wall_ratio) / max(1e-9, prev[i] - req[i] * a.wall_ratio) \
                if prev[i] > req[i] * a.wall_ratio else k
            cut = mon_def / (mon_def + k)
            dmg_req = max(1.0, req[i] * (1 - cut))
            dmg_prev = max(1.0, prev[i] * (1 - cut))
            boss_def = mon_def * a.boss_def_scale
            dmg_boss = max(1.0, req[i] * (1 - boss_def / (boss_def + k)))

        # ── §10 TTK 목표에서 체력을 역산한다 ────────────────────────────
        mon_hp = dmg_req * a.ttk_normal
        boss_hp = dmg_boss * a.ttk_boss_win

        # ── 보스 공격력은 **패배 턴**에서 역산한다 ──────────────────────
        # 승리 턴만 맞추면 "이길 수 없는 보스" 가 승리 턴만 보고 통과한다.
        boss_atk = pdef[i] + php[i] / a.ttk_boss_lose

        rows.append(dict(
            zone=i + 1, tier=min(a.tiers, 1 + i * a.tiers // n),
            req=req[i], prev=prev[i],
            mon_def=mon_def, mon_hp=mon_hp,
            boss_def=boss_def, boss_hp=boss_hp, boss_atk=boss_atk,
            dmg_req=dmg_req, dmg_prev=dmg_prev, dmg_boss=dmg_boss,
            php=php[i], pdef=pdef[i],
        ))
    return rows


def report(rows, a):
    print("| 구역 | 티어 | 요구 ATK | 앞 장비 ATK | 일반 DEF | 일반 HP | 보스 DEF | 보스 HP | 보스 ATK |")
    print("|--:|--:|--:|--:|--:|--:|--:|--:|--:|")
    for r in rows:
        print("| %d | %d | %.0f | %.0f | %.0f | %.0f | %.0f | %.0f | %.0f |" % (
            r["zone"], r["tier"], r["req"], r["prev"],
            r["mon_def"], r["mon_hp"], r["boss_def"], r["boss_hp"], r["boss_atk"]))

    print()
    print("| 구역 | 요구 장비 피해 | 앞 장비 피해 | **누출** | 보스에게 앞 장비 |")
    print("|--:|--:|--:|--:|--:|")
    for r in rows:
        print("| %d | %.0f | %.0f | **%.0f%%** | %.0f |" % (
            r["zone"], r["dmg_req"], r["dmg_prev"],
            100.0 * r["dmg_prev"] / max(1e-9, r["dmg_req"]),
            max(1.0, r["prev"] - r["boss_def"])))

    # ── 자기 검증 — 표가 스스로 성립하는지 본다 (§14 점검 목록) ────────
    print("\n=== 검증 ===")
    ok = True

    gaps = [rows[i]["req"] - rows[i - 1]["req"] for i in range(1, len(rows))]
    if gaps and min(gaps) > 0:
        print("  [PASS] 사다리가 단조다 (최소 간격 %.1f)" % min(gaps))
    else:
        print("  [FAIL] 사다리가 내려가는 구역이 있다 — 티어와 강화 폭이 겹친다")
        ok = False

    leak = max(100.0 * r["dmg_prev"] / max(1e-9, r["dmg_req"]) for r in rows[1:]) if len(rows) > 1 else 0
    if leak <= a.max_leak * 100:
        print("  [PASS] 앞 장비 누출 최대 %.0f%% (상한 %.0f%%)" % (leak, a.max_leak * 100))
    else:
        print("  [FAIL] 앞 장비 누출 %.0f%% — 벽이 서지 않는다" % leak)
        ok = False

    slope = min(max(1.0, r["prev"] - r["boss_def"]) for r in rows[1:]) if len(rows) > 1 else 0
    if slope >= a.slope_dmg * 0.9:
        print("  [PASS] 보스에게 앞 장비가 최소 %.0f 을 긁는다 (기울기가 보인다)" % slope)
    else:
        print("  [FAIL] 보스에게 앞 장비가 %.0f 뿐 — \"조금만 더\" 가 아니라 \"불가능\" 으로 읽힌다" % slope)
        ok = False

    # 🔴 **패배 턴은 승리 턴보다 길어야 한다.** 짧으면 플레이어가 먼저 죽으므로
    # "그 보스는 이길 수 없다" 는 뜻이다. 승리 턴만 맞추면 이 사고가 통과한다.
    lose, win = a.ttk_boss_lose, a.ttk_boss_win
    if lose <= win:
        print("  [FAIL] 패배 %.0f턴 ≤ 승리 %.0f턴 — 플레이어가 먼저 죽는다(이길 수 없는 보스)"
              % (lose, win))
        ok = False
    else:
        print("  [PASS] 패배 %.0f턴 > 승리 %.0f턴 (여유 %.0f턴)" % (lose, win, lose - win))

    print("\n%s" % (">>> 표가 성립한다." if ok else ">>> 입력을 고쳐야 한다."))
    return 0 if ok else 1


def main():
    p = argparse.ArgumentParser(description="설계 결정에서 밸런스 수치표를 유도한다")
    p.add_argument("--zones", type=int, default=10, help="구역(층·지역) 수")
    p.add_argument("--tiers", type=int, default=5, help="재질 티어 수")
    p.add_argument("--atk-first", type=float, default=17, help="1구역 요구 공격력")
    p.add_argument("--atk-last", type=float, default=146, help="마지막 구역 요구 공격력")
    p.add_argument("--unarmed", type=float, default=5, help="맨몸 공격력(1구역의 '앞 장비')")
    p.add_argument("--hp-first", type=float, default=100, help="1구역 플레이어 HP")
    p.add_argument("--hp-last", type=float, default=240, help="마지막 구역 플레이어 HP")
    p.add_argument("--def-first", type=float, default=1, help="1구역 플레이어 DEF")
    p.add_argument("--def-last", type=float, default=40, help="마지막 구역 플레이어 DEF")
    p.add_argument("--defense", choices=["subtract", "ratio"], default="subtract",
                   help="방어의 형태 (§5)")
    p.add_argument("--ratio-k", type=float, default=1000, help="비율형의 K — DEF/(DEF+K)")
    p.add_argument("--wall-dmg", type=float, default=1,
                   help="뺄셈형: 앞 구역 장비가 내는 피해(벽의 높이)")
    p.add_argument("--wall-ratio", type=float, default=0.15,
                   help="비율형: 앞 구역 장비가 요구 장비 대비 낼 비율")
    p.add_argument("--slope-dmg", type=float, default=7,
                   help="보스에게 앞 구역 장비가 내야 할 피해(기울기)")
    p.add_argument("--boss-def-scale", type=float, default=0.9,
                   help="비율형: 보스 DEF = 일반 DEF × 이 값")
    p.add_argument("--ttk-normal", type=float, default=6, help="일반 몬스터 목표 턴")
    p.add_argument("--ttk-boss-win", type=float, default=12, help="보스 승리 목표 턴")
    # 🔴 기본값은 승리 턴보다 **길어야** 한다 — 아니면 이길 수 없는 보스가 된다.
    p.add_argument("--ttk-boss-lose", type=float, default=16,
                   help="보스 패배 하한 턴 (승리 턴보다 길어야 한다)")
    p.add_argument("--max-leak", type=float, default=0.25, help="앞 장비 누출 상한")
    p.add_argument("--curve", default="geom",
                   choices=["geom", "linear", "exp", "log", "sigmoid", "step"],
                   help="요구 공격력이 자라는 모양 (§2). 기본 geom=등비")
    p.add_argument("--curve-param", type=float, default=1.3, help="곡선 세기")
    p.add_argument("--curve-steps", type=int, default=5, help="step 곡선의 계단 수")
    a = p.parse_args()

    print("# 유도된 밸런스 표")
    print()
    print("> ⚠️ **이 수치는 아래 입력에서 유도된 것이다.** 입력이 바뀌면 표가 바뀐다.")
    print("> 옮겨 적지 말고 필요할 때 다시 돌린다.")
    print(">")
    print("> 입력: 구역 %d · 티어 %d · 곡선 %s · 방어 %s · TTK 일반 %g / 보스 승 %g · 패 %g · 누출 상한 %g%%"
          % (a.zones, a.tiers, a.curve, a.defense, a.ttk_normal, a.ttk_boss_win,
             a.ttk_boss_lose, a.max_leak * 100))
    print()
    return report(build(a), a)


if __name__ == "__main__":
    raise SystemExit(main())
