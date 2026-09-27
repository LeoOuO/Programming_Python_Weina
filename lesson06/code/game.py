# =====================================================================
#  SLIME  TOWER  -  你的第一個完整遊戲
#  生字：tower 塔 · floor 樓層 · rest 休息 · escape 逃跑 · final 最終的
#
#  用到的東西全部來自第 1~5 堂：
#    變數與 if      (第 1 堂)
#    for / while / random  (第 2 堂)
#    清單 list      (第 3 堂)
#    函式 def       (第 4 堂)
#    字典 dict      (第 5 堂)
#
#  執行：python3 game.py
# =====================================================================
import random
import time

SPEED = 0.3          # 想快一點就改成 0
MAX_POTIONS = 3      # 背包最多只能放 3 瓶藥水

# ---------------------------------------------------------------- 資料
game = {
    "hero": {"name": "Hero", "hp": 60, "max_hp": 60, "atk": 12},
    "gold": 30,
    "potions": 1,
    "floor": 1,
}

MONSTERS = [
    {"name": "Slime",      "hp": 22, "atk": 6,  "gold": 25},
    {"name": "Bat",        "hp": 28, "atk": 8,  "gold": 30},
    {"name": "Goblin",     "hp": 36, "atk": 10, "gold": 40},
    {"name": "Orc",        "hp": 48, "atk": 13, "gold": 55},
    {"name": "Slime King", "hp": 70, "atk": 15, "gold": 99},   # 最後一層的王
]

SHOP = {
    "Potion":      {"price": 25, "text": "+1 potion"},
    "Sharp Sword": {"price": 50, "text": "ATK +4"},
    "Big Shield":  {"price": 60, "text": "max HP +20, full heal"},
}


# ------------------------------------------------------------ 小工具函式
def say(text):
    print(text)
    time.sleep(SPEED)


def bar(hp, max_hp):
    blocks = int(hp / max_hp * 20)
    if blocks < 0:
        blocks = 0
    return "█" * blocks + "░" * (20 - blocks)


def show_status():
    hero = game["hero"]
    print(f"  {hero['name']}  {bar(hero['hp'], hero['max_hp'])} "
          f"{max(hero['hp'], 0)}/{hero['max_hp']}   ATK {hero['atk']}   "
          f"{game['gold']}g   potions {game['potions']}")


def is_alive(hp):
    return hp > 0


def hero_damage():
    """算出主角這一擊的傷害（10% 機率暴擊）"""
    atk = game["hero"]["atk"]
    if random.randint(1, 100) <= 10:
        return atk * 2, True
    return random.randint(atk - 2, atk + 2), False


def drink_potion():
    """喝藥水。沒有藥水的話回傳 False"""
    if game["potions"] <= 0:
        return False
    hero = game["hero"]
    game["potions"] = game["potions"] - 1
    hero["hp"] = min(hero["hp"] + 30, hero["max_hp"])
    say(f"  You drink a potion -> {hero['hp']} HP")
    return True


# ---------------------------------------------------------------- 戰鬥
def battle(monster):
    """打一隻怪。贏了回傳 True，倒下回傳 False。"""
    hero = game["hero"]
    hp = monster["hp"]
    say(f"\n  A {monster['name']} blocks the stairs!  HP {hp}  ATK {monster['atk']}")

    while is_alive(hp) and is_alive(hero["hp"]):
        print()
        print(f"   1) Attack    2) Potion ({game['potions']})    3) Run away")
        choice = input("   > ")

        if choice == "2":
            if not drink_potion():
                say("  No potions left!")
                continue                      # 沒喝到，不算用掉一回合
        elif choice == "3":
            if random.randint(1, 100) <= 50:  # 50% 逃跑成功
                say("  You escaped!")
                return False
            say("  You failed to escape!")
        else:
            damage, crit = hero_damage()
            hp = hp - damage
            if crit:
                say(f"  CRITICAL HIT! {damage} damage")
            else:
                say(f"  You hit for {damage}")
            if not is_alive(hp):
                break

        # 怪物反擊
        damage = random.randint(monster["atk"] - 2, monster["atk"] + 2)
        hero["hp"] = hero["hp"] - damage
        say(f"  The {monster['name']} hits you for {damage}")
        show_status()

    if not is_alive(hero["hp"]):
        return False

    game["gold"] = game["gold"] + monster["gold"]
    say(f"\n  {monster['name']} defeated!   +{monster['gold']} gold")
    return True


# ---------------------------------------------------------------- 商店
def shop():
    while True:
        print("\n" + "-" * 44)
        print(f"  SHOP                       you have {game['gold']}g")
        names = []
        for item in SHOP:
            names.append(item)
        for i in range(len(names)):
            data = SHOP[names[i]]
            print(f"   {i + 1}) {names[i]:<12} {data['price']:>3}g   {data['text']}")
        print("   0) Leave the shop")

        choice = input("   > ")
        if choice == "0":
            return
        if choice not in ["1", "2", "3"]:
            print("   That is not on the list.")
            continue

        item = names[int(choice) - 1]
        data = SHOP[item]
        if data["price"] > game["gold"]:
            say("   Not enough gold.")
            continue
        if item == "Potion" and game["potions"] >= MAX_POTIONS:
            say(f"   You can only carry {MAX_POTIONS} potions.")
            continue

        game["gold"] = game["gold"] - data["price"]
        hero = game["hero"]
        if item == "Potion":
            game["potions"] = game["potions"] + 1
        elif item == "Sharp Sword":
            hero["atk"] = hero["atk"] + 4
        elif item == "Big Shield":
            hero["max_hp"] = hero["max_hp"] + 20
            hero["hp"] = hero["max_hp"]
        say(f"   Bought {item}!")
        show_status()


# ------------------------------------------------------------ 主程式
print("=" * 46)
print("            S L I M E   T O W E R")
print("=" * 46)
name = input("What is your name, hero? ")
if name != "":
    game["hero"]["name"] = name

say("\nFive floors. One Slime King at the top. Good luck.")
show_status()

for floor in range(len(MONSTERS)):
    game["floor"] = floor + 1
    print("\n" + "=" * 46)
    print(f"  FLOOR {game['floor']}")
    print("=" * 46)

    shop()                                   # 每層樓前面都有商店

    won = battle(MONSTERS[floor])
    if not is_alive(game["hero"]["hp"]):
        print("\n" + "=" * 46)
        print(f"  You fell on floor {game['floor']}...   GAME OVER")
        print(f"  Gold collected: {game['gold']}")
        print("=" * 46)
        break
    if not won:                              # 逃跑成功，這層不算過
        say("  You run back down the stairs and try again.")

    # 過關休息
    hero = game["hero"]
    hero["hp"] = min(hero["hp"] + 15, hero["max_hp"])
    say(f"\n  You rest on the stairs. HP {hero['hp']}")
else:
    print("\n" + "=" * 46)
    print("  YOU BEAT THE SLIME KING!")
    print(f"  {game['hero']['name']} cleared all 5 floors "
          f"with {game['hero']['hp']} HP and {game['gold']} gold.")
    print("=" * 46)

print()
print("這支程式有 8 個函式、3 份資料（game / MONSTERS / SHOP）。")
print("想加第六層？在 MONSTERS 加一隻怪就好，其他都不用動。")
