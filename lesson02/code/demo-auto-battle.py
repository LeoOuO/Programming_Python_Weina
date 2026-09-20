# ===== 第 2 堂 最後 Demo：自動戰鬥 =====
# 上一堂只打一回合，這次用 while 讓它一直打到分出勝負，
# 用 random 讓每一擊都不一樣。
# 執行：python3 demo-auto-battle.py
import random
import time

SPEED = 0.45          # 動畫速度，改小一點會打很快

HERO = "勇者"
HERO_MAX_HP = 120
HERO_ATK = 14

BOSS = "熔岩巨龍"
BOSS_MAX_HP = 160
BOSS_ATK = 14


def bar(hp, max_hp):
    """血條：20 格方塊"""
    blocks = int(hp / max_hp * 20)
    if blocks < 0:
        blocks = 0
    return "█" * blocks + "░" * (20 - blocks)


def show(hero_hp, boss_hp):
    print(f"  {HERO:<5} {bar(hero_hp, HERO_MAX_HP)} {max(hero_hp, 0):>3}/{HERO_MAX_HP}")
    print(f"  {BOSS:<5} {bar(boss_hp, BOSS_MAX_HP)} {max(boss_hp, 0):>3}/{BOSS_MAX_HP}")


def attack(name, base_atk):
    """算出這一擊的傷害，回傳 (傷害, 說明文字)"""
    roll = random.randint(1, 100)          # 擲一顆 100 面骰決定這一擊的品質
    if roll >= 90:
        return base_atk * 2, f"💥 {name} 暴擊！"
    elif roll <= 10:
        return 0, f"😵 {name} 失手了"
    else:
        damage = random.randint(base_atk - 4, base_atk + 4)
        return damage, f"⚔️  {name} 攻擊"


hero_hp = HERO_MAX_HP
boss_hp = BOSS_MAX_HP
turn = 0
hero_total = 0        # 統計：勇者總共打出多少傷害
potions = 2           # 藥水只有兩瓶，用完就沒了

print("=" * 38)
print("        自 動 戰 鬥  開 始")
print("=" * 38)
show(hero_hp, boss_hp)
time.sleep(SPEED * 2)

# 只要兩邊都還活著，就一直打下去
while hero_hp > 0 and boss_hp > 0:
    turn = turn + 1
    print(f"\n── 第 {turn} 回合 ──")

    # 勇者先出手
    damage, text = attack(HERO, HERO_ATK)
    boss_hp = boss_hp - damage
    hero_total = hero_total + damage
    print(f"{text} 造成 {damage} 點傷害")
    time.sleep(SPEED)

    # 王被打倒就不用反擊了
    if boss_hp <= 0:
        break

    # 王反擊
    damage, text = attack(BOSS, BOSS_ATK)
    hero_hp = hero_hp - damage
    print(f"{text} 造成 {damage} 點傷害")
    time.sleep(SPEED)

    show(hero_hp, boss_hp)

    # 血太低而且還有藥水的時候，自動喝一瓶
    if hero_hp <= 30 and hero_hp > 0 and potions > 0:
        potions = potions - 1
        hero_hp = hero_hp + 40
        if hero_hp > HERO_MAX_HP:
            hero_hp = HERO_MAX_HP
        print(f"🧪 {HERO} 喝下藥水，血量回到 {hero_hp}（剩 {potions} 瓶）")
        time.sleep(SPEED)

print()
print("=" * 38)
if boss_hp <= 0:
    print(f"🎉 第 {turn} 回合，{BOSS} 倒下了！")
else:
    print(f"💀 第 {turn} 回合，{HERO} 倒下了……")
print(f"   總回合數：{turn}")
print(f"   {HERO} 總共打出 {hero_total} 點傷害")
print(f"   平均每回合 {hero_total // turn} 點")
print("=" * 38)

print()
print("想改難度就改上面的數字：BOSS_ATK 調高會變難，potions 調多會變簡單。")
print("（下一堂課我們會用「清單」做出背包和抽卡）")
