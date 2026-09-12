# Python 入門（國一 · 2026 秋）

學生：國一女生，想學 Python，對手機遊戲／app 有興趣。
第一堂為試教（2026-09-14）。

## 資料夾

| 路徑 | 內容 |
|---|---|
| `lesson01-trial/slides.html` | 試教簡報（互動 HTML，N 鍵教師備註，O 總覽） |
| `lesson01-trial/playground.html` | **Python 遊戲工坊**：瀏覽器內直接跑 Python，零安裝、離線可用 |
| `lesson01-trial/_vendor/` | Skulpt 1.2.0（MIT），工坊的 Python 執行引擎 |
| `notes/` | 教學計畫、學生紀錄（只給老師） |

## 上課前 2 分鐘檢查

1. 用 Chrome / Safari / Edge 直接開 `lesson01-trial/playground.html`，**先按右上角「測試模式」**（試用不會存檔，不會動到學生的程式），再按「▶ 執行」，右邊出現字就 OK。試完記得把測試模式關掉。
2. 開 `lesson01-trial/slides.html`，按 **N** 確認備註看得到，按 **F** 全螢幕。
3. 工坊「③彩虹螺旋」執行一次（畫圖需 3～5 秒，正常）。

工坊不需要網路、不需要裝 Python；Mac / Windows 都一樣。
學生的程式會自動存在該瀏覽器的 localStorage，換瀏覽器或清資料就沒了 → 下課前請按「💾 下載我的程式」。

## 路線（暫定，待與家長確認）

Python 基礎（8～10 堂，每堂做出一個可玩的東西）→ pygame 電腦 2D 小遊戲（專題）→ Godot（GDScript 語法近似 Python，可輸出 iOS/Android）。
