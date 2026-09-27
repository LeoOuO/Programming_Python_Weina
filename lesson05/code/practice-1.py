# ===== Lesson 5  Practice 1: fill in the blanks =====
# ===== 第 5 堂 練習一：填空 =====
#
# Every  ?  is a blank you have to fill in.
# VS Code underlines them in red, so you can see what is still missing.
# Running the file stops at the first  ?  with a SyntaxError and tells you
# the line number. Fill one in, run it, fill in the next.
#
# 每一個  ?  都是要你填的空格。VS Code 會用紅色底線標出來，
# 一眼就看得到還有哪裡沒寫。執行的話會在第一個 ? 停下來，
# 出現 SyntaxError 並告訴你行號。填一個、執行一次，再填下一個。

monster = {
    "name": "Goblin",
    "hp": 45,
    "atk": 12,
}

# --- 1. Take a value by name / 用名稱拿值 -----------------------------

print(monster[?])             # should print Goblin - a name in quotes  填名稱
print(monster[?])             # should print 45


# --- 2. Change one item / 改一項 --------------------------------------
# The monster takes 10 damage.  怪物被打了 10 點

monster["hp"] = monster["hp"] - ?
print(f"{monster['name']} has {monster['hp']} HP")     # should be 35


# --- 3. Add a new item / 加一項 ---------------------------------------
# Give the monster a "gold" item worth 30.  幫怪物加上掉落金幣，值是 30

monster[?] = 30               # the new name is gold  填新名稱
print(monster)


# --- 4. Dictionaries inside a list / 清單裡放字典 ---------------------

party = [
    {"name": "Luna",  "hp": 100},
    {"name": "Borin", "hp": 140},
]

print(party[0][?])            # should print Luna
print(party[1]["hp"])            # already written - what does it print?


# --- 5. Go through the party / 走訪整隊 -------------------------------

for member in ?:              # which list?  要跑哪一個清單？
    print(f"{member['name']} has {member['hp']} HP")


# --- 6. Total HP / 總血量 ---------------------------------------------

total = ?                     # where does it start?  起點填多少？
for member in party:
    total = total + member[?]    # which item do we add?  加哪一項？
print(f"total HP {total}")       # should be 240


# --- 7. Buying something / 買東西 -------------------------------------

prices = {"Potion": 20, "Shield": 60}
gold = 50

if prices["Potion"] <= ?:     # compare the price with what?  跟什麼比？
    gold = gold - prices["Potion"]
    print(f"Bought a Potion, {gold} gold left")

# Think about it: when do you use a dictionary, and when a list?
# 想一想：字典和清單，什麼時候用哪一個？
