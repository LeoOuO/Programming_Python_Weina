# ===== Lesson 2  Practice 1：填空 =====
# 把每個 ____ 換成正確的東西。執行  python3 practice-1.py
# 沒填的地方會說  NameError: name '____' is not defined，訊息裡有行號。
import random

# --- 1. 重複五次 ------------------------------------------------------
# 印出五行 "Attack!"

for i in range(____):            # 填次數
    print("Attack!")


# --- 2. range 的起點和終點 --------------------------------------------
# 要印出 1 2 3 4 5（注意：終點那個數字不會被印出來）

for i in range(1, ____):         # 填終點
    print(i)


# --- 3. 連段傷害 ------------------------------------------------------
# 第 i 下的傷害是 8 的 i 倍：8, 16, 24, 32, 40

atk = 8
for i in range(1, 6):
    damage = atk * ____          # 填一個變數名稱
    print(f"Hit {i}: {damage}")


# --- 4. 累加 ----------------------------------------------------------
# 把五次的傷害加起來，最後印出 total 120

total = ____                     # 起點要填多少？
for i in range(1, 6):
    damage = 8 * i
    total = ____ + damage        # 填一個變數名稱
print(f"total {total}")


# --- 5. 亂數 ----------------------------------------------------------
# 隨機一個 1 到 6 的點數（像骰子一樣）

roll = random.____(1, 6)         # 填函式名稱：randint 還是 choice？
print(f"You rolled {roll}")

drops = ["Gold", "Potion", "Nothing"]
loot = random.____(drops)        # 從清單裡挑一個，要用哪個？
print(f"You found: {loot}")


# --- 6. while 迴圈 ----------------------------------------------------
# 怪物有 50 點血，每下打 10 點，打到血量 <= 0 為止

hp = 50
hits = 0
stop_at = ____                   # 打到血量小於等於多少就停？填 0
while hp > stop_at:              # 注意：條件寫的是「繼續」的條件
    hits = hits + 1
    hp = hp - 10
print(f"It took {hits} hits")    # 應該是 5

# 想一想：如果把  hp = hp - 10  這一行刪掉會發生什麼事？
