# ===== Lesson 4 practice - reference answers (TEACHER ONLY) =====
# --- Practice 1（填空）解答 ------------------------------------------
# 1. def show_title():
# 2. def introduce(name):
# 3. return result
# 4. answer = double(21)
# 5. return hp <= 0
# 6. d, text = punch(10)
#    想一想：print 是印給人看，return 是把值交回程式，還可以再拿去算。
#
# 兩種錯誤訊息的差別要當場講：
#   SyntaxError -> 關鍵字（def / return）還沒填，Python 連讀都讀不懂
#   NameError   -> 文法沒問題，但這個名字還沒有值
import random

# --- Practice 2 ----------------------------------------------------
# 1.
def welcome(name):
    print(f"Welcome to the dungeon, {name}!")

for n in ["Luna", "Borin", "Sera"]:
    welcome(n)

# 2.
def exp_needed(level):
    return level * 100

for level in range(1, 6):
    print(f"level {level}: {exp_needed(level)} exp")

# 3.  常見錯：忘了 return，或把 if damage < 1 寫在 return 後面（永遠不會執行）
def damage_of(atk, defense):
    damage = atk - defense
    if damage < 1:
        damage = 1
    return damage

print(damage_of(20, 5), damage_of(5, 20))      # 15  1

# 4.
def is_critical(roll):
    return roll >= 90

crits = 0
for i in range(10):
    if is_critical(random.randint(1, 100)):
        crits = crits + 1
print(f"{crits} crits out of 10")

# 5.  自由發揮，重點是「回傳兩個值」的形式
def thunder(atk):
    if random.randint(1, 100) <= 50:
        return 0, "Thunder misses!"
    damage = atk * 3
    return damage, f"THUNDER! {damage} damage"

for i in range(5):
    damage, text = thunder(10)
    print(text)

# 6.  函式呼叫函式 —— 這題寫得出來代表真的懂了
def attack(atk, defense):
    damage = damage_of(atk, defense)
    if is_critical(random.randint(1, 100)):
        damage = damage * 2
    return damage

for i in range(10):
    print(attack(20, 5), end=" ")
print()
