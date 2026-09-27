# ===== Lesson 2 final demo: automatic battle =====
# 生字：automatic 自動的 · battle 戰鬥 · dragon 龍 · lava 熔岩 · average 平均
# Last lesson the fight was one turn long. Now a while loop keeps it going
# until someone falls, and random makes every hit different.
# Run it with:  python3 demo-auto-battle.py
import random
import time

SPEED = 0.45          # animation speed - make it smaller to fight faster

HERO = "Hero"
HERO_MAX_HP = 120
HERO_ATK = 14

BOSS = "Lava Dragon"
BOSS_MAX_HP = 160
BOSS_ATK = 14


def bar(hp, max_hp):
    """20 格的血條（bar 長條）"""
    blocks = int(hp / max_hp * 20)
    if blocks < 0:
        blocks = 0
    return "█" * blocks + "░" * (20 - blocks)


def show(hero_hp, boss_hp):
    print(f"  {HERO:<12} {bar(hero_hp, HERO_MAX_HP)} {max(hero_hp, 0):>3}/{HERO_MAX_HP}")
    print(f"  {BOSS:<12} {bar(boss_hp, BOSS_MAX_HP)} {max(boss_hp, 0):>3}/{BOSS_MAX_HP}")


def attack(name, base_atk):
    """算出這一擊並印出結果，然後回傳傷害（work out 算出 · return 回傳）"""
    roll = random.randint(1, 100)          # 擲骰子決定這一擊的品質（decide 決定）
    if roll >= 90:
        damage = base_atk * 2
        print(f"{name} lands a CRITICAL HIT for {damage} damage!")
    elif roll <= 10:
        damage = 0
        print(f"{name} swings and misses")
    else:
        damage = random.randint(base_atk - 4, base_atk + 4)
        print(f"{name} attacks for {damage} damage")
    return damage


hero_hp = HERO_MAX_HP
boss_hp = BOSS_MAX_HP
turn = 0
hero_total = 0        # 統計 stats：勇者總共打出多少傷害
potions = 2           # 只有兩瓶藥水，用完就沒了

print("=" * 42)
print("            AUTO BATTLE  START")
print("=" * 42)
show(hero_hp, boss_hp)
time.sleep(SPEED * 2)

# 只要雙方都還活著就繼續打（both 兩者都 · alive 活著）
while hero_hp > 0 and boss_hp > 0:
    turn = turn + 1
    print(f"\n-- Turn {turn} --")

    # 勇者先出手
    damage = attack(HERO, HERO_ATK)
    boss_hp = boss_hp - damage
    hero_total = hero_total + damage
    time.sleep(SPEED)

    # 王已經倒了就不用反擊了（counter-attack 反擊）
    if boss_hp <= 0:
        break

    # 王反擊
    damage = attack(BOSS, BOSS_ATK)
    hero_hp = hero_hp - damage
    time.sleep(SPEED)

    show(hero_hp, boss_hp)

    # 血量低而且還有藥水的時候，自動喝一瓶
    if hero_hp <= 30 and hero_hp > 0 and potions > 0:
        potions = potions - 1
        hero_hp = hero_hp + 40
        if hero_hp > HERO_MAX_HP:
            hero_hp = HERO_MAX_HP
        print(f"{HERO} drinks a potion, back to {hero_hp} HP ({potions} left)")
        time.sleep(SPEED)

print()
print("=" * 42)
if boss_hp <= 0:
    print(f"  The {BOSS} falls on turn {turn}!")
else:
    print(f"  The {HERO} falls on turn {turn}...")
print(f"  Turns: {turn}")
print(f"  Total damage by {HERO}: {hero_total}")
print(f"  Average per turn: {hero_total // turn}")
print("=" * 42)

print()
print("Change the numbers at the top to change the difficulty:")
print("higher BOSS_ATK is harder, more potions is easier.")
print("(Next lesson: lists - a bag and a card gacha)")
