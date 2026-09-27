# ===== Example 1: a character sheet (dictionary) =====
# 生字：dictionary 字典 · key 鍵（名稱）· value 值 · sheet 資料表
#
# 清單 list 是「一排東西」，用位置 0、1、2 拿。
# 字典 dict 是「一組有名稱的資料」，用名稱拿 —— 像查字典一樣。

hero = {                       # 大括號 { }，每一項是  "名稱": 值
    "name": "Luna",
    "hp": 100,
    "atk": 18,
    "gold": 50,
}

print(hero)
print(hero["name"])            # 用「名稱」拿值，不是用數字位置
print(hero["hp"])

# 改一項
hero["hp"] = hero["hp"] - 30   # 被打了
print(f"{hero['name']} now has {hero['hp']} HP")

# 加一項（本來沒有的名稱，寫進去就會多一項）
hero["level"] = 5
print(hero)

# 檢查有沒有某一項
if "gold" in hero:
    print(f"gold: {hero['gold']}")

# Try it 試試看：
# 1. 把 hero 改成你自己的角色，多加一項 "job"
# 2. 讓她賺 100 金幣（gold 加 100）再印出來
# 3. 印 hero["mana"] 會怎樣？看看錯誤訊息（KeyError 找不到這個鍵）
