# ===== Lesson 3  Practice 1：填空 =====
# 把每個 ____ 換成正確的東西。執行  python3 practice-1.py
import random

bag = ["Wooden Sword", "Red Potion", "Bread", "Shield"]

# --- 1. 用位置拿東西 --------------------------------------------------
# 位置從 0 開始數！

print(bag[____])                 # 想印出 Wooden Sword
print(bag[____])                 # 想印出 Bread
print(bag[-1])                   # 這個已經幫你寫好了，印出什麼？


# --- 2. 有幾樣東西 ----------------------------------------------------

print(f"You are carrying {____(bag)} items")     # 填函式名稱


# --- 3. 撿東西、丟東西 ------------------------------------------------

bag.____("Iron Sword")           # 撿到鐵劍 -> 加到最後面
print(bag)

bag.____("Bread")                # 麵包吃掉了 -> 拿出來
print(bag)


# --- 4. 走訪整個清單 --------------------------------------------------
# 印出  1. Swordsman   2. Mage   3. Archer

party = ["Swordsman", "Mage", "Archer"]

for i in range(len(party)):
    print(f"{i + ____}. {party[i]}")      # 編號要從 1 開始，該加多少？


# --- 5. 統計 ----------------------------------------------------------

hp_list = [120, 70, 90, 80]

print(f"total   {____(hp_list)}")         # 總和
print(f"highest {____(hp_list)}")         # 最大
print(f"lowest  {____(hp_list)}")         # 最小
print(f"average {sum(hp_list) / ____(hp_list)}")   # 平均 = 總和 ÷ 幾個


# --- 6. 收集結果 ------------------------------------------------------
# 抽五次，把抽到的卡收進 results 清單

pool = ["Rare Card"] * 5 + ["Common Card"] * 95

results = ____                   # 一開始要是一個空清單，怎麼寫？
for i in range(5):
    card = random.choice(pool)
    results.____(card)           # 把抽到的放進去
print(results)

# 想一想：如果把  results = []  那一行搬到 for 迴圈「裡面」，結果會變怎樣？
