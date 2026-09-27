# ===== Lesson 4 final demo: a three-room dungeon =====
# 生字：dungeon 地城 · room 房間 · monster 怪物 · skill 技能 · victory 勝利
#
# 整支程式是用「函式」堆出來的：每個函式做一件事，主程式只負責把它們串起來。
# 這就是真正的遊戲程式長的樣子。
# 執行：python3 demo-dungeon.py
import random
import time

SPEED = 0.4
MAX_HP = 90
FIREBALL_COST = 3      # 火球要花 3 點魔力（mana 魔力）


def say(text):
    """印一行字然後停一下"""
    print(text)
    time.sleep(SPEED)


def bar(hp, max_hp):
    """把血量畫成 20 格方塊"""
    blocks = int(hp / max_hp * 20)
    if blocks < 0:
        blocks = 0
    return "█" * blocks + "░" * (20 - blocks)


# ---------- 技能：每個都是一個函式，回傳 (傷害, 訊息) ----------
def slash(atk):
    damage = random.randint(atk - 2, atk + 2)
    return damage, f"Slash! {damage} damage"


def fireball(atk):
    if random.randint(1, 100) <= 25:          # 25% 失手
        return 0, "Fireball misses!"
    damage = atk * 2
    return damage, f"FIREBALL! {damage} damage"


def monster_attack(name, atk):
    damage = random.randint(atk - 3, atk + 3)
    return damage, f"{name} hits you for {damage} damage"


def is_alive(hp):
    return hp > 0


# ---------- 一場戰鬥：也是一個函式 ----------
def fight(hero_hp, mana, monster_name, monster_hp, monster_atk):
    """打一隻怪，回傳戰鬥後的 (血量, 魔力)"""
    say(f"\nA {monster_name} appears!  HP {monster_hp}")

    while is_alive(hero_hp) and is_alive(monster_hp):
        print()
        print(f"  1) Slash      2) Fireball (costs {FIREBALL_COST} mana, you have {mana})")
        choice = input("  Your move? ")

        if choice == "2" and mana >= FIREBALL_COST:
            mana = mana - FIREBALL_COST
            damage, text = fireball(14)
        else:
            if choice == "2":
                say("  Not enough mana! You swing your sword instead.")
            damage, text = slash(14)

        monster_hp = monster_hp - damage
        say("  " + text)

        if not is_alive(monster_hp):
            break

        damage, text = monster_attack(monster_name, monster_atk)
        hero_hp = hero_hp - damage
        say("  " + text)
        say(f"  You  {bar(hero_hp, MAX_HP)} {max(hero_hp, 0)}/{MAX_HP}")

    if is_alive(hero_hp):
        say(f"\n  The {monster_name} is defeated!")
    return hero_hp, mana


# ---------- 主程式：只負責把函式串起來 ----------
print("=" * 40)
print("           DUNGEON  QUEST")
print("=" * 40)

hero_hp = MAX_HP
mana = 6                                                             # 整趟地城只有 6 點魔力
rooms = [("Slime", 30, 9), ("Goblin", 45, 12), ("Dragon", 65, 15)]   # 三個房間，越來越難

for i in range(len(rooms)):
    name, monster_hp, monster_atk = rooms[i]
    say(f"\n--- Room {i + 1} of {len(rooms)} ---")
    hero_hp, mana = fight(hero_hp, mana, name, monster_hp, monster_atk)

    if not is_alive(hero_hp):
        print("\n" + "=" * 40)
        print(f"  You fell in room {i + 1}...  GAME OVER")
        print("=" * 40)
        break

    # 過關後回血
    hero_hp = hero_hp + 15
    if hero_hp > MAX_HP:
        hero_hp = MAX_HP
    mana = mana + 2
    say(f"  You rest: {hero_hp} HP, {mana} mana")
else:
    print("\n" + "=" * 40)
    print("  VICTORY! You cleared the dungeon!")
    print(f"  Remaining HP: {hero_hp}, mana {mana}")
    print("=" * 40)

print()
print("這支程式裡有 7 個函式。想加新技能？再寫一個函式，")
print("然後在 fight() 裡多一個選項就好，其他地方都不用動。")
print("火球有魔力限制，所以要想「這一場值不值得用」——這就是遊戲設計。")
