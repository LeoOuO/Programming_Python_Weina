# ===== Lesson 1 practice - reference answers (TEACHER ONLY) =====
# Each one lists the mistake students usually make. Give hints as questions,
# never the code itself.

# --- Question 1 ----------------------------------------------------
name = "Rain"
job = "Swordsman"
hp = 100
atk = 18
print(f"{name} is a {job} with {hp} HP and {atk} ATK")
# Common error: using + with a number -> TypeError.
# Hint: "is that a word or a number you are joining?"

# --- Question 2 ----------------------------------------------------
level = int(input("What is your level? "))
atk = 10 + level * 2
print(f"A level {level} hero has {atk} attack")
# Common error: forgetting int(), so "3" * 2 becomes "33".
# Hint: "right now, is your 3 a word or a number?"

# --- Question 3 ----------------------------------------------------
hp = int(input("How much HP? "))
if hp >= 70:
    print("Looking good")
elif hp >= 30:
    print("Be careful")
else:
    print("Drink a potion now!")
# Common error: wrong order (30 first), so everything hits the first branch.
# Hint: "if you type 90, is the first condition true?"

# --- Question 4 (challenge) ----------------------------------------
a_atk, a_def = 18, 5
b_atk, b_def = 14, 12
a_power = a_atk * 2 + a_def       # 41
b_power = b_atk * 2 + b_def       # 40
if a_power > b_power:
    print(f"A is stronger ({a_power} vs {b_power})")
elif b_power > a_power:
    print(f"B is stronger ({b_power} vs {a_power})")
else:
    print("It's a tie")
# Most students forget the tie. Ask: "what if both are exactly the same?"
