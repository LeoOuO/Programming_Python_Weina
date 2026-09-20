# ===== Lesson 1 final demo: your first boss fight =====
# Everything here is from today: variables, int(), maths, if / elif / else.
# Run it with:  python3 demo-boss.py
import time

SPEED = 0.35          # animation speed - make it smaller (0.1) to go faster
MAX_HP = 100
BOSS_MAX_HP = 120


def say(text):
    """Print one line, then pause so the fight has a rhythm."""
    print(text)
    time.sleep(SPEED)


def bar(hp, max_hp):
    """Draw the HP as 20 blocks, like ######--------------"""
    blocks = int(hp / max_hp * 20)
    if blocks < 0:
        blocks = 0
    return "█" * blocks + "░" * (20 - blocks)


# ---------- character data: all just variables ----------
name = input("Hero, what is your name? ")
hp = MAX_HP
atk = 18

boss = "Slime King"
boss_hp = BOSS_MAX_HP
boss_atk = 15

print()
say("=" * 38)
say(f"  {name}  HP {hp}  ATK {atk}")
say(f"  {boss}  HP {boss_hp}  ATK {boss_atk}")
say("=" * 38)
print()

# ---------- one turn: you choose what to do ----------
say(f"The {boss} blocks your way!")
print()
print("  1) Attack")
print("  2) Power strike  (double damage, but no guard this turn)")
print("  3) Drink a potion  (heal 30 HP, but no attack this turn)")
choice = input("\nWhat do you do? Type 1, 2 or 3: ")

print()

# input() gives us text, so we compare with text
if choice == "1":
    damage = atk
    guarding = True
    say(f"{name} swings a sword!")
elif choice == "2":
    damage = atk * 2
    guarding = False
    say(f"{name} charges up... POWER STRIKE!")
elif choice == "3":
    damage = 0
    guarding = True
    hp = hp + 30
    if hp > MAX_HP:                 # never heal above full health
        hp = MAX_HP
    say(f"{name} drinks a potion. HP is back to {hp}")
else:
    damage = 0
    guarding = False
    say("Wrong key! You stand there doing nothing...")

# ---------- the boss takes damage ----------
if damage > 0:
    boss_hp = boss_hp - damage
    say(f"   {damage} damage!")
    say(f"   {boss}  {bar(boss_hp, BOSS_MAX_HP)}  {boss_hp}/{BOSS_MAX_HP}")

print()

# ---------- the boss strikes back ----------
if boss_hp > 0:
    boss_damage = boss_atk
    if guarding:
        boss_damage = int(boss_damage / 2)    # guarding cuts the damage in half
        say("You raise your shield and block half of it")
    hp = hp - boss_damage
    say(f"The {boss} hits back for {boss_damage} damage!")
    say(f"   {name}  {bar(hp, MAX_HP)}  {hp}/{MAX_HP}")

print()

# ---------- who is winning after this turn? ----------
if boss_hp <= 0:
    say(f"The {boss} is defeated! {name} wins!")
elif hp <= 0:
    say(f"{name} has fallen... try again!")
elif hp > boss_hp:
    say("You are winning. Keep it up!")
else:
    say("This looks bad. Be careful next turn.")

print()
print("(Next lesson we make the fight keep going until someone falls)")
