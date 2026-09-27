# Python 入門（國一 · 2026 秋）

學生：國一，對手機遊戲／app 有興趣。課程用**遊戲題材**教語法，
每一堂最後都有一個**可以執行、會動的 Demo**，長期目標是做出一款自己的遊戲。

## 課程進度

| 堂 | 主題 | 語法 | 最後 Demo |
|---|---|---|---|
| 試教 | 做一個會動的東西 | print / input / if / while | 猜數字（瀏覽器工坊） |
| 1 | 角色與傷害 | 變數、型別、`int()`、f-string、`if/elif/else`、and/or | `demo-boss.py` 王戰一回合 |
| 2 | 讓它自己打下去 | `for`/`range`、累加、`random`、`while`、`break` | `demo-auto-battle.py` 全自動戰鬥 |
| 3 | 背包與抽卡 | 清單 list、索引、append/remove、走訪、統計 | `demo-gacha.py` 轉蛋機 |
| 4 | 把功能包起來 | 函式 `def`、參數、`return`、回傳兩個值 | `demo-dungeon.py` 三房間地城 |
| 5 | 角色資料與商店 | 字典 dict、清單裡放字典、買賣三步驟 | `demo-shop.py` 打怪賺錢買裝備 |
| 6 | 專題：完整遊戲 | 遊戲主迴圈、遊戲狀態、三層結構 | `game.py` Slime Tower（可破關） |
| 下一階段 | 有畫面的遊戲 | pygame：視窗、圖片、鍵盤、碰撞 | 2D 小遊戲 |

## 資料夾

| 路徑 | 內容 |
|---|---|
| `index.html` | **課程總覽頁**：進度、每堂連結、檔案說明、課前檢查 |
| `SETUP.md` | **第一堂先做**：安裝 Python 與 VS Code、終端機基本操作 |
| `lessonNN/slides.html` | 上課簡報（**N** 教師備註、**O** 總覽、**F** 全螢幕） |
| `lessonNN/code/01-*.py …` | 課堂範例，照號碼順序講 |
| `lessonNN/code/practice-1.py` | 練習第一階段：**填空**（骨架都在，把每個 `?` 填掉） |
| `lessonNN/code/practice-2.py` | 練習第二階段：**自己完成**（從空白開始寫） |
| `lessonNN/code/demo-*.py` | 每堂最後的 Demo |
| `lesson01-trial/` | 試教用的簡報與瀏覽器工坊（正式上課後不再使用） |
| `mywork/` | **學生寫作業的地方**（教材更新不會動到這裡） |
| `開始上課.command` / `更新教材.command` | 學生點兩下就執行的小工具 |
| `../teacher-notes/python-junior/` | **老師用**：練習參考解答、教學計畫。另一個 repo，**刻意沒有 remote**，推不出去 |
| `_assets/`、`tools-build-decks.py` | 簡報的共用引擎與組版script |

## 學生那一端的流程（不會有 git 衝突）

1. 點兩下 **開始上課.command** → 輸入堂數 → 今天的檔案被複製到 `mywork/lesson0N/`
2. **所有練習都在 `mywork/` 裡改**，教材資料夾（`lesson01/` …）她完全不動
3. 老師更新教材後，她點兩下 **更新教材.command**（就是 `git pull`）

因為我們永遠不會去改 `mywork/` 底下的檔案，`git pull` 不可能跟她的作業打架。
`開始上課.command` 也不會覆蓋已經存在的檔案，點幾次都安全。

## 上課前 2 分鐘檢查

1. 學生電腦上 `python3 --version` 有反應。
2. `cd` 到今天的 `lessonNN/code/`，隨便跑一個範例。
3. 開 `lessonNN/slides.html`，按 **N** 確認備註看得到。
4. 今天的 Demo 先自己跑一次（`demo-*.py`）。

## 改教材

- 改投影片內容 → 改 `_assets/body-lessonNN.html` → `python3 tools-build-decks.py`
- 改簡報的樣式或按鍵 → 改 `_assets/_deck-head.html` / `_deck-tail.html` → 重跑，三堂一起更新
- 範例程式直接改 `lessonNN/code/*.py`，沒有建置步驟

Demo 的動畫速度都在檔案最上面的 `SPEED`，上課想加快就改小。

程式碼（變數名稱、註解、輸出訊息）一律用英文，順便練英文；投影片與說明文字維持中文。
註解以英文為主。中文只出現在兩個地方：**定義變數那一行**，以及**該段註解最後一行的單字表**
（只收比較少見的字，多半是遊戲才會用到的 damage、potion、mana 之類；room、gold 這種基礎字不收）。
練習題的說明中英文各寫一份。填空題用 `?` 當空格，編輯器會直接畫紅底線提示。
