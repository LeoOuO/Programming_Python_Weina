# ===== Example 2: keeping the whole game in one place =====
# 生字：state 狀態 · progress 進度 · unlock 解鎖 · record 紀錄
#
# 遊戲進行中的所有資料，放在一個字典裡叫做「遊戲狀態」。
# 好處：要存檔、要重來、要顯示，通通只要處理這一包。

game = {
    "hero": {"name": "Luna", "hp": 100, "max_hp": 100, "atk": 15},
    "gold": 50,
    "bag": ["Potion"],
    "room": 1,                     # 現在在第幾關
    "wins": 0,                     # 打贏幾場
}

# 字典裡面還有字典，一層一層拿
print(game["hero"]["name"])
print(game["hero"]["hp"])
print(game["bag"])

# 打贏一場：三個地方一起更新
game["wins"] = game["wins"] + 1
game["gold"] = game["gold"] + 40
game["room"] = game["room"] + 1
print(game)


def show_status(game):             # 有了狀態字典，顯示就只是一個函式
    hero = game["hero"]
    print(f"\n{hero['name']}  HP {hero['hp']}/{hero['max_hp']}  "
          f"ATK {hero['atk']}  {game['gold']}g  room {game['room']}")


show_status(game)

# Try it 試試看：
# 1. 在 game 裡加一項 "potions"，數量 2
# 2. 寫一個 is_game_over(game) 函式，血量 <= 0 時回傳 True
