# ===== Example 2: the damage formula =====
# 生字：damage 傷害 · defense 防禦 · skill 技能 · formula 公式
# Damage in a game is just a piece of maths.

atk = 18          # attack 攻擊力
defense = 5       # 對方的防禦力（enemy 敵人）
skill = 1.5       # multiplier 倍率

# 運算子 operators：
#   +  add 加        -  subtract 減      *  multiply 乘
#   /  divide 除     // 除完取整數       %  remainder 餘數
damage = (atk - defense) * skill

print(f"ATK {atk}, enemy DEF {defense}, skill x{skill}")
print(f"damage = ({atk} - {defense}) * {skill} = {damage}")

# 注意：/ 和小數倍率算出來會有小數點（float 浮點數）。
# 遊戲通常要整數（whole number），所以用 int() 把小數點後面切掉。
print(f"damage as a whole number: {int(damage)}")    # whole number 整數

hits = 3
print(f"{hits} hits in a row deal {int(damage) * hits} damage")

# Try it 試試看：
# 1. 把 skill 改成 2，傷害變多少？
# 2. 如果對方的 defense 比你的 atk 還高會怎樣？（把 defense 改成 25）
# 3. 印出 7 // 2 和 7 % 2，對一下答案
