# ===== Example 3: getting an answer back (return) =====
# 生字：return 回傳 · result 結果 · value 值

# print 是「印出來給人看」，return 是「把答案交回去給程式用」。

def damage_of(atk, defense):       # 算傷害，然後把答案交回去
    damage = atk - defense
    if damage < 1:                 # 遊戲裡傷害不會是負的
        damage = 1
    return damage                  # 把算好的值送回呼叫的地方


d1 = damage_of(20, 5)              # d1 收到 15
d2 = damage_of(8, 30)              # 算出來是負的 -> 變成 1
print(f"d1 = {d1}")
print(f"d2 = {d2}")

# 回傳的值可以直接拿來算
total = damage_of(20, 5) + damage_of(15, 3)
print(f"two hits total {total}")


def is_alive(hp):                  # 回傳 True 或 False 也很常見
    return hp > 0


print(is_alive(50))                # True
print(is_alive(0))                 # False

if is_alive(35):
    print("still standing!")       # 讀起來就像英文句子

# Try it 試試看：
# 1. 寫一個 exp_for_level(level)，回傳 level * 100
# 2. 寫一個 is_critical(roll)，roll >= 90 時回傳 True
# 3. 把 damage_of 裡的 return 改成 print，然後執行 —— d1 會變成什麼？為什麼？
