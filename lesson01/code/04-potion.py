# ===== 範例 4：什麼時候該喝藥水（and / or / not）=====

hp = int(input("你現在的血量是多少？ "))
potions = int(input("身上有幾瓶藥水？ "))

# and：兩邊都成立才算成立
# or ：只要有一邊成立就算成立
# not：反過來

if hp < 30 and potions > 0:
    print("🧪 快喝藥水！血太低了")
elif hp < 30 and potions == 0:
    print("😱 沒藥水了，快逃！")
elif hp >= 80 or potions >= 5:
    print("💪 狀態很好，衝吧")
else:
    print("🙂 還好，繼續前進")

# 試試看：
# 1. 輸入 hp=20、藥水=0，看看會走到哪一條
# 2. 自己加一條規則：血量剛好 100 的時候印「滿血！」
#    （提示：要放在最前面，為什麼？）
