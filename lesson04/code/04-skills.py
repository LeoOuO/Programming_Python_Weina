# ===== Example 4: a skill system made of functions =====
import random

# Each skill 技能 is one function that returns (damage, message).
# To add a new skill you just write one more function -
# the battle code does not change at all.

def slash(atk):
    """Slash 斬擊: steady damage"""
    damage = random.randint(atk - 2, atk + 2)
    return damage, f"Slash! {damage} damage"


def fireball(atk):
    """Fireball 火球: big damage, but it sometimes misses"""
    if random.randint(1, 100) <= 25:          # 25% chance 機率 to miss
        return 0, "Fireball misses!"
    damage = atk * 2
    return damage, f"FIREBALL! {damage} damage"


def heal_self(hp, max_hp):
    """Heal 治療: +30 HP, but never above the maximum"""
    hp = hp + 30
    if hp > max_hp:
        hp = max_hp
    return hp, f"You heal up to {hp} HP"


# try them out
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

# Try it:
# 1. Add your own skill thunder(atk): damage atk * 3, but a 50% chance to miss
# 2. Change the fireball miss chance from 25 to 10 and run it a few times
