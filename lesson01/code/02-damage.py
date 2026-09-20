# ===== 範例 2：傷害公式 =====
# 遊戲裡的傷害其實就是一條算式

atk = 18          # 我方攻擊力
defense = 5       # 對方防禦力
skill = 1.5       # 技能倍率

# 運算子：+ 加  - 減  * 乘  / 除  // 整數除法  % 餘數  ** 次方
damage = (atk - defense) * skill

print(f"攻擊 {atk}，對方防禦 {defense}，技能倍率 {skill}")
print(f"傷害 = ({atk} - {defense}) × {skill} = {damage}")

# 注意：用 / 或乘上小數，算出來會帶小數點（叫做「浮點數」）
# 遊戲的傷害通常取整數，用 int() 把小數點後面砍掉
print(f"取整數後的傷害：{int(damage)}")

# 連續攻擊的總傷害
hits = 3
print(f"連續 {hits} 下，總傷害 {int(damage) * hits}")

# 試試看：
# 1. 把 skill 改成 2，傷害變多少？
# 2. 如果對方防禦力比攻擊力還高，會發生什麼事？（把 defense 改成 25 試試）
# 3. 算算看 7 // 2 和 7 % 2 各是多少，印出來對答案
