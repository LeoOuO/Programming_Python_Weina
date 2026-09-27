# ===== Lesson 2 practice - reference answers (TEACHER ONLY) =====
# --- Practice 1（填空）解答 ------------------------------------------
# 1. range(5)
# 2. range(1, 6)        終點不會被印出來，所以要寫 6
# 3. damage = atk * i
# 4. total = 0   /   total = total + damage
# 5. random.randint(1, 6)   /   random.choice(drops)
# 6. stop_at = 0
#    想一想：把 hp = hp - 10 刪掉 -> 無窮迴圈，要按 Control + C。
#
# 第 4 題最容易錯：total 的起點要在迴圈「外面」設成 0。
# 如果她填錯成 total = damage，讓她執行看看數字對不對，自己發現。

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
