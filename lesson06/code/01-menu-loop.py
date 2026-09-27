# ===== Example 1: the game loop (a menu that keeps coming back) =====
#
# Every game has one big loop around everything:
# show the menu -> wait for the player -> do it -> back to the menu.

gold = 100
playing = True                     # this variable decides whether the game goes on

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
        playing = False            # the loop condition turns False -> it stops
        print("Bye!")
    else:
        print("That is not an option.")     # the player typed something else

print(f"You finished with {gold} gold")

# Try it:
# 1. Add a 4) Gamble option: 50% chance +50 gold, 50% chance -30
# 2. Replace playing = False with break - is the result the same?
#   gamble 賭一把
