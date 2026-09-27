# ===== Lesson 6 practice - reference answers (TEACHER ONLY) =====
# --- Practice 1（填空迷你版）解答 ------------------------------------
# 1. "gold": 20,        /  game["hero"]["name"]
# 2. show()
# 3. return random.randint(atk - 2, atk + 2)
# 4. while hp > 0 and game["hero"]["hp"] > 0:
#    game["hero"]["hp"] - monster["atk"]
#    return True
# 5. for monster in monsters:
#
# 填完執行應該會通關（兩隻怪都不強），讓她玩一次再往下。
#
# --- Practice 2（改造 game.py）帶法 ----------------------------------
# 這份沒有標準答案，重點是過程。優先順序：
#   1 換皮      -> 最有動力，先做
#   2 第六層    -> 只要在 MONSTERS 加一行，證明「分層」的好處。
#                  加完問她：「主程式改了嗎？」答案是沒有，這就是重點。
#   5 難度調整  -> 今天的靈魂。讓她玩三次自己決定數值，
#                  這是她第一次做遊戲設計師的工作。
#
# 3 新商品的改法（她會卡在這裡）：
#     SHOP 加一項：
#         "Lucky Charm": {"price": 40, "text": "crit chance up"},
#     shop() 的 choice 檢查要改成 ["1","2","3","4"]，
#     然後在效果那串 elif 後面加：
#         elif item == "Lucky Charm":
#             game["crit"] = game["crit"] + 10
#     並在 hero_damage() 用 game["crit"] 取代寫死的 10。
#     -> 這題會動到三個地方，正好說明「新增資料容易，新增規則麻煩」。
#
# 4 新技能的改法：
#     照第 4 堂的 fireball 寫一個函式，在 battle() 的選單多印一行，
#     再加一個 elif choice == "4":。
#
# 6 戰績：game 加 "wins": 0，battle 贏了 game["wins"] += 1，結尾印出來。
# 7 寶箱：主迴圈 shop() 之前加
#         if random.randint(1, 100) <= 30:
#             found = random.randint(10, 50)
#             game["gold"] = game["gold"] + found
#             say(f"  You found a chest! +{found} gold")
#
# --- 驗收標準 --------------------------------------------------------
# 下課時她的 game.py 要能執行、能玩完，而且至少有三處是她自己改的。
# 不要求她做完全部七項。
