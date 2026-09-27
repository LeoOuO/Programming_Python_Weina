# ===== Lesson 6  Practice 1：填空（迷你版遊戲）=====
# 這是一個縮小版的 Slime Tower，骨架都在，把 ____ 填掉就能玩。
# 執行  python3 practice-1.py
#
# 兩種錯誤訊息：
#   SyntaxError -> 關鍵字（return 之類）那一格還沒填
#   NameError: name '____' is not defined -> 這一行的值還沒填
import random

# --- 1. 遊戲狀態 ------------------------------------------------------
game = {
    "hero": {"name": "Hero", "hp": 50, "atk": 10},
    "gold": ____,                # 一開始給玩家 20 金幣
    "floor": 1,
}

print(game["hero"][____])        # 想印出 Hero


# --- 2. 顯示狀態的函式 ------------------------------------------------
def show():
    hero = game["hero"]
    print(f"{hero['name']}  HP {hero['hp']}  ATK {hero['atk']}  {game['gold']}g")

____()                           # 呼叫上面那個函式


# --- 3. 傷害函式 ------------------------------------------------------
def hero_damage():
    atk = game["hero"]["atk"]
    ____ random.randint(atk - 2, atk + 2)    # 把算好的傷害交回去

print("test damage:", hero_damage())


# --- 4. 一場戰鬥 ------------------------------------------------------
def battle(monster):
    """贏了回傳 True，輸了回傳 False"""
    hp = monster["hp"]
    print(f"\nA {monster['name']} appears! HP {hp}")

    while hp > 0 and game["hero"]["hp"] > ____:     # 兩邊都還活著才繼續
        damage = hero_damage()
        hp = hp - damage
        print(f"  you hit for {damage}, monster has {max(hp, 0)} HP")

        if hp <= 0:
            break

        game["hero"]["hp"] = game["hero"]["hp"] - monster[____]   # 怪物的攻擊力
        print(f"  it hits back, you have {game['hero']['hp']} HP")

    if game["hero"]["hp"] <= 0:
        return False
    game["gold"] = game["gold"] + monster["gold"]
    print(f"  {monster['name']} defeated! +{monster['gold']}g")
    return ____                  # 打贏了要回傳什麼？


# --- 5. 怪物圖鑑 ------------------------------------------------------
monsters = [
    {"name": "Slime",  "hp": 20, "atk": 5, "gold": 20},
    {"name": "Goblin", "hp": 30, "atk": 7, "gold": 30},
]


# --- 6. 主迴圈 --------------------------------------------------------
for monster in ____:             # 要跑哪一個清單？
    won = battle(monster)
    if not won:
        print("\nGAME OVER")
        break
else:
    print("\nYou cleared the tower!")
    show()
