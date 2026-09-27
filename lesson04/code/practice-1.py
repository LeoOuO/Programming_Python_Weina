# ===== Lesson 4  Practice 1: fill in the blanks =====
# ===== 第 4 堂 練習一：填空 =====
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

# --- 1. Define a function / 定義一個函式 ------------------------------
# It prints the game title.  印出遊戲標題

? show_title():               # which keyword defines a function?  用哪個關鍵字？
    print("*** DUNGEON QUEST ***")

show_title()                     # this line CALLS it - already written  這行是呼叫


# --- 2. Parameters / 參數 ---------------------------------------------
# So the function can print any character's name.  讓函式可以印不同角色的名字

def introduce(?):             # hint: the line below uses a name - use the same one
                                 # 提示：下面那行用到什麼名字，參數就要叫什麼
    print(f"I am {name}, the hero!")

introduce("Luna")                # should print: I am Luna, the hero!


# --- 3. Return / 回傳 -------------------------------------------------
# Work out the total HP and hand the answer back.  算出總血量，把答案交回去

def total_hp(base, bonus):
    result = base + bonus
    ? result               # which keyword hands result back?  用哪個關鍵字？

print(total_hp(100, 20))         # should print 120


# --- 4. Use the returned value / 用回傳值 -----------------------------

def double(n):
    return n * 2

answer = ?(21)                # call the function above so answer becomes 42
print(answer)


# --- 5. Return True or False / 回傳 True 或 False ---------------------

def is_dead(hp):
    return hp <= ?            # down when the HP drops to what?  多少算倒下？

print(is_dead(0))                # True
print(is_dead(10))               # False


# --- 6. Two returned values / 兩個回傳值 ------------------------------

def punch(atk):
    damage = random.randint(atk - 1, atk + 1)
    return damage, "Punch!"      # two things at once  一次回傳兩個

d, text = ?(10)               # call punch
print(text, d)

# Think about it: inside a function, what is the difference between print and return?
# 想一想：函式裡面用 print 和用 return，差在哪裡？
