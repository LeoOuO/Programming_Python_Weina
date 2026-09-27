# ===== Example 2: adding things up =====
# The trick: make a counter 計數器 first, then keep adding to it inside the loop.

total = 0                    # total 總和 damage, starts at 0

for i in range(1, 6):
    damage = 12 * i
    total = total + damage   # old total + this hit -> store it back
    print(f"Hit {i} deals {damage}, total so far {total}")

print(f"Five-hit combo total: {total}")

# The same trick counts how many times something happened
crit_count = 0                       # how many critical hits 暴擊
rolls = [97, 12, 85, 43, 99]        # pretend 假裝 these are five dice rolls

for roll in rolls:                   # for can take items out of a list one by one
    if roll >= 80:
        crit_count = crit_count + 1

print(f"{crit_count} critical hits out of 5")

# Try it:
# 1. Replace  total = total + damage  with  total += damage  (same meaning, shorter)
# 2. Add up every number from 1 to 100
