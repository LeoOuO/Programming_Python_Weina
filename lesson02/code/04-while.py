# ===== 範例 4：不知道要跑幾次的時候用 while =====
# for  = 重複「固定次數」
# while = 重複「直到條件不成立為止」

import random

hp = 100
turn = 0

while hp > 0:                       # 只要血量還大於 0，就一直打下去
    turn = turn + 1
    damage = random.randint(10, 25)
    hp = hp - damage
    print(f"第 {turn} 回合：受到 {damage} 點傷害，剩下 {hp} 點血")

print(f"撐了 {turn} 回合才倒下")

# ⚠️ while 一定要有「會讓條件變成不成立」的那一行（這裡是 hp = hp - damage）
#    不然程式會永遠跑下去，要按 Control + C 才停得下來

# 試試看：
# 1. 把傷害改成 random.randint(1, 5)，大概會撐幾回合？
# 2. 加一行：如果回合數超過 50 就 break（強制跳出迴圈）
