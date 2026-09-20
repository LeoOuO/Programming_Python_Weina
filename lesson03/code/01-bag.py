# ===== Example 1: the bag (a list) =====
# A list is a row of boxes in order, written inside square brackets [ ]

bag = ["Wooden Sword", "Red Potion", "Bread"]

print(bag)                 # print the whole list
print(len(bag))            # len() = how many items are inside

# Take one item out by its POSITION - positions start at 0!
print(f"slot 1: {bag[0]}")
print(f"slot 2: {bag[1]}")
print(f"last slot: {bag[-1]}")     # -1 means the last one

# Picked something up -> append (add to the end)
bag.append("Iron Sword")
print(f"picked up an iron sword: {bag}")

# Used something -> remove (take that item out)
bag.remove("Red Potion")
print(f"drank the potion: {bag}")

# Replace one slot
bag[0] = "Steel Sword"
print(f"upgraded the weapon: {bag}")

# Try it:
# 1. What happens if you print bag[10]? Read the error message
# 2. Pick up three more items
# 3. Print "You are carrying N items"
