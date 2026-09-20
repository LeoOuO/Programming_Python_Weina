# ===== Example 2: going through the whole party (for + list) =====

party = ["Swordsman", "Mage", "Archer", "Healer"]
hp_list = [120, 70, 90, 80]

print("=== PARTY ===")
for member in party:               # take out one item at a time until they run out
    print(f"- {member}")

print()
print("=== with numbers ===")
for i in range(len(party)):        # i will be 0, 1, 2, 3
    print(f"{i + 1}. {party[i]}  HP {hp_list[i]}")

print()
# handy list tools
print(f"party size: {len(party)}")
print(f"total HP:   {sum(hp_list)}")
print(f"highest HP: {max(hp_list)}")
print(f"lowest HP:  {min(hp_list)}")
print(f"sorted:     {sorted(hp_list)}")

# "in" checks whether something is inside the list
if "Mage" in party:
    print("There is a mage in the party, we can use magic")

# Try it:
# 1. Work out the average HP of the party (hint: total divided by size)
# 2. Use for + if to print only the members with less than 90 HP
