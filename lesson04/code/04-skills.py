# ===== Example 4: a skill system made of functions =====
# 生字：skill 技能 · slash 斬擊 · fireball 火球 · cost 消耗 · mana 魔力
import random

# 每個技能寫成一個函式，回傳 (傷害, 訊息)
# 這樣要加新技能時，只要再寫一個函式，不用去動戰鬥的程式。

def slash(atk):
    """普通斬擊：穩定的傷害"""
    damage = random.randint(atk - 2, atk + 2)
    return damage, f"Slash! {damage} damage"


def fireball(atk):
    """火球：傷害高，但有時候會失手"""
    if random.randint(1, 100) <= 25:          # 25% 機率沒打中
        return 0, "Fireball misses!"
    damage = atk * 2
    return damage, f"FIREBALL! {damage} damage"


def heal_self(hp, max_hp):
    """治療：回復 30 點，但不會超過上限"""
    hp = hp + 30
    if hp > max_hp:
        hp = max_hp
    return hp, f"You heal up to {hp} HP"


# 用用看
for i in range(3):
    damage, text = slash(12)
    print(text)

print()
for i in range(3):
    damage, text = fireball(12)
    print(text)

print()
hp, text = heal_self(80, 100)
print(text)

# Try it 試試看：
# 1. 自己加一個技能 thunder(atk)：傷害 atk * 3，但 50% 機率失手
# 2. 把 fireball 的失手機率從 25 改成 10，多跑幾次感覺差別
