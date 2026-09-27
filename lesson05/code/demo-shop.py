# ===== Lesson 5 final demo: fight, loot, shop =====
#
# Every character and every item 道具 is a dictionary, so all the data
# for one thing stays in one place.
# The loop: fight a monster -> take the gold -> go shopping -> fight again
# Run it with:  python3 demo-shop.py
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


# ---------- the hero: one dictionary holds everything ----------
hero = {
    "name": "Hero",
    "hp": 85,
    "max_hp": 85,
    "atk": 13,
    "gold": 60,
    "potions": 1,
}

# ---------- the monster book 圖鑑: a list of dictionaries ----------
monsters = [
    {"name": "Slime",  "hp": 26, "atk": 7,  "gold": 30},
    {"name": "Goblin", "hp": 40, "atk": 10, "gold": 55},
    {"name": "Ogre",   "hp": 56, "atk": 13, "gold": 80},   # ogre 食人魔
]

# ---------- the shop: name -> data ----------
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
    """Fight one monster. Returns True and takes the gold if you win."""
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
    """Visit the shop. Keep buying until you leave."""
    while True:
        print("\n" + "=" * 42)
        print(f"  SHOP        you have {hero['gold']} gold")
        print("=" * 42)
        names = []                      # collect the names so we can pick by number
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

        # turn the number the player typed into an item name
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


# ---------- the main program ----------
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
