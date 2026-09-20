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
| 之後 | 函式與完整小遊戲 | `def`、把前三堂組起來 | 文字 RPG |

## 資料夾

| 路徑 | 內容 |
|---|---|
| `SETUP.md` | **第一堂先做**：安裝 Python 與 VS Code、終端機基本操作 |
| `lessonNN/slides.html` | 上課簡報（**N** 教師備註、**O** 總覽、**F** 全螢幕） |
| `lessonNN/code/01-*.py …` | 課堂範例，照號碼順序講 |
| `lessonNN/code/practice.py` | 課堂練習（只有題目，沒有答案） |
| `lessonNN/code/demo-*.py` | 每堂最後的 Demo |
| `lesson01-trial/` | 試教用的簡報與瀏覽器工坊（正式上課後不再使用） |
| `notes/` | **老師用**：教學計畫、練習參考解答、選購建議 |
| `_assets/`、`tools-build-decks.py` | 簡報的共用引擎與組版script |

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
