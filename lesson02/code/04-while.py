# ===== Example 4: use while when you do not know how many times =====
# 生字：while 當…的時候 · condition 條件 · survive 撐住／存活 · until 直到
# for   = 重複「固定次數」（fixed 固定）
# while = 一直重複，「直到」條件不成立為止（until 直到 · condition 條件）

import random

hp = 100
turn = 0

while hp > 0:                       # 只要血量還大於 0 就繼續（keep going 繼續下去）
    turn = turn + 1
    damage = random.randint(10, 25)
    hp = hp - damage
    print(f"Turn {turn}: took {damage} damage, {hp} HP left")

print(f"You survived {turn} turns")

# 警告 WARNING：while 迴圈一定要有一行讓條件變成不成立
#（這裡是 hp = hp - damage）。沒有的話程式永遠不會停，
# 只能按 Control + C 強制停掉。

# Try it 試試看：
# 1. 把傷害改成 random.randint(1, 5)，大概撐幾回合？
# 2. 加一段：如果回合數超過 50 就 break（跳出迴圈）
