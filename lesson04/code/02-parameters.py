# ===== Example 2: passing information in (parameters) =====
# 生字：parameter 參數 · pass 傳入 · argument 引數（傳進去的值）

def attack(name, damage):          # 括號裡是「參數」：呼叫時要給的資料
    print(f"{name} attacks for {damage} damage!")


attack("Hero", 12)                 # 傳進去的值：Hero 和 12
attack("Slime King", 20)
attack("Archer", 7)

# 一個函式寫一次，可以用在任何角色身上。

# 參數可以有預設值（default 預設）
def heal(name, amount=30):         # 沒給 amount 的話就用 30
    print(f"{name} heals {amount} HP")


heal("Hero")                       # 用預設的 30
heal("Hero", 50)                   # 自己指定 50

# Try it 試試看：
# 1. 加一個 miss(name) 函式，印出 "<name> swings and misses"
# 2. 讓 attack 多一個參數 weapon（武器），印成 "Hero attacks with Sword for 12 damage"
