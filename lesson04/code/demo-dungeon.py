# ===== Lesson 4 final demo: a three-room dungeon =====
#
# The whole program is built out of functions: each one does a single job,
# and the main program just puts them together.
# This is what real game code looks like.
#   dungeon 地城 · mana 魔力 · goblin 哥布林
# Run it with:  python3 demo-dungeon.py
import random
import time

SPEED = 0.4
MAX_HP = 90
FIREBALL_COST = 3      # a fireball costs 3 mana 魔力


def say(text):
    """Print one line, then pause"""
    print(text)
    time.sleep(SPEED)


def bar(hp, max_hp):
    """Draw the HP as 20 blocks"""
    blocks = int(hp / max_hp * 20)
    if blocks < 0:
        blocks = 0
    return "█" * blocks + "░" * (20 - blocks)


# ---------- skills: each one is a function returning (damage, message) ----------
def slash(atk):
    damage = random.randint(atk - 2, atk + 2)
    return damage, f"Slash! {damage} damage"


def fireball(atk):
    if random.randint(1, 100) <= 25:          # 25% chance to miss
        return 0, "Fireball misses!"
    damage = atk * 2
    return damage, f"FIREBALL! {damage} damage"


def monster_attack(name, atk):
    damage = random.randint(atk - 3, atk + 3)
    return damage, f"{name} hits you for {damage} damage"


def is_alive(hp):
    return hp > 0


# ---------- one battle: also just a function ----------
def fight(hero_hp, mana, monster_name, monster_hp, monster_atk):
    """Fight one monster. Returns the (hp, mana) you are left with."""
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


# ---------- the main program: it only chains the functions together ----------
print("=" * 40)
print("           DUNGEON  QUEST")
print("=" * 40)

hero_hp = MAX_HP
mana = 6                                                             # only 6 mana for the whole dungeon
rooms = [("Slime", 30, 9), ("Goblin", 45, 12), ("Dragon", 65, 15)]   # harder each room

for i in range(len(rooms)):
    name, monster_hp, monster_atk = rooms[i]
    say(f"\n--- Room {i + 1} of {len(rooms)} ---")
    hero_hp, mana = fight(hero_hp, mana, name, monster_hp, monster_atk)

    if not is_alive(hero_hp):
        print("\n" + "=" * 40)
        print(f"  You fell in room {i + 1}...  GAME OVER")
        print("=" * 40)
        break

    # rest after clearing a room
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
