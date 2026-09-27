# ===== Example 1: a character sheet (dictionary) =====
#
# A list is a row of things, taken out by position: 0, 1, 2.
# A dictionary is a set of named data, taken out by name -
# just like looking a word up in a real dictionary.
#   dictionary 字典 · key 鍵（名稱）· value 值

hero = {                       # curly brackets { }; every item is  "name": value
    "name": "Luna",
    "hp": 100,
    "atk": 18,
    "gold": 50,
}

print(hero)
print(hero["name"])            # take a value by NAME, not by a number
print(hero["hp"])

# change one item
hero["hp"] = hero["hp"] - 30   # took a hit
print(f"{hero['name']} now has {hero['hp']} HP")

# add a new item (writing a name that was not there adds it)
hero["level"] = 5
print(hero)

# check whether an item exists
if "gold" in hero:
    print(f"gold: {hero['gold']}")

# Try it:
# 1. Change hero into your own character and add a "job" item
# 2. Give the hero 100 more gold, then print it
# 3. What happens if you print hero["mana"]? Read the error
#    (KeyError = there is no such key)
#   curly brackets 大括號
