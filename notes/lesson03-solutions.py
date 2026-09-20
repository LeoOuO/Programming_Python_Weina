# ===== 第 3 堂 練習參考解答（老師用）=====
import random

# --- 練習 1 --------------------------------------------------------
bag = ["木劍", "紅藥水", "麵包"]
print(bag)
bag.append("盾牌")
bag.append("金幣")
print(bag)
bag.remove("麵包")
print(bag)

# --- 練習 2 --------------------------------------------------------
party = ["劍士", "法師", "弓箭手"]
for i in range(len(party)):
    print(f"{i + 1}. {party[i]}")
# 常見錯：印出 0. 劍士（忘了 +1）；或用 for m in party 卻想要編號。

# --- 練習 3 --------------------------------------------------------
hp_list = [120, 70, 90, 80, 55]
print(f"總和 {sum(hp_list)}")                       # 415
print(f"最高 {max(hp_list)}  最低 {min(hp_list)}")   # 120 / 55
print(f"平均 {sum(hp_list) / len(hp_list)}")         # 83.0

# --- 練習 4 --------------------------------------------------------
strong = []
for hp in hp_list:
    if hp > 80:
        strong.append(hp)
print(strong)                                        # [120, 90]
# 常見錯：strong = [] 放進迴圈；或 append 寫成 strong.append(hp_list)。
# 這題是 Demo 的核心骨架，一定要做出來。

# --- 練習 5（挑戰）-------------------------------------------------
pool = ["稀有卡"] * 5 + ["普通卡"] * 95
count = 0
for i in range(100):
    if random.choice(pool) == "稀有卡":
        count = count + 1
print(f"100 抽裡有 {count} 張稀有卡")
# 理論值 5 張，實際會在 1~10 之間跳 —— 正好聊「機率不等於保證」，
# 也就是為什麼真的遊戲要做保底。
