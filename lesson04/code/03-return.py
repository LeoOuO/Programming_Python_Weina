# ===== Example 3: getting an answer back (return) =====

# print shows something to a person.
# return hands the answer back to the program, so it can be used again.
#   return 回傳

def damage_of(atk, defense):       # work out the damage, then hand it back
    damage = atk - defense
    if damage < 1:                 # damage is never negative in a game
        damage = 1
    return damage                  # send the value back to where it was called


d1 = damage_of(20, 5)              # d1 gets 15
d2 = damage_of(8, 30)              # would be negative -> becomes 1
print(f"d1 = {d1}")
print(f"d2 = {d2}")

# A returned value can go straight into more maths
total = damage_of(20, 5) + damage_of(15, 3)
print(f"two hits total {total}")


def is_alive(hp):                  # returning True or False is very common
    return hp > 0


print(is_alive(50))                # True
print(is_alive(0))                 # False

if is_alive(35):
    print("still standing!")       # it reads like an English sentence

# Try it:
# 1. Write exp_for_level(level) that returns level * 100
# 2. Write is_critical(roll) that returns True when roll >= 90
# 3. Change the return inside damage_of into a print, then run it.
#    What does d1 become? Why?
