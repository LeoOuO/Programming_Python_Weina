# ===== Example 1: combo attacks (the for loop) =====
# 生字：combo 連段 · loop 迴圈 · range 範圍 · hit 一擊
# for 是「重複做固定次數」（repeat 重複 · fixed 固定的）。

atk = 12

for i in range(5):           # range(5) 會給出 0, 1, 2, 3, 4（五個數字）
    print(f"Hit {i}: {atk} damage")

print("---- same thing, but starting from 1 ----")   # 一樣的事，但從 1 開始

for i in range(1, 6):        # range(1, 6) 給 1, 2, 3, 4, 5（不含 6，included 包含）
    print(f"Hit {i}: {atk} damage")

print("---- a combo: every hit is stronger ----")    # 每一下更強（stronger 更強）

for i in range(1, 6):
    damage = atk * i         # 第 i 下打出 i 倍的傷害
    print(f"Hit {i}: {damage} damage")

# Try it 試試看：
# 1. 改成 8 連段
# 2. range(0, 10, 2) 會印出什麼？自己試一次
# 3. 印 5 行劍，每行比前一行多一把（提示：文字可以用 * 乘）
