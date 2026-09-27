# ===== Example 2: the damage formula =====
# Damage in a game is just a piece of maths.

atk = 18          # my attack power
defense = 5       # the enemy's defense 防禦
skill = 1.5       # skill multiplier 倍率

# Operators:  + add    - subtract    * multiply
#             / divide  // divide and drop the decimals  % remainder
#   remainder 餘數
damage = (atk - defense) * skill

print(f"ATK {atk}, enemy DEF {defense}, skill x{skill}")
print(f"damage = ({atk} - {defense}) * {skill} = {damage}")

# Careful: / and decimal multipliers give a number with a dot (a float).
# Games usually want whole numbers, so int() cuts the decimals off.
#   float 浮點數 · multiplier 倍率
print(f"damage as a whole number: {int(damage)}")

hits = 3
print(f"{hits} hits in a row deal {int(damage) * hits} damage")

# Try it:
# 1. Change skill to 2 - how much damage now?
# 2. What if the enemy defense is higher than your attack? (set defense to 25)
# 3. Print 7 // 2 and 7 % 2 and check the answers
