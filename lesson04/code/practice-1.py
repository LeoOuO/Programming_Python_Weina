# ===== Lesson 4  Practice 1：填空 =====
# 把每個 ____ 換成正確的東西。執行  python3 practice-1.py
#
# 這次會看到兩種錯誤訊息，它們在講不同的事：
#   SyntaxError  -> 文法還不完整，通常是關鍵字（def / return）那一格還沒填
#   NameError: name '____' is not defined  -> 這一行的值還沒填
# 兩種訊息都會告訴你行號，照著一格一格填就好。
import random

# --- 1. 定義一個函式 --------------------------------------------------
# 印出遊戲標題

____ show_title():               # 定義函式要用哪個關鍵字？
    print("*** DUNGEON QUEST ***")

show_title()                     # 這一行是「呼叫」，已經幫你寫好


# --- 2. 參數 ----------------------------------------------------------
# 讓函式可以印出不同角色的名字

def introduce(____):             # 提示：下面那行用到什麼名字，參數就要叫什麼
    print(f"I am {name}, the hero!")

introduce("Luna")                # 應該印出 I am Luna, the hero!


# --- 3. 回傳 ----------------------------------------------------------
# 算出總血量，把答案交回去

def total_hp(base, bonus):
    result = base + bonus
    ____ result               # 把 result 交回去要用哪個關鍵字？

print(total_hp(100, 20))         # 應該印出 120


# --- 4. 用回傳值 ------------------------------------------------------

def double(n):
    return n * 2

answer = ____(21)                # 呼叫上面那個函式，讓 answer 變成 42
print(answer)


# --- 5. 回傳 True / False ---------------------------------------------

def is_dead(hp):
    return hp <= ____            # 血量小於等於多少算倒下？

print(is_dead(0))                # True
print(is_dead(10))               # False


# --- 6. 兩個回傳值 ----------------------------------------------------

def punch(atk):
    damage = random.randint(atk - 1, atk + 1)
    return damage, "Punch!"      # 一次回傳兩個東西

d, text = ____(10)               # 呼叫 punch
print(text, d)

# 想一想：函式裡面用 print 和用 return，差在哪裡？
