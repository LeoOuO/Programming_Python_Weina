# ===== Example 3: a shop (dictionaries + a bag) =====
#
# The stock 商品 is a dictionary too: one name for one price 價格.

prices = {
    "Potion": 20,
    "Iron Sword": 80,
    "Shield": 60,
}

gold = 100                             # gold 金幣
bag = []                               # what we have bought

print("=== SHOP ===")
for item in prices:                    # looping a dictionary gives you the NAMES
    print(f"  {item:<12} {prices[item]} gold")

print(f"\nYou have {gold} gold")

# 買一樣東西
want = "Shield"
if prices[want] <= gold:               # can we afford 買得起 it?
    gold = gold - prices[want]
    bag.append(want)
    print(f"Bought {want}! {gold} gold left")
else:
    print(f"You cannot afford the {want}")

# 再買一樣
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
