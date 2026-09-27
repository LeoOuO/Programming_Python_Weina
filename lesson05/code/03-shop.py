# ===== Example 3: a shop (dictionaries + a bag) =====
#
# The stock is a dictionary too: one name for one price.
#   stock 商品 · afford 買得起

prices = {
    "Potion": 20,
    "Iron Sword": 80,
    "Shield": 60,
}

gold = 100
bag = []                               # what we have bought

print("=== SHOP ===")
for item in prices:                    # looping a dictionary gives you the NAMES
    print(f"  {item:<12} {prices[item]} gold")

print(f"\nYou have {gold} gold")

# buy something
want = "Shield"
if prices[want] <= gold:               # can we afford it?
    gold = gold - prices[want]
    bag.append(want)
    print(f"Bought {want}! {gold} gold left")
else:
    print(f"You cannot afford the {want}")

# buy one more thing
want = "Iron Sword"
if prices[want] <= gold:
    gold = gold - prices[want]
    bag.append(want)
    print(f"Bought {want}! {gold} gold left")
else:
    print(f"You cannot afford the {want}")

print(f"\nBag: {bag}")

# Try it:
# 1. Add two new items to the shop
# 2. Change gold to 300 and see whether the second purchase works
# 3. Think about it: what happens if you buy the same item twice?
