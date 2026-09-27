# ===== Example 1: build a character card =====
# A variable is a named box. It can hold text, or a number.

name = "Rain"          # text in quotes is a string 字串
job = "Swordsman"      # swordsman 劍士
level = 3              # no quotes -> an integer 整數
hp = 100
atk = 18

print("=== CHARACTER ===")
print("Name: " + name)        # text + text = joined together
print("Job: " + job)
print("Level:", level)        # a comma prints different things on one line
print("HP:", hp)
print("ATK:", atk)

# f-string: put f before the quotes, then any variable inside { }
print(f"{name} is a level {level} {job} with {hp} HP and {atk} ATK")

# Try it:
# 1. Change name and job to your own character
# 2. Add a defense 防禦 variable and print it too
# 3. Change level to "3" (with quotes) and run again - which line breaks? Why?
