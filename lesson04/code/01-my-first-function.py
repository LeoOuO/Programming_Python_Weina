# ===== Example 1: your first function =====
# 生字：function 函式 · define 定義 · call 呼叫 · repeat 重複
# 函式 = 把幾行程式包起來，取一個名字，之後叫名字就會執行。

def greet():                       # def = define（定義）一個函式，名字叫 greet
    print("=" * 30)
    print("  WELCOME, HERO!")
    print("=" * 30)


# 上面只是「定義」，寫了不會執行。要用這個名字「呼叫」它才會動：
greet()                            # call 呼叫
print("something happens...")
greet()                            # 想印幾次就呼叫幾次

# 沒有函式的話，上面那三行 print 要複製兩次。
# Try it 試試看：
# 1. 再呼叫 greet() 三次
# 2. 改 greet 裡面的字，看看三個地方是不是一起變了（這就是函式的好處）
# 3. 自己寫一個 game_over() 函式，印出 GAME OVER
