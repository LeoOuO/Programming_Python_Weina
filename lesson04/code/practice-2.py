# ===== Lesson 4  Practice 2: write it yourself =====
# ===== 第 4 堂 練習二：自己完成 =====
#
# No skeleton this time - start from an empty line.
# 這次沒有骨架，從空白開始寫。
#   python3 practice-2.py
import random

# --- 1. A greeting function / 打招呼函式 ------------------------------
# Write welcome(name) that prints "Welcome to the dungeon, <name>!"
# Then call it three times with three different names.
# 寫一個 welcome(name) 函式，用三個不同的名字各呼叫一次。

# your code here / 你的程式寫在這裡


# --- 2. A function that returns / 會回傳答案的函式 --------------------
# Write exp_needed(level) that returns level * 100.
# Use a for loop to print how much levels 1 to 5 need.
# 寫一個 exp_needed(level) 回傳 level * 100，用 for 印出 1~5 級各需要多少。

# your code here / 你的程式寫在這裡


# --- 3. A damage function / 傷害函式 ----------------------------------
# Write damage_of(atk, defense):
#   damage = attack - defense, but never less than 1
#   return the answer
# Test: damage_of(20, 5) is 15,  damage_of(5, 20) is 1
# 傷害 = 攻擊 - 防禦，但最少是 1，算完 return 回去。

# your code here / 你的程式寫在這裡


# --- 4. A True / False function / 回傳 True 或 False ------------------
# Write is_critical(roll) that returns True when roll >= 90.
# Roll ten times, use the function, and print how many criticals you got.
# 寫一個 is_critical(roll)，擲 10 次骰子，印出總共暴擊幾次。

# your code here / 你的程式寫在這裡


# --- 5. Your own skill / 自己的技能 -----------------------------------
# Like the ones in 04-skills.py, write your own skill function:
#   it takes atk and returns (damage, message)
#   give it some randomness (a critical, a miss, a damage range...)
# Call it 5 times and print every message.
# 照 04-skills.py 的樣子寫一個自己的技能，接收 atk、回傳 (傷害, 訊息)，呼叫 5 次。

# your code here / 你的程式寫在這裡


# --- 6. Challenge: chain two functions / 挑戰：串起兩個函式 -----------
# Using damage_of from 3 and is_critical from 4, write attack(atk, defense):
#   roll a 1-100 dice
#   if it is a critical, double the damage
#   return the final damage
# Call it 10 times and print the results.
# 用第 3、4 題的函式寫一個 attack(atk, defense)，呼叫 10 次印出結果。

# your code here / 你的程式寫在這裡
