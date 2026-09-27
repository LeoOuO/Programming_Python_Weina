# ===== Lesson 3 final demo: the gacha machine =====
# 生字：gacha 轉蛋 · machine 機器 · spin 轉動 · lucky 幸運 · stats 統計
# 到處都是清單：卡池、背包、最後的統計。
# Run it with:  python3 demo-gacha.py
import random
import time

SPEED = 0.25

# ---------- 卡池：稀有卡少少幾張，普通卡很多張 ----------
POOL = (["SSR Dragon Knight"] * 1
        + ["SSR Unicorn"] * 1
        + ["SR Fire Mage"] * 4
        + ["SR Ice Mage"] * 4
        + ["R Archer"] * 15
        + ["R Rookie Knight"] * 15
        + ["N Villager"] * 30
        + ["N Piglet"] * 30)


def spin():
    """轉動的動畫：快速閃過隨機的卡，最後停在真正抽到的那張（flash 閃過）"""
    card = random.choice(POOL)
    for i in range(8):          # 閃 8 次，做出「在轉」的感覺
        print("\r   [ " + random.choice(POOL) + " ]" + " " * 20, end="", flush=True)
        time.sleep(SPEED / 3)
    print("\r   * " + card + " *" + " " * 20)
    return card


print("=" * 44)
print("            GACHA MACHINE")
print("=" * 44)

ssr_in_pool = 0
for card in POOL:                  # 數數看卡池裡有幾張 SSR
    if "SSR" in card:
        ssr_in_pool = ssr_in_pool + 1

print(f"The pool has {len(POOL)} cards, {ssr_in_pool} of them SSR")
print(f"Chance of an SSR: {ssr_in_pool} out of {len(POOL)}")
print()

name = input("What is your name? ")
input("Press Enter for ten draws...")
print()

bag = []                       # 背包一開始是空清單
for i in range(10):
    print(f"Draw {i + 1}")
    card = spin()
    bag.append(card)           # 每張抽到的卡都放進背包
    time.sleep(SPEED / 2)

# ---------- 統計 stats ----------
print()
print("=" * 44)
print(f"  {name}'s ten draws")
print("=" * 44)

ssr = 0
sr = 0
for card in bag:               # 把背包裡的卡一張一張看過
    if "SSR" in card:
        ssr = ssr + 1
    elif "SR" in card:
        sr = sr + 1

print(f"  SSR:   {ssr}")
print(f"  SR:    {sr}")
print(f"  other: {len(bag) - ssr - sr}")
print()

print("  Your bag:")
for i in range(len(bag)):
    print(f"   {i + 1:>2}. {bag[i]}")

print()
if ssr >= 2:
    print("  Incredibly lucky! Two or more SSR")
elif ssr == 1:
    print("  Nice, you got an SSR")
elif sr >= 3:
    print("  No SSR, but plenty of SR")
else:
    print("  Bad luck this time... try again")

print()
print("Change the numbers in POOL (* how many copies) to change the rates,")
print("then draw again and see the difference.")
