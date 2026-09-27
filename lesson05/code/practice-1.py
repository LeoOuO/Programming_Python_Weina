# ===== Lesson 5  Practice 1：填空 =====
# 把每個 ____ 換成正確的東西。執行  python3 practice-1.py

monster = {
    "name": "Goblin",
    "hp": 45,
    "atk": 12,
}

# --- 1. 用名稱拿值 ----------------------------------------------------

print(monster[____])             # 想印出 Goblin，填名稱（記得加引號）
print(monster[____])             # 想印出 45


# --- 2. 改一項 --------------------------------------------------------
# 怪物被打了 10 點

monster["hp"] = monster["hp"] - ____
print(f"{monster['name']} has {monster['hp']} HP")     # 應該是 35


# --- 3. 加一項 --------------------------------------------------------
# 幫怪物加上「掉落金幣」這個資料，值是 30

monster[____] = 30               # 填新的名稱，叫 gold
print(monster)


# --- 4. 清單裡放字典 --------------------------------------------------

party = [
    {"name": "Luna",  "hp": 100},
    {"name": "Borin", "hp": 140},
]

print(party[0][____])            # 想印出 Luna
print(party[1]["hp"])            # 這行已經寫好，印出什麼？


# --- 5. 走訪整隊 ------------------------------------------------------

for member in ____:              # 要跑哪一個清單？
    print(f"{member['name']} has {member['hp']} HP")


# --- 6. 總血量 --------------------------------------------------------

total = ____                     # 起點填多少？
for member in party:
    total = total + member[____]    # 要加哪一項？
print(f"total HP {total}")       # 應該是 240


# --- 7. 買東西 --------------------------------------------------------

prices = {"Potion": 20, "Shield": 60}
gold = 50

if prices["Potion"] <= ____:     # 跟什麼比才知道買不買得起？
    gold = gold - prices["Potion"]
    print(f"Bought a Potion, {gold} gold left")

# 想一想：字典和清單，什麼時候用哪一個？
