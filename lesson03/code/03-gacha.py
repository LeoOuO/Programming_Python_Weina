# ===== 範例 3：抽卡的機率是怎麼做的 =====
import random

# 做法：把卡池做成一個清單，稀有的放少張、普通的放多張
pool = (["SSR 龍騎士"] * 2       # 2 張
        + ["SR 火法師"] * 8       # 8 張
        + ["R 弓箭手"] * 30       # 30 張
        + ["N 村民"] * 60)        # 60 張，合計 100 張

print(f"卡池總共有 {len(pool)} 張卡")
print(f"抽到 SSR 的機率是 {pool.count('SSR 龍騎士')} / {len(pool)}")

card = random.choice(pool)        # 從卡池裡隨機抽一張
print(f"你抽到了：{card}")

print()
print("---- 十連抽 ----")
results = []                      # 先準備一個空清單裝結果
for i in range(10):
    card = random.choice(pool)
    results.append(card)          # 抽到的放進清單
    print(f"{i + 1}. {card}")

print()
print(f"這十抽裡面 SSR 有 {results.count('SSR 龍騎士')} 張")

# 試試看：
# 1. 把 SSR 改成 10 張，再抽十次，感覺有差嗎？
# 2. 抽 1000 次，數數看真的抽到幾張 SSR（用 for 跑 1000 次）
