# ===== Example 1: the game loop (a menu that keeps coming back) =====
# 生字：menu 選單 · loop 迴圈 · quit 離開 · invalid 無效的
#
# 每個遊戲最外面都有一個大迴圈：顯示選單 -> 等玩家選 -> 做事 -> 再回到選單。

gold = 100
playing = True                     # 這個變數控制遊戲要不要繼續

while playing:
    print()
    print("=== WHAT NOW? ===")
    print("  1) Work  (+30 gold)")
    print("  2) Rest")
    print("  3) Quit")
    choice = input("Choose: ")

    if choice == "1":
        gold = gold + 30
        print(f"You worked hard. Gold: {gold}")
    elif choice == "2":
        print("You take a nap. Nothing happens.")
    elif choice == "3":
        playing = False            # 迴圈的條件變成 False -> 下一輪就停了
        print("Bye!")
    else:
        print("That is not an option.")     # invalid 無效的選擇

print(f"You finished with {gold} gold")

# Try it 試試看：
# 1. 加一個選項 4) Gamble：50% 機率 +50 金幣，50% -30
# 2. 把 playing = False 改成 break，結果一樣嗎？
