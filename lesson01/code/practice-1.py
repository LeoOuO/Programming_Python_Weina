# ===== Lesson 1  Practice 1: fill in the blanks =====
# ===== 第 1 堂 練習一：填空 =====
#
# The program is already written. Just replace every  ?  with the right thing.
# 程式已經寫好了，只要把每個  ?  換成正確的東西。
#
# Every  ?  is a blank you have to fill in.
# VS Code underlines them in red, so you can see what is still missing.
# Running the file stops at the first  ?  with a SyntaxError and tells you
# the line number. Fill one in, run it, fill in the next.
#
# 每一個  ?  都是要你填的空格。VS Code 會用紅色底線標出來，
# 一眼就看得到還有哪裡沒寫。執行的話會在第一個 ? 停下來，
# 出現 SyntaxError 並告訴你行號。填一個、執行一次，再填下一個。

# --- 1. Character card / 角色卡 ---------------------------------------
# Fill in the three variables so the last line prints:  Luna is a Mage with 80 HP
# 把三個變數填好，讓最後一行印出：Luna is a Mage with 80 HP

name = ?              # a name, in quotes, e.g. "Luna"  名字，記得加引號
job = ?               # a job, e.g. "Mage"  職業
hp = ?                # a number, no quotes  血量，填數字不要加引號

print(f"{name} is a {job} with {hp} HP")


# --- 2. Attack formula / 攻擊力公式 -----------------------------------
# attack = 10 + level x 2
# 攻擊力 = 10 + 等級 × 2

level = 5
atk = 10 + level * ?          # fill in a number  填一個數字

print(f"level {level} -> atk {atk}")      # should print atk 20


# --- 3. Text into a number / 把文字變成數字 ---------------------------
# input() gives you text. Turn it into a number before doing maths.
# input() 拿到的是文字，要先變成數字才能算數學。

answer = input("How many potions do you have? ")
potions = ?(answer)           # which function turns text into a whole number?
                                 # 哪個函式可以把文字變成整數？

print(f"You have {potions} potions, {potions * 2} in two bags")


# --- 4. Three-way decision / 三段判斷 ---------------------------------
# hp >= 70 -> "Looking good",  30 to 69 -> "Be careful",  else -> "Danger!"
# 血量 >= 70 印 "Looking good"，30~69 印 "Be careful"，其他印 "Danger!"

hp = 45

if hp >= 70:
    print("Looking good")
elif hp >= ?:                 # fill in a number  填一個數字
    print(?)                  # what should it print? in quotes  要印什麼？記得加引號
else:
    print("Danger!")


# --- 5. Two conditions / 兩個條件 -------------------------------------
# Drink a potion only when the HP is below 30 AND there is a potion left.
# 「血量低於 30 而且 還有藥水」才喝藥水。

hp = 20
potions = 3

if hp < ? and potions > 0:    # fill in the number  填門檻數字
    print("Drink a potion!")
else:
    print("Keep fighting")

# Think about it: why is this "and" and not "or"?
# Change it to or, set potions to 0, run it - what goes wrong?
# 想一想：這裡為什麼是 and 不是 or？
# 把 and 改成 or、potions 改成 0 執行看看，結果哪裡怪怪的？
