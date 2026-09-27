# ===== Example 3: a shop (dictionaries + a bag) =====
# 生字：shop 商店 · item 道具 · price 價格 · buy 買 · afford 買得起
#
# 商品也是字典：一個名稱對一個價格。

prices = {
    "Potion": 20,
    "Iron Sword": 80,
    "Shield": 60,
}

gold = 100
bag = []

print("=== SHOP ===")
for item in prices:                    # for 跑字典會拿到「名稱」
    print(f"  {item:<12} {prices[item]} gold")

print(f"\nYou have {gold} gold")

# 買一樣東西
want = "Shield"
if prices[want] <= gold:               # 錢夠嗎？（afford 負擔得起）
    gold = gold - prices[want]
    bag.append(want)
    print(f"Bought {want}! {gold} gold left")
else:
    print(f"You cannot afford the {want}")

# 再買一樣
want = "Iron Sword"
if prices[want] <= gold:
    gold = gold - prices[want]
    bag.append(want)
    print(f"Bought {want}! {gold} gold left")
else:
    print(f"You cannot afford the {want}")

print(f"\nBag: {bag}")

# Try it 試試看：
# 1. 在商店加兩樣新商品
# 2. 把 gold 改成 300，看第二次買會不會成功
# 3. 想一想：如果要買同一樣東西兩次，程式會怎樣？
