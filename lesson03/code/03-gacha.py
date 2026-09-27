# ===== Example 3: how card draw rates actually work =====
# 生字：pool 卡池 · draw 抽（卡）· rate 機率 · rare 稀有的 · copy 張（同樣的卡）
import random

# 訣竅：把卡池做成一個清單。
# 稀有卡放少少幾張，普通卡放很多張（rare 稀有 · common 普通 · few 少 · many 多）。
pool = (["SSR Dragon Knight"] * 2       # 2 copies
        + ["SR Fire Mage"] * 8          # 8 張（mage 法師）
        + ["R Archer"] * 30             # 30 copies
        + ["N Villager"] * 60)          # 60 張，總共 100 張（villager 村民 · in total 總共）

print(f"The pool has {len(pool)} cards")
print(f"Chance of an SSR: {pool.count('SSR Dragon Knight')} out of {len(pool)}")

card = random.choice(pool)        # 從卡池裡隨機抽一張
print(f"You drew: {card}")

print()
print("---- ten draws ----")      # 十連抽
results = []                      # 一個空清單，用來收集結果（empty 空的 · collect 收集）
for i in range(10):
    card = random.choice(pool)
    results.append(card)          # 把每次抽到的卡放進清單
    print(f"{i + 1}. {card}")

print()
print(f"SSR cards in these ten draws: {results.count('SSR Dragon Knight')}")

# Try it 試試看：
# 1. 把 SSR 改成 10 張再抽一次，感覺得出差別嗎？（difference 差別）
# 2. 抽 1000 次，數數看真的抽到幾張 SSR
