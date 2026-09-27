# ===== Example 2: passing information in (parameters) =====

def attack(name, damage):          # the words in ( ) are parameters 參數
    print(f"{name} attacks for {damage} damage!")


attack("Hero", 12)                 # the values we pass 傳入: Hero and 12
attack("Slime King", 20)
attack("Archer", 7)

# Write the function once, use it for any character.

# A parameter can have a default 預設 value
def heal(name, amount=30):         # without an amount, 30 is used
    print(f"{name} heals {amount} HP")


heal("Hero")                       # uses the default 30
heal("Hero", 50)                   # we choose 50 instead

# Try it:
# 1. Add a miss(name) function that prints "<name> swings and misses"
# 2. Give attack one more parameter, weapon 武器:
#    "Hero attacks with Sword for 12 damage"
