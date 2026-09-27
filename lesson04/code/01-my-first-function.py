# ===== Example 1: your first function =====
# A function packs a few lines together and gives them a name.
# After that, saying the name runs all of them.
#   function 函式 · define 定義 · call 呼叫

def greet():                       # def = define a function called greet
    print("=" * 30)
    print("  WELCOME, HERO!")
    print("=" * 30)


# Defining does NOT run it. You have to CALL it by name:
greet()                            # call it
print("something happens...")
greet()                            # call it as many times as you like

# Without a function, those three print lines would be copied twice.
# Try it:
# 1. Call greet() three more times
# 2. Change the text inside greet - did every place change together?
# 3. Write your own game_over() function that prints GAME OVER
