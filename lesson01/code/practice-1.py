# ===== Lesson 1  Practice 1：填空 =====
# 程式已經寫好了，只要把每個 ____ 換成正確的東西。
#
# 怎麼知道還有哪裡沒填？直接執行：
#   python3 practice-1.py
# 沒填的地方會說  NameError: name '____' is not defined
# 訊息最後會告訴你是第幾行（line N），一次填一個、填完就執行一次。

# --- 1. 角色卡 --------------------------------------------------------
# 把三個變數填好，讓最後一行印出：  Luna is a Mage with 80 HP

name = ____              # 填一個名字，記得加引號，例如 "Luna"
job = ____               # 職業，例如 "Mage"（法師）
hp = ____                # 血量，填一個數字，不要加引號

print(f"{name} is a {job} with {hp} HP")


# --- 2. 攻擊力公式 ----------------------------------------------------
# 攻擊力 = 10 + 等級 × 2

level = 5
atk = 10 + level * ____          # 填一個數字

print(f"level {level} -> atk {atk}")      # 應該印出 atk 20


# --- 3. 把文字變成數字 ------------------------------------------------
# input() 拿到的是文字，要先變成數字才能算數學

answer = input("How many potions do you have? ")
potions = ____(answer)           # 填一個函式名稱，把文字變成整數

print(f"You have {potions} potions, {potions * 2} in two bags")


# --- 4. 判斷 ----------------------------------------------------------
# 血量 >= 70 印 "Looking good"，30~69 印 "Be careful"，其他印 "Danger!"

hp = 45

if hp >= 70:
    print("Looking good")
elif hp >= ____:                 # 填一個數字
    print(____)                  # 填要印的話，記得加引號
else:
    print("Danger!")


# --- 5. 兩個條件 ------------------------------------------------------
# 「血量低於 30 而且 還有藥水」才喝藥水

hp = 20
potions = 3

if hp < ____ and potions > 0:    # 填門檻數字
    print("Drink a potion!")
else:
    print("Keep fighting")

# 想一想：這裡為什麼是 and 不是 or？
# 把 and 改成 or，再把 potions 改成 0 執行看看，結果哪裡怪怪的？
