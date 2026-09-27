# ===== Example 3: critical hits (if / elif / else) =====
# 生字：critical hit 暴擊 · roll 擲（骰子）· miss 沒打中 · normal 普通
# if 的意思是「如果」：條件成立（true 真）才做縮排裡面的那幾行。
# condition 條件 · indent 縮排

atk = 20
roll = int(input("Roll a 100-sided dice (type 1-100): "))   # dice 骰子；input 拿到的是文字，int() 把它變成數字

if roll >= 95:
    damage = atk * 3
    print("PERFECT CRITICAL! Triple damage")
elif roll >= 80:            # 上面那條不成立（false 假）才會檢查這一條
    damage = atk * 2
    print("CRITICAL HIT! Double damage")
elif roll <= 5:
    damage = 0
    print("You missed completely")
else:                       # 前面全部都不成立的時候
    damage = atk
    print("Normal attack")

print(f"This hit deals {damage} damage")

# 比較 comparison：  >   <   >=   <=   ==（等於 equal）  !=（不等於 not equal）
# 注意：比較要用「兩個」等號 ==；一個 = 是把值放進盒子。

# Try it 試試看：
# 1. 把暴擊的門檻（threshold 門檻）從 80 改成 50，暴擊就變容易了
# 2. 加一條：剛好擲到 50 的時候印 "Right in the middle"
