# ===== Lesson 3  Practice 1: fill in the blanks =====
# ===== 第 3 堂 練習一：填空 =====
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

bag = ["Wooden Sword", "Red Potion", "Bread", "Shield"]

# --- 1. Take an item by position / 用位置拿東西 -----------------------
# Positions start at 0!  位置從 0 開始數！

print(bag[?])                 # should print Wooden Sword
print(bag[?])                 # should print Bread
print(bag[-1])                   # already written - what does it print?  印出什麼？


# --- 2. How many items / 有幾樣東西 -----------------------------------

print(f"You are carrying {?(bag)} items")     # a function name  填函式名稱


# --- 3. Pick up and drop / 撿東西、丟東西 -----------------------------

bag.?("Iron Sword")           # picked it up -> add to the end  加到最後面
print(bag)

bag.?("Bread")                # ate the bread -> take it out  拿出來
print(bag)


# --- 4. Go through the list / 走訪整個清單 ----------------------------
# Print  1. Swordsman   2. Mage   3. Archer

party = ["Swordsman", "Mage", "Archer"]

for i in range(len(party)):
    print(f"{i + ?}. {party[i]}")      # numbering starts at 1  編號從 1 開始


# --- 5. Stats / 統計 --------------------------------------------------

hp_list = [120, 70, 90, 80]

print(f"total   {?(hp_list)}")         # the sum  總和
print(f"highest {?(hp_list)}")         # the biggest
print(f"lowest  {?(hp_list)}")         # the smallest
print(f"average {sum(hp_list) / ?(hp_list)}")   # average = sum / how many


# --- 6. Collect the results / 收集結果 --------------------------------
# Draw five times and collect every card into the results list.
# 抽五次，把抽到的卡收進 results 清單。

pool = ["Rare Card"] * 5 + ["Common Card"] * 95

results = ?                   # an empty list - how is that written?  空清單
for i in range(5):
    card = random.choice(pool)
    results.?(card)           # put the card in  把抽到的放進去
print(results)

# Think about it: what if  results = []  moved INSIDE the for loop?
# 想一想：如果把 results = [] 搬到 for 迴圈裡面，結果會變怎樣？
