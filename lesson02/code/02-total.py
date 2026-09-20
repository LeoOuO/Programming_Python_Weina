# ===== 範例 2：把傷害加起來（累加）=====
# 訣竅：先準備一個「計數的盒子」，在迴圈裡一直往裡面加

total = 0                    # 總傷害，從 0 開始

for i in range(1, 6):
    damage = 12 * i
    total = total + damage   # 舊的總和 + 這一下 → 存回去
    print(f"第 {i} 下 {damage}，目前累積 {total}")

print(f"五連段總傷害：{total}")

# 同樣的手法可以數「有幾次暴擊」
crit_count = 0
rolls = [97, 12, 85, 43, 99]        # 先假裝這是五次骰出來的點數

for roll in rolls:                   # for 也可以直接把清單裡的東西一個一個拿出來
    if roll >= 80:
        crit_count = crit_count + 1

print(f"五次裡面暴擊了 {crit_count} 次")

# 試試看：
# 1. 把 total = total + damage 改成 total += damage（一樣的意思，比較短）
# 2. 算算看 1 加到 100 是多少
