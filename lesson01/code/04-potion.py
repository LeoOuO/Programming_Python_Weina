# ===== Example 4: when should you drink a potion? (and / or / not) =====
# 生字：potion 藥水 · drink 喝 · shape 狀態

hp = int(input("How much HP do you have? "))
potions = int(input("How many potions are in your bag? "))

# and：兩邊都要成立
# or ：至少一邊成立就好
# not：反過來（opposite 相反）

if hp < 30 and potions > 0:
    print("Drink a potion, your HP is too low!")
elif hp < 30 and potions == 0:
    print("No potions left. RUN!")
elif hp >= 80 or potions >= 5:
    print("You are in good shape. Go!")
else:
    print("Not bad. Keep going.")

# Try it 試試看：
# 1. 輸入 hp = 20、potions = 0，會走到哪一行？
# 2. 自己加一條規則：血量剛好 100 的時候印 "Full health!"
#    （提示 hint：這條要放在最前面，為什麼？）
