# ===== Example 2: a whole party (a list of dictionaries) =====

# A list of dictionaries = a whole party 隊伍, each member with its own data.
party = [
    {"name": "Luna",  "hp": 100, "atk": 18},
    {"name": "Borin", "hp": 140, "atk": 12},
    {"name": "Sera",  "hp": 80,  "atk": 24},
]

print(party[0])                # the first character (the whole set of data)
print(party[0]["name"])        # that character's name

print()
for member in party:           # one at a time; each one is a dictionary
    print(f"{member['name']:<6} HP {member['hp']:>4}  ATK {member['atk']}")

# find the strongest 最強的 one
print()
best = party[0]
for member in party:
    if member["atk"] > best["atk"]:
        best = member
print(f"Strongest: {best['name']} ({best['atk']} ATK)")

# total HP of the whole party
total = 0
for member in party:
    total = total + member["hp"]
print(f"Party total HP: {total}")

# Try it:
# 1. Add a fourth character to the party
# 2. Find the one with the LOWEST hp (change > into <, and think about why)
# 3. Give every member 10 more hp
