# ===== 第 1 堂 最後 Demo：對上第一隻王 =====
# 用到今天學的全部東西：變數、型別轉換、運算、if / elif / else
# 執行：在終端機打  python3 demo-boss.py
import time

SPEED = 0.35          # 動畫速度，想快一點就改小，例如 0.1
MAX_HP = 100
BOSS_MAX_HP = 120


def say(text):
    """印一行字，然後停一下，讓畫面有節奏"""
    print(text)
    time.sleep(SPEED)


def bar(hp, max_hp):
    """把血量畫成 20 格方塊，例如 ██████░░░░░░░░░░░░░░"""
    blocks = int(hp / max_hp * 20)
    if blocks < 0:
        blocks = 0
    return "█" * blocks + "░" * (20 - blocks)


# ---------- 角色資料：全部都是變數 ----------
name = input("勇者，你叫什麼名字？ ")
hp = MAX_HP
atk = 18

boss = "史萊姆王"
boss_hp = BOSS_MAX_HP
boss_atk = 15

print()
say("=" * 34)
say(f"  {name}  HP {hp}  ATK {atk}")
say(f"  {boss}  HP {boss_hp}  ATK {boss_atk}")
say("=" * 34)
print()

# ---------- 一回合：你先選要做什麼 ----------
say(f"{boss} 擋在你面前！")
print()
print("  1) 普通攻擊")
print("  2) 蓄力一擊（傷害 2 倍，但這回合不防禦）")
print("  3) 喝藥水（回復 30 點血，這回合不攻擊）")
choice = input("\n你要做什麼？輸入 1、2 或 3： ")

print()

# input() 拿到的是「字」，所以這裡拿字串來比對
if choice == "1":
    damage = atk
    guarding = True
    say(f"⚔️  {name} 揮出一劍！")
elif choice == "2":
    damage = atk * 2
    guarding = False
    say(f"🔥 {name} 蓄力……全力一擊！")
elif choice == "3":
    damage = 0
    guarding = True
    hp = hp + 30
    if hp > MAX_HP:                 # 血量最多只能回到滿血
        hp = MAX_HP
    say(f"🧪 {name} 喝下藥水，血量回到 {hp}")
else:
    damage = 0
    guarding = False
    say("😵 你按錯鍵了，這回合發呆中……")

# ---------- 結算：王掉血 ----------
if damage > 0:
    boss_hp = boss_hp - damage
    say(f"   造成 {damage} 點傷害！")
    say(f"   {boss}  {bar(boss_hp, BOSS_MAX_HP)}  {boss_hp}/{BOSS_MAX_HP}")

print()

# ---------- 王反擊 ----------
if boss_hp > 0:
    boss_damage = boss_atk
    if guarding:
        boss_damage = int(boss_damage / 2)    # 有防禦，傷害減半（取整數）
        say("🛡️  你舉起盾牌，擋掉一半傷害")
    hp = hp - boss_damage
    say(f"💢 {boss} 反擊，造成 {boss_damage} 點傷害！")
    say(f"   {name}  {bar(hp, MAX_HP)}  {hp}/{MAX_HP}")

print()

# ---------- 這回合結束，誰佔上風？ ----------
if boss_hp <= 0:
    say(f"🎉 {boss} 倒下了！{name} 獲勝！")
elif hp <= 0:
    say(f"💀 {name} 倒下了……下次再來挑戰！")
elif hp > boss_hp:
    say("你佔上風，繼續保持！")
else:
    say("情勢不妙，下一回合要小心。")

print()
print("（下一堂課我們會讓它一直打下去，直到分出勝負）")
