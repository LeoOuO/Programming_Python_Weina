# ===== Example 2: keeping the whole game in one place =====
#
# All the data of a game in progress goes into one dictionary:
# the game state.
# Saving, restarting, showing the status - all of them only touch this one box.
#   game state 遊戲狀態

game = {
    "hero": {"name": "Luna", "hp": 100, "max_hp": 100, "atk": 15},
    "gold": 50,
    "bag": ["Potion"],
    "room": 1,                     # which room we are in
    "wins": 0,                     # battles won so far
}

# a dictionary inside a dictionary - take it one layer at a time
print(game["hero"]["name"])
print(game["hero"]["hp"])
print(game["bag"])

# winning a battle updates three things at once
game["wins"] = game["wins"] + 1
game["gold"] = game["gold"] + 40
game["room"] = game["room"] + 1
print(game)


def show_status(game):             # with a state dictionary, showing it is just one function
    hero = game["hero"]
    print(f"\n{hero['name']}  HP {hero['hp']}/{hero['max_hp']}  "
          f"ATK {hero['atk']}  {game['gold']}g  room {game['room']}")


show_status(game)

# Try it:
# 1. Add a "potions" item to game, with 2 in it
# 2. Write is_game_over(game) that returns True when the hp is 0 or less
