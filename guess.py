# 自己出題目的心理測驗（把問題和答案換成你的！）
print("你是哪一種動物？")
score = 0

a = input("放假想做什麼？ 1:睡覺  2:出去玩  3:看影片  ")
if a == "2":
    score = score + 2
elif a == "3":
    score = score + 1

b = input("喜歡哪種食物？ 1:肉  2:蔬菜  3:甜點  ")
if b == "1":
    score = score + 2
elif b == "3":
    score = score + 1

c = input("朋友形容你是？ 1:安靜  2:活潑  3:搞笑  ")
if c == "2":
    score = score + 2
elif c == "3":
    score = score + 1

print("")
if score >= 5:
    print("小狗：熱情又愛玩")
elif score >= 3:
    print("貓咪：有自己的想法")
else:
    print("烏龜：慢慢來但很穩")
