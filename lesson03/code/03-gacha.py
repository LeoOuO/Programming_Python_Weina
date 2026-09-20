# ===== Example 3: how card draw rates actually work =====
import random

# The trick: build the card pool as a list.
# Rare cards get few copies, common cards get many.
pool = (["SSR Dragon Knight"] * 2       # 2 copies
        + ["SR Fire Mage"] * 8          # 8 copies
        + ["R Archer"] * 30             # 30 copies
        + ["N Villager"] * 60)          # 60 copies, 100 cards in total

print(f"The pool has {len(pool)} cards")
print(f"Chance of an SSR: {pool.count('SSR Dragon Knight')} out of {len(pool)}")

card = random.choice(pool)        # draw one random card from the pool
print(f"You drew: {card}")

print()
print("---- ten draws ----")
results = []                      # an empty list to collect the results
for i in range(10):
    card = random.choice(pool)
    results.append(card)          # put every card we drew into the list
    print(f"{i + 1}. {card}")

print()
print(f"SSR cards in these ten draws: {results.count('SSR Dragon Knight')}")

# Try it:
# 1. Change the SSR to 10 copies and draw again - can you feel the difference?
# 2. Draw 1000 times and count how many SSR you really get
