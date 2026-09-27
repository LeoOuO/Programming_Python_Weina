# ===== Lesson 5 final demo: fight, loot, shop =====
# 生字：loot 戰利品 · shop 商店 · stock 庫存 · equip 裝備 · afford 買得起
#
# 這次每個角色、每件道具都是一個「字典」，資料整整齊齊放在一起。
# 流程：打一隻怪 -> 拿金幣 -> 去商店買東西 -> 再打下一隻
# 執行：python3 demo-shop.py
import random
import time

SPEED = 0.35


def say(text):
    print(text)
    time.sleep(SPEED)


def bar(hp, max_hp):
    blocks = int(hp / max_hp * 20)
    if blocks < 0:
        blocks = 0
    return "█" * blocks + "░" * (20 - blocks)


# ---------- 主角：一個字典裝完所有資料 ----------
hero = {
    "name": "Hero",
    "hp": 85,
    "max_hp": 85,
    "atk": 13,
    "gold": 60,
    "potions": 1,
}

# ---------- 怪物圖鑑：清單裡放字典 ----------
monsters = [
    {"name": "Slime",  "hp": 26, "atk": 7,  "gold": 30},
    {"name": "Goblin", "hp": 40, "atk": 10, "gold": 55},
    {"name": "Ogre",   "hp": 56, "atk": 13, "gold": 80},
]

# ---------- 商店：名稱 -> 資料 ----------
shop = {
    "Potion":     {"price": 20, "effect": "heal",  "amount": 30},
    "Sharp Sword": {"price": 55, "effect": "atk",  "amount": 5},
    "Armor":      {"price": 70, "effect": "maxhp", "amount": 25},
}


def show_hero():
    say(f"  {hero['name']}  {bar(hero['hp'], hero['max_hp'])} "
        f"{max(hero['hp'], 0)}/{hero['max_hp']}  ATK {hero['atk']}  "
        f"{hero['gold']}g  potions {hero['potions']}")


def fight(monster):
    """打一隻怪。贏了回傳 True 並拿到金幣，輸了回傳 False。"""
    hp = monster["hp"]
    say(f"\nA {monster['name']} appears!  HP {hp}  ATK {monster['atk']}")

    while hp > 0 and hero["hp"] > 0:
        print()
        print(f"  1) Attack      2) Potion ({hero['potions']} left)")
        choice = input("  Your move? ")

        if choice == "2" and hero["potions"] > 0:
            hero["potions"] = hero["potions"] - 1
            hero["hp"] = min(hero["hp"] + 30, hero["max_hp"])
            say(f"  You drink a potion -> {hero['hp']} HP")
        else:
            damage = random.randint(hero["atk"] - 2, hero["atk"] + 2)
            hp = hp - damage
            say(f"  You hit the {monster['name']} for {damage}")
            if hp <= 0:
                break

        damage = random.randint(monster["atk"] - 2, monster["atk"] + 2)
        hero["hp"] = hero["hp"] - damage
        say(f"  The {monster['name']} hits you for {damage}")
        show_hero()

    if hero["hp"] <= 0:
        return False

    hero["gold"] = hero["gold"] + monster["gold"]
    say(f"\n  {monster['name']} defeated!  +{monster['gold']} gold")
    return True


def visit_shop():
    """逛商店，可以買到不想買為止。"""
    while True:
        print("\n" + "=" * 42)
        print(f"  SHOP        you have {hero['gold']} gold")
        print("=" * 42)
        names = []                      # 把商品名稱收成清單，才能用編號選
        for item in shop:
            names.append(item)
        for i in range(len(names)):
            item = names[i]
            data = shop[item]
            print(f"  {i + 1}) {item:<12} {data['price']:>3}g   "
                  f"({data['effect']} +{data['amount']})")
        print("  0) Leave")

        choice = input("  Buy which? ")
        if choice == "0":
            return

        # 把輸入的編號變成商品名稱
        if choice not in ["1", "2", "3"]:
            print("  ...what?")
            continue
        item = names[int(choice) - 1]
        data = shop[item]

        if data["price"] > hero["gold"]:
            say(f"  You cannot afford the {item}")
            continue

        hero["gold"] = hero["gold"] - data["price"]
        if data["effect"] == "heal":
            hero["potions"] = hero["potions"] + 1
        elif data["effect"] == "atk":
            hero["atk"] = hero["atk"] + data["amount"]
        elif data["effect"] == "maxhp":
            hero["max_hp"] = hero["max_hp"] + data["amount"]
            hero["hp"] = hero["hp"] + data["amount"]
        say(f"  Bought {item}!")
        show_hero()


# ---------- 主程式 ----------
print("=" * 42)
print("        SHOP  &  SWORD")
print("=" * 42)
show_hero()

for monster in monsters:
    visit_shop()
    if not fight(monster):
        print("\n" + "=" * 42)
        print(f"  You fell to the {monster['name']}...  GAME OVER")
        print(f"  Gold collected: {hero['gold']}")
        print("=" * 42)
        break
    show_hero()
else:
    print("\n" + "=" * 42)
    print("  You cleared every monster!")
    print(f"  Final: {hero['hp']}/{hero['max_hp']} HP, "
          f"ATK {hero['atk']}, {hero['gold']} gold")
    print("=" * 42)

print()
print("整個遊戲的資料都放在最上面的三個字典裡：hero、monsters、shop。")
print("想加新商品或新怪物？改那三個地方就好，下面的程式完全不用動。")
print("（提示：一開始的 60 金幣剛好買得起 Sharp Sword。買不買，結局差很多。）")
