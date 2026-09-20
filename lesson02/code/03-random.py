# ===== 範例 3：讓電腦擲骰子（random）=====
# import 就是「借用別人寫好的工具箱」

import random

# randint(a, b)：隨機給一個 a 到 b 之間的整數（含 a 和 b）
roll = random.randint(1, 100)
print(f"骰出了 {roll}")

# choice(清單)：從清單裡隨機挑一個
drops = ["生鏽的劍", "紅藥水", "金幣 x10", "什麼都沒有"]
print(f"打倒怪物，掉落：{random.choice(drops)}")

print("---- 打十隻怪，看看掉什麼 ----")
for i in range(1, 11):
    print(f"第 {i} 隻：{random.choice(drops)}")

# 每次執行結果都不一樣，這就是遊戲好玩的地方
# 試試看：
# 1. 多加幾個掉落物，把「傳說之劍」加進去
# 2. 讓傷害變成 random.randint(10, 20)，每一下都不一樣
