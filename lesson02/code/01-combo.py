# ===== Example 1: combo attacks (the for loop) =====
# "for" repeats something a fixed number of times.

atk = 12         # attack power 攻擊力

for i in range(5):           # range(5) gives 0, 1, 2, 3, 4  (five numbers)
    print(f"Hit {i}: {atk} damage")

print("---- same thing, but starting from 1 ----")

for i in range(1, 6):        # range(1, 6) gives 1, 2, 3, 4, 5  (6 is not included)
    print(f"Hit {i}: {atk} damage")

print("---- a combo 連段: every hit is stronger ----")

for i in range(1, 6):
    damage = atk * i         # hit number i does i times the damage 傷害
    print(f"Hit {i}: {damage} damage")

# Try it:
# 1. Make it an 8-hit combo 連段
# 2. What does range(0, 10, 2) print? Try it yourself
# 3. Print 5 lines of swords, one more on each line (hint: text can be * multiplied)
