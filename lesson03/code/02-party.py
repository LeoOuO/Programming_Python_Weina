# ===== Example 2: going through the whole party (for + list) =====
# 生字：party 隊伍 · member 成員 · archer 弓箭手 · healer 牧師 · sorted 排好序的

party = ["Swordsman", "Mage", "Archer", "Healer"]
hp_list = [120, 70, 90, 80]

print("=== PARTY ===")
for member in party:               # 一次拿一個出來，直到拿完（at a time 一次一個）
    print(f"- {member}")

print()
print("=== with numbers ===")      # 這次連編號一起印
for i in range(len(party)):        # i 會依序是 0, 1, 2, 3
    print(f"{i + 1}. {party[i]}  HP {hp_list[i]}")

print()
# 清單的好用工具（handy 好用的）
print(f"party size: {len(party)}")
print(f"total HP:   {sum(hp_list)}")
print(f"highest HP: {max(hp_list)}")
print(f"lowest HP:  {min(hp_list)}")
print(f"sorted:     {sorted(hp_list)}")

# in 用來檢查某樣東西在不在清單裡（whether 是否）
if "Mage" in party:
    print("There is a mage in the party, we can use magic")

# Try it 試試看：
# 1. 算出隊伍的平均血量（average 平均 · divided by 除以）
# 2. 用 for + if 只印出血量低於 90 的隊員
