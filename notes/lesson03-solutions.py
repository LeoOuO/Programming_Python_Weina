# ===== Lesson 3 practice - reference answers (TEACHER ONLY) =====
import random

# --- Question 1 ----------------------------------------------------
bag = ["Wooden Sword", "Red Potion", "Bread"]
print(bag)
bag.append("Shield")
bag.append("Gold")
print(bag)
bag.remove("Bread")
print(bag)

# --- Question 2 ----------------------------------------------------
party = ["Swordsman", "Mage", "Archer"]
for i in range(len(party)):
    print(f"{i + 1}. {party[i]}")
# Common error: printing "0. Swordsman" (forgot the + 1), or using
# for m in party when the number is needed.

# --- Question 3 ----------------------------------------------------
hp_list = [120, 70, 90, 80, 55]
print(f"total {sum(hp_list)}")                        # 415
print(f"highest {max(hp_list)}  lowest {min(hp_list)}")   # 120 / 55
print(f"average {sum(hp_list) / len(hp_list)}")       # 83.0

# --- Question 4 ----------------------------------------------------
strong = []
for hp in hp_list:
    if hp > 80:
        strong.append(hp)
print(strong)                                         # [120, 90]
# Common error: strong = [] inside the loop, or appending the whole list.
# This is the backbone of the demo - make sure she gets this one working.

# --- Question 5 (challenge) ----------------------------------------
pool = ["Rare Card"] * 5 + ["Common Card"] * 95
count = 0
for i in range(100):
    if random.choice(pool) == "Rare Card":
        count = count + 1
print(f"{count} rare cards in 100 draws")
# Expected 5, but it jumps between 1 and 10 - a good moment to explain why
# real games add a pity system.
