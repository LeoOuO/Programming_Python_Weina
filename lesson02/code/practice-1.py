# ===== Lesson 2  Practice 1: fill in the blanks =====
# ===== 第 2 堂 練習一：填空 =====
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

# --- 1. Repeat five times / 重複五次 ----------------------------------
# Print "Attack!" five times.  印出五行 "Attack!"

for i in range(?):            # how many times?  填次數
    print("Attack!")


# --- 2. Start and end of range / range 的起點和終點 -------------------
# Print 1 2 3 4 5.  Careful: the end number is NOT printed.
# 要印出 1 2 3 4 5（注意：終點那個數字不會被印出來）

for i in range(1, ?):         # fill in the end  填終點
    print(i)


# --- 3. Combo damage / 連段傷害 ---------------------------------------
# Hit number i does 8 times i damage: 8, 16, 24, 32, 40
# 第 i 下的傷害是 8 的 i 倍

atk = 8
for i in range(1, 6):
    damage = atk * ?          # a variable name  填一個變數名稱
    print(f"Hit {i}: {damage}")


# --- 4. Adding up / 累加 ----------------------------------------------
# Add up the five hits. The total should be 120.
# 把五次的傷害加起來，最後印出 total 120

total = ?                     # where does the total start?  起點填多少？
for i in range(1, 6):
    damage = 8 * i
    total = ? + damage        # a variable name  填一個變數名稱
print(f"total {total}")


# --- 5. Randomness / 亂數 ---------------------------------------------
# Roll a random number from 1 to 6, like a dice.
# 隨機一個 1 到 6 的點數

roll = random.?(1, 6)         # randint or choice?  填函式名稱
print(f"You rolled {roll}")

drops = ["Gold", "Potion", "Nothing"]
loot = random.?(drops)        # pick one from a list - which one?  從清單裡挑一個
print(f"You found: {loot}")


# --- 6. The while loop / while 迴圈 -----------------------------------
# The monster has 50 HP. Every hit does 10. Keep hitting until it is down.
# 怪物有 50 點血，每下打 10 點，打到血量 <= 0 為止

hp = 50
hits = 0
stop_at = ?                   # stop when the HP drops to what?  填 0
while hp > stop_at:              # note: this is the condition to CONTINUE  這是「繼續」的條件
    hits = hits + 1
    hp = hp - 10
print(f"It took {hits} hits")    # should be 5  應該是 5

# Think about it: what happens if you delete the line  hp = hp - 10 ?
# 想一想：如果把 hp = hp - 10 這一行刪掉會發生什麼事？
