# ===== Example 4: when should you drink a potion? (and / or / not) =====

hp = int(input("How much HP do you have? "))
potions = int(input("How many potions are in your bag? "))

# and : both sides must be true
# or  : at least one side must be true
# not : the opposite

if hp < 30 and potions > 0:
    print("Drink a potion, your HP is too low!")
elif hp < 30 and potions == 0:
    print("No potions left. RUN!")
elif hp >= 80 or potions >= 5:
    print("You are in good shape. Go!")
else:
    print("Not bad. Keep going.")

# Try it:
# 1. Enter hp = 20 and potions = 0 - which line runs?
# 2. Add your own rule: when HP is exactly 100, print "Full health!"
#    (hint: it has to go first - why?)
