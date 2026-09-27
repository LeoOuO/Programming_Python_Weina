# ===== Lesson 6  Practice 1: fill in the blanks (a mini game) =====
# ===== 第 6 堂 練習一：填空（迷你版遊戲）=====
#
# This is a small version of Slime Tower. The skeleton is all here -
# fill in every  ?  and you can play it.
# 這是縮小版的 Slime Tower，骨架都在，把每個  ?  填掉就能玩。
#
# Every  ?  is a blank you have to fill in.
# VS Code underlines them in red, so you can see what is still missing.
# Running the file stops at the first  ?  with a SyntaxError and tells you
# the line number. Fill one in, run it, fill in the next.
#
# 每一個  ?  都是要你填的空格。VS Code 會用紅色底線標出來，
# 一眼就看得到還有哪裡沒寫。執行的話會在第一個 ? 停下來，
# 出現 SyntaxError 並告訴你行號。填一個、執行一次，再填下一個。
import random

# --- 1. The game state / 遊戲狀態 -------------------------------------
game = {
    "hero": {"name": "Hero", "hp": 50, "atk": 10},
    "gold": ?,                # the player starts with 20 gold  一開始 20 金幣
    "floor": 1,
}

print(game["hero"][?])        # should print Hero


# --- 2. A function that shows the status / 顯示狀態的函式 -------------
def show():
    hero = game["hero"]
    print(f"{hero['name']}  HP {hero['hp']}  ATK {hero['atk']}  {game['gold']}g")

?()                           # call the function above  呼叫上面那個函式


# --- 3. A damage function / 傷害函式 ----------------------------------
def hero_damage():
    atk = game["hero"]["atk"]
    ? random.randint(atk - 2, atk + 2)    # hand the damage back  把傷害交回去

print("test damage:", hero_damage())


# --- 4. One battle / 一場戰鬥 -----------------------------------------
def battle(monster):
    """True = you won, False = you lost  贏了回傳 True，輸了回傳 False"""
    hp = monster["hp"]
    print(f"\nA {monster['name']} appears! HP {hp}")

    while hp > 0 and game["hero"]["hp"] > ?:     # both still alive  兩邊都還活著
        damage = hero_damage()
        hp = hp - damage
        print(f"  you hit for {damage}, monster has {max(hp, 0)} HP")

        if hp <= 0:
            break

        game["hero"]["hp"] = game["hero"]["hp"] - monster[?]   # the monster's attack
        print(f"  it hits back, you have {game['hero']['hp']} HP")

    if game["hero"]["hp"] <= 0:
        return False
    game["gold"] = game["gold"] + monster["gold"]
    print(f"  {monster['name']} defeated! +{monster['gold']}g")
    return ?                  # what do we return after winning?  打贏了回傳什麼？


# --- 5. The monster book / 怪物圖鑑 -----------------------------------
monsters = [
    {"name": "Slime",  "hp": 20, "atk": 5, "gold": 20},
    {"name": "Goblin", "hp": 30, "atk": 7, "gold": 30},
]


# --- 6. The main loop / 主迴圈 ----------------------------------------
for monster in ?:             # which list?  要跑哪一個清單？
    won = battle(monster)
    if not won:
        print("\nGAME OVER")
        break
else:
    print("\nYou cleared the tower!")
    show()
