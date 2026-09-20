# ===== Lesson 2 practice - reference answers (TEACHER ONLY) =====
import random

# --- Question 1 ----------------------------------------------------
for i in range(10):
    print("Attack!")

# --- Question 2 ----------------------------------------------------
total = 0
for i in range(1, 11):
    exp = i * 15
    total = total + exp
    print(f"Monster {i} gives {exp} exp")
print(f"Total exp: {total}")          # 825
# Common error: total = 0 inside the loop (answer becomes 150).
# Hint: "how many times do you want the reset to happen?"

# --- Question 3 ----------------------------------------------------
prizes = ["Gold", "Potion", "Gem", "Nothing"]
for i in range(5):
    print(f"Draw {i + 1}: {random.choice(prizes)}")

# --- Question 4 ----------------------------------------------------
hp = 100
hits = 0
while hp > 0:
    hits = hits + 1
    hp = hp - random.randint(8, 20)
print(f"It took {hits} hits")          # usually 7-9
# Common error: while hp <= 0 (condition reversed, loop never runs).
# Hint: "is that the condition to CONTINUE or to STOP?"

# --- Question 5 (challenge) ----------------------------------------
count = 0
for i in range(1000):
    if random.randint(1, 100) >= 95:
        count = count + 1
print(f"{count} rolls out of 1000 were 95 or higher")
# The real answer is about 60 (95 to 100 is six numbers = 6%).
# Most people guess 5% / 50 - close but not exact, a nice chance to talk
# about randint including BOTH ends.
