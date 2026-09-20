# ===== Example 4: use while when you do not know how many times =====
# for   = repeat a FIXED number of times
# while = repeat UNTIL the condition stops being true

import random

hp = 100
turn = 0

while hp > 0:                       # keep going while HP is above 0
    turn = turn + 1
    damage = random.randint(10, 25)
    hp = hp - damage
    print(f"Turn {turn}: took {damage} damage, {hp} HP left")

print(f"You survived {turn} turns")

# WARNING: a while loop needs a line that makes the condition false one day
# (here it is  hp = hp - damage ).  Without it the program never stops
# and you have to press Control + C.

# Try it:
# 1. Change the damage to random.randint(1, 5) - how many turns now?
# 2. Add: if the turn number goes over 50, break out of the loop
