# ===== Example 1: the bag (a list) =====
# 生字：bag 背包 · list 清單 · slot 格子 · append 加到後面 · remove 移除
# 清單是一排「有順序」的盒子，寫在中括號 [ ] 裡面
#（row 一排 · in order 依序 · square brackets 中括號）

bag = ["Wooden Sword", "Red Potion", "Bread"]   # wooden 木頭的 · bread 麵包

print(bag)                 # 印出整個清單（whole 整個）
print(len(bag))            # len() = 裡面有幾樣東西（length 長度）

# 用「位置」把其中一樣拿出來（position 位置）——位置是從 0 開始數的！
print(f"slot 1: {bag[0]}")
print(f"slot 2: {bag[1]}")
print(f"last slot: {bag[-1]}")     # -1 代表最後一個（last 最後）

# 撿到東西 -> append，加到最後面（pick up 撿起來）
bag.append("Iron Sword")
print(f"picked up an iron sword: {bag}")

# 用掉東西 -> remove，把那一樣拿走
bag.remove("Red Potion")
print(f"drank the potion: {bag}")

# 換掉某一格（replace 取代）
bag[0] = "Steel Sword"
print(f"upgraded the weapon: {bag}")

# Try it 試試看：
# 1. 印 bag[10] 會怎樣？讀讀看錯誤訊息（error message 錯誤訊息）
# 2. 再撿三樣東西進背包
# 3. 印出 "You are carrying N items"（carry 攜帶）
