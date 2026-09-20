# ===== Example 3: critical hits (if / elif / else) =====
# "if" means: only do the indented lines when the condition is true.

atk = 20
roll = int(input("Roll a 100-sided dice (type 1-100): "))   # input gives text, int() turns it into a number

if roll >= 95:
    damage = atk * 3
    print("PERFECT CRITICAL! Triple damage")
elif roll >= 80:            # only checked when the line above was false
    damage = atk * 2
    print("CRITICAL HIT! Double damage")
elif roll <= 5:
    damage = 0
    print("You missed completely")
else:                       # none of the above were true
    damage = atk
    print("Normal attack")

print(f"This hit deals {damage} damage")

# Comparisons:  >   <   >=   <=   ==  (equal)   !=  (not equal)
# Careful: use TWO equal signs == to compare. One = puts a value in a box.

# Try it:
# 1. Change the critical threshold from 80 to 50 - criticals become easier
# 2. Add a case: when the roll is exactly 50, print "Right in the middle"
