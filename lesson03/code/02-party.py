# ===== 範例 2：走訪整個隊伍（for + 清單）=====

party = ["劍士", "法師", "弓箭手", "牧師"]
hp_list = [120, 70, 90, 80]

print("=== 隊伍名單 ===")
for member in party:               # 一次拿出一個，直到拿完
    print(f"- {member}")

print()
print("=== 帶編號印出來 ===")
for i in range(len(party)):        # i 會是 0, 1, 2, 3
    print(f"{i + 1}. {party[i]}  HP {hp_list[i]}")

print()
# 常用的清單工具
print(f"隊伍人數：{len(party)}")
print(f"血量總和：{sum(hp_list)}")
print(f"最高血量：{max(hp_list)}")
print(f"最低血量：{min(hp_list)}")
print(f"血量由小到大：{sorted(hp_list)}")

# in：檢查某個東西在不在清單裡
if "法師" in party:
    print("隊伍裡有法師，可以放魔法了")

# 試試看：
# 1. 算出隊伍的平均血量（提示：總和 ÷ 人數）
# 2. 用 for + if 印出「血量低於 90 的隊員」
