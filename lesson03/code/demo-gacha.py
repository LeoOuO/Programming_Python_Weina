# ===== 第 3 堂 最後 Demo：轉蛋機 =====
# 用到今天學的清單：卡池、背包、統計
# 執行：python3 demo-gacha.py
import random
import time

SPEED = 0.25

# ---------- 卡池：稀有的放少張、普通的放多張 ----------
POOL = (["🐉 SSR 龍騎士"] * 1
        + ["🦄 SSR 獨角獸"] * 1
        + ["🔥 SR 火法師"] * 4
        + ["❄️  SR 冰法師"] * 4
        + ["🏹 R 弓箭手"] * 15
        + ["🗡️  R 見習劍士"] * 15
        + ["🧑‍🌾 N 村民"] * 30
        + ["🐷 N 小豬"] * 30)


def spin():
    """轉蛋動畫：符號快速跳動，最後停在抽到的那張"""
    card = random.choice(POOL)
    for i in range(8):          # 先跳動 8 次，做出「轉」的感覺
        print("\r   🎰 " + random.choice(POOL) + "        ", end="", flush=True)
        time.sleep(SPEED / 3)
    print("\r   ✨ " + card + "        ")
    return card


print("=" * 40)
print("        轉 蛋 機")
print("=" * 40)
ssr_in_pool = 0
for card in POOL:                  # 數數看卡池裡有幾張 SSR
    if "SSR" in card:
        ssr_in_pool = ssr_in_pool + 1

print(f"卡池共 {len(POOL)} 張，其中 SSR {ssr_in_pool} 張")
print(f"抽中 SSR 的機率：{ssr_in_pool} / {len(POOL)}")
print()

name = input("你的名字？ ")
input("按 Enter 開始十連抽…")
print()

bag = []                       # 背包：一開始是空清單
for i in range(10):
    print(f"第 {i + 1} 抽")
    card = spin()
    bag.append(card)           # 抽到的卡放進背包
    time.sleep(SPEED / 2)

# ---------- 統計 ----------
print()
print("=" * 40)
print(f"  {name} 的十連抽結果")
print("=" * 40)

ssr = 0
sr = 0
for card in bag:               # 把背包裡的卡一張一張看過
    if "SSR" in card:
        ssr = ssr + 1
    elif "SR" in card:
        sr = sr + 1

print(f"  SSR：{ssr} 張")
print(f"  SR ：{sr} 張")
print(f"  其他：{len(bag) - ssr - sr} 張")
print()

print("  背包內容：")
for i in range(len(bag)):
    print(f"   {i + 1:>2}. {bag[i]}")

print()
if ssr >= 2:
    print("  🎊 歐洲人！兩張以上 SSR")
elif ssr == 1:
    print("  😀 運氣不錯，抽到 SSR 了")
elif sr >= 3:
    print("  🙂 沒有 SSR，但 SR 不少")
else:
    print("  😭 非洲人……再來一次吧")

print()
print("想改機率就改上面 POOL 裡的數字（× 幾張），改完再抽一次看看。")
