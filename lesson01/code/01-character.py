# ===== Example 1: build a character card =====
# 生字：character 角色 · level 等級 · job 職業
# A variable is a named box. It can hold text, or a number.

name = "Rain"          # 引號裡的文字叫 string（字串）
job = "Swordsman"      # swordsman 劍士
level = 3              # 沒有引號 -> integer（整數）
hp = 100
atk = 18

print("=== CHARACTER ===")
print("Name: " + name)        # 文字 + 文字 = 接在一起
print("Job: " + job)
print("Level:", level)        # 逗號可以把不同東西印在同一行
print("HP:", hp)
print("ATK:", atk)

# f-string：引號前面加 f，大括號 { } 裡面可以直接放變數
print(f"{name} is a level {level} {job} with {hp} HP and {atk} ATK")

# Try it 試試看：
# 1. 把 name 和 job 改成你自己的角色
# 2. 加一個 defense（防禦力）變數，也印出來
# 3. 把 level 改成 "3"（加引號）再執行，哪一行會壞掉？為什麼？
