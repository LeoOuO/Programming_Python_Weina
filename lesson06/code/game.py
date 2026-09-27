# =====================================================================
#  SLIME  TOWER  -  your first complete game
#
#  Everything in here comes from lessons 1 to 5:
#    variables and if        (lesson 1)
#    for / while / random    (lesson 2)
#    lists                   (lesson 3)
#    functions               (lesson 4)
#    dictionaries            (lesson 5)
#
#  Run it with:  python3 game.py
# =====================================================================
import random
import time

SPEED = 0.3          # set it to 0 to skip the animation
MAX_POTIONS = 3      # you can only carry 3 potions 藥水

# ------------------------------------------------------------------ data
game = {
    "hero": {"name": "Hero", "hp": 60, "max_hp": 60, "atk": 12},
    "gold": 30,
    "potions": 1,
    "floor": 1,          # which floor we are on
}

MONSTERS = [
    {"name": "Slime",      "hp": 22, "atk": 6,  "gold": 25},
    {"name": "Bat",        "hp": 28, "atk": 8,  "gold": 30},
    {"name": "Goblin",     "hp": 36, "atk": 10, "gold": 40},
    {"name": "Orc",        "hp": 48, "atk": 13, "gold": 55},
    {"name": "Slime King", "hp": 70, "atk": 15, "gold": 99},   # the boss on the top floor
]

SHOP = {
    "Potion":      {"price": 25, "text": "+1 potion"},
    "Sharp Sword": {"price": 50, "text": "ATK +4"},
    "Big Shield":  {"price": 60, "text": "max HP +20, full heal"},
}


# ------------------------------------------------------------ small helpers
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
    """Work out this hit. 10% chance of a critical hit."""
    atk = game["hero"]["atk"]
    if random.randint(1, 100) <= 10:
        return atk * 2, True
    return random.randint(atk - 2, atk + 2), False


def drink_potion():
    """Drink a potion. Returns False when there are none left."""
    if game["potions"] <= 0:
        return False
    hero = game["hero"]
    game["potions"] = game["potions"] - 1
    hero["hp"] = min(hero["hp"] + 30, hero["max_hp"])
    say(f"  You drink a potion -> {hero['hp']} HP")
    return True


# ---------------------------------------------------------------- battle
def battle(monster):
    """Fight one monster. True = you won, False = you went down."""
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
                continue                      # nothing happened, so it costs no turn
        elif choice == "3":
            if random.randint(1, 100) <= 50:  # 50% chance to escape
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

        # the monster strikes back
        damage = random.randint(monster["atk"] - 2, monster["atk"] + 2)
        hero["hp"] = hero["hp"] - damage
        say(f"  The {monster['name']} hits you for {damage}")
        show_status()

    if not is_alive(hero["hp"]):
        return False

    game["gold"] = game["gold"] + monster["gold"]
    say(f"\n  {monster['name']} defeated!   +{monster['gold']} gold")
    return True


# ------------------------------------------------------------------ shop
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


# ---------------------------------------------------------- main program
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

    shop()                                   # there is a shop before every floor

    won = battle(MONSTERS[floor])
    if not is_alive(game["hero"]["hp"]):
        print("\n" + "=" * 46)
        print(f"  You fell on floor {game['floor']}...   GAME OVER")
        print(f"  Gold collected: {game['gold']}")
        print("=" * 46)
        break
    if not won:                              # you escaped, so this floor does not count
        say("  You run back down the stairs and try again.")

    # rest after clearing the floor
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
