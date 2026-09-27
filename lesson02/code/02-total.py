# ===== Example 2: adding things up =====
# 生字：total 總和 · count 數量／計數 · crit（critical）暴擊
# 訣竅：先做一個「計數的盒子」（counter 計數器），然後在迴圈裡一直往裡面加。

total = 0                    # 總傷害，從 0 開始

for i in range(1, 6):
    damage = 12 * i
    total = total + damage   # 舊的總和 + 這一下 -> 存回去（store 儲存）
    print(f"Hit {i} deals {damage}, total so far {total}")

print(f"Five-hit combo total: {total}")

# 同樣的招數可以數「某件事發生幾次」（happened 發生）
crit_count = 0
rolls = [97, 12, 85, 43, 99]        # 假裝這是五次骰出來的點數（pretend 假裝）

for roll in rolls:                   # for 也可以把清單裡的東西一個一個拿出來
    if roll >= 80:
        crit_count = crit_count + 1

print(f"{crit_count} critical hits out of 5")

# Try it 試試看：
# 1. 把 total = total + damage 改成 total += damage（意思一樣，比較短）
# 2. 把 1 加到 100
