# ===== Example 2: a whole party (a list of dictionaries) =====
# 生字：party 隊伍 · each 每一個 · strongest 最強的

# 清單裡面放字典 = 一整隊角色，每個角色都有自己的一組資料。
party = [
    {"name": "Luna",  "hp": 100, "atk": 18},
    {"name": "Borin", "hp": 140, "atk": 12},
    {"name": "Sera",  "hp": 80,  "atk": 24},
]

print(party[0])                # 第一個角色（整組資料）
print(party[0]["name"])        # 第一個角色的名字

print()
for member in party:           # 一個一個拿出來，每個都是字典
    print(f"{member['name']:<6} HP {member['hp']:>4}  ATK {member['atk']}")

# 找出攻擊力最高的
print()
best = party[0]
for member in party:
    if member["atk"] > best["atk"]:
        best = member
print(f"Strongest: {best['name']} ({best['atk']} ATK)")

# 全隊總血量
total = 0
for member in party:
    total = total + member["hp"]
print(f"Party total HP: {total}")

# Try it 試試看：
# 1. 在隊伍裡加第四個角色
# 2. 找出血量最低的那個（把 > 改成 <，想一想為什麼）
# 3. 讓全隊每個人的 hp 都加 10
