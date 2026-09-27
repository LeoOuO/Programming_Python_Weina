# ===== Example 3: let the computer roll dice (random) =====
# 生字：random 隨機 · dice 骰子 · drop 掉落物 · rusty 生鏽的
# import 的意思是：借用別人寫好的工具箱（borrow 借 · toolbox 工具箱）。

import random

# randint(a, b)：隨機給一個 a 到 b 之間的整數（between 之間，頭尾都包含）
roll = random.randint(1, 100)
print(f"You rolled {roll}")

# choice(清單)：從清單裡隨機挑一個（pick 挑 · item 東西）
drops = ["Rusty Sword", "Red Potion", "10 Gold", "Nothing"]
print(f"The monster drops: {random.choice(drops)}")

print("---- fight ten monsters and see what drops ----")   # 打十隻怪，看掉什麼
for i in range(1, 11):
    print(f"Monster {i}: {random.choice(drops)}")

# 每次執行結果都不一樣（result 結果），這就是遊戲好玩的地方。
# Try it 試試看：
# 1. 多加幾個掉落物，把 "Legendary Sword"（傳說之劍）放進去
# 2. 把傷害改成 random.randint(10, 20)，每一下都不一樣
