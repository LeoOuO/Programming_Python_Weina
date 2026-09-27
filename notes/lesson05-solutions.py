# ===== Lesson 5 practice - reference answers (TEACHER ONLY) =====
# --- Practice 1（填空）解答 ------------------------------------------
# 1. monster["name"]  /  monster["hp"]
# 2. monster["hp"] - 10
# 3. monster["gold"] = 30
# 4. party[0]["name"]        （party[1]["hp"] 印出 140）
# 5. for member in party:
# 6. total = 0  /  member["hp"]
# 7. if prices["Potion"] <= gold:
#    想一想：資料有「名稱」用字典（角色、商品），一排同類的東西用清單（隊伍、背包）。
#
# 常見錯誤：f-string 裡面引號打架 -> f"{hero["name"]}" 會壞掉，
#           要寫 f"{hero['name']}"（外雙內單）。她一定會踩到。

# --- Practice 2 ----------------------------------------------------
hero = {"name": "Luna", "hp": 100, "atk": 18, "gold": 40}
print(f"{hero['name']}  HP {hero['hp']}  ATK {hero['atk']}  {hero['gold']}g")

# 2.
hero["hp"] = hero["hp"] - 25
print(hero["hp"])                                   # 75
hero["hp"] = min(hero["hp"] + 30, 100)              # 也可以用 if 寫
print(hero["hp"])                                   # 100

# 3.
monsters = [
    {"name": "Slime",  "hp": 30, "gold": 20},
    {"name": "Goblin", "hp": 45, "gold": 35},
    {"name": "Ogre",   "hp": 70, "gold": 60},
]
for m in monsters:
    print(f"{m['name']:<8} HP {m['hp']:>3}  {m['gold']}g")

# 4.  跟第 3 堂「找最大」同一招，只是換成字典
best = monsters[0]
for m in monsters:
    if m["gold"] > best["gold"]:
        best = m
print(f"richest: {best['name']} ({best['gold']}g)")

# 5.
for m in monsters:
    hero["gold"] = hero["gold"] + m["gold"]
print(f"gold now {hero['gold']}")                   # 40 + 115 = 155

# 6.
prices = {"Potion": 20, "Shield": 60, "Sword": 90}
bag = []
for item in prices:
    print(f"{item:<8} {prices[item]}g")

want = "Shield"
if prices[want] <= hero["gold"]:
    hero["gold"] = hero["gold"] - prices[want]
    bag.append(want)
    print(f"bought {want}, {hero['gold']}g left")
else:
    print(f"cannot afford {want}")

# 7.  陷阱：邊買邊扣錢，所以後面的可能就買不起了 —— 這正是要她體會的
for item in prices:
    if prices[item] <= hero["gold"]:
        hero["gold"] = hero["gold"] - prices[item]
        bag.append(item)
print(bag, f"{hero['gold']}g left")
