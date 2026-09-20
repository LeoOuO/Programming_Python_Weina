# ===== 範例 1：連段攻擊（for 迴圈）=====
# for 就是「重複做固定次數」

atk = 12

for i in range(5):           # range(5) 會給出 0, 1, 2, 3, 4 共五個數字
    print(f"第 {i} 下攻擊，傷害 {atk}")

print("---- 換個寫法，讓招式編號從 1 開始 ----")

for i in range(1, 6):        # range(1, 6) 會給出 1, 2, 3, 4, 5（不含 6）
    print(f"第 {i} 下攻擊，傷害 {atk}")

print("---- 連段：每一下比前一下痛 ----")

for i in range(1, 6):
    damage = atk * i         # 第 i 下的傷害是 atk 的 i 倍
    print(f"第 {i} 下：{damage}")

# 試試看：
# 1. 改成 8 連段
# 2. range(0, 10, 2) 會印出什麼？自己試一次
# 3. 印出 5 行「⚔️」，每行比前一行多一個（提示：字串可以用 * 乘）
