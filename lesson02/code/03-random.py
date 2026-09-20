# ===== Example 3: let the computer roll dice (random) =====
# "import" means: borrow a toolbox somebody else already wrote.

import random

# randint(a, b): a random whole number between a and b (both included)
roll = random.randint(1, 100)
print(f"You rolled {roll}")

# choice(list): pick one random item from a list
drops = ["Rusty Sword", "Red Potion", "10 Gold", "Nothing"]
print(f"The monster drops: {random.choice(drops)}")

print("---- fight ten monsters and see what drops ----")
for i in range(1, 11):
    print(f"Monster {i}: {random.choice(drops)}")

# Every run gives a different result - that is what makes games fun.
# Try it:
# 1. Add more drops, put a "Legendary Sword" in there
# 2. Make the damage random.randint(10, 20) so every hit is different
