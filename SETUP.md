# 開始寫程式前：安裝與設定（Mac 為主，Windows 附在後面）

第一堂課會一起做完，約 15 分鐘。做完之後每堂課都只是「開編輯器 → 開終端機」。

## Mac

### 1. 確認 Python
打開「終端機」（Launchpad 搜尋「終端機」，或按 ⌘ + 空白鍵打 terminal），輸入：

```
python3 --version
```

- 出現 `Python 3.x.x` → 有了，跳到第 2 步。
- 出現 `command not found` 或跳出「開發者工具」安裝視窗 → 到 <https://www.python.org/downloads/> 下載最新版 macOS 安裝檔，一路按繼續，裝完關掉終端機再開一次，重新確認。

> 注意：`python`（沒有 3）在 Mac 上可能不存在或是舊版，**一律用 `python3`**。

### 2. 裝編輯器 VS Code
<https://code.visualstudio.com> 下載 → 解壓縮後把 `Visual Studio Code` 拖進「應用程式」。

第一次打開後：
1. 左側方塊圖示（Extensions）→ 搜尋 `Python` → 安裝 Microsoft 出的那個。
2. 選單 `File → Open Folder…` → 選我們的課程資料夾。

### 3. 把課程資料夾放好
建議放在桌面，路徑不要有空格或中文（之後在終端機比較好打），例如：

```
~/Desktop/python/
```

### 4. 跑跑看
在終端機：

```
cd ~/Desktop/python/lesson01/code
python3 01-character.py
```

看到角色卡印出來就成功了。

> **`cd` 的快速做法**：打 `cd ` （後面空一格），然後把資料夾從 Finder **直接拖進終端機視窗**，路徑會自動補上，按 Enter。

## Windows

1. <https://www.python.org/downloads/> 下載安裝檔，**安裝第一頁一定要勾「Add Python to PATH」**，再按 Install Now。
2. VS Code 同上，安裝 Python 擴充套件。
3. 終端機用「PowerShell」或 VS Code 內建終端機。
4. 指令用 `python` 而不是 `python3`：

```
cd C:\Users\你的名字\Desktop\python\lesson01\code
python 01-character.py
```

## 三個一定要會的操作

| 操作 | 做什麼 |
|---|---|
| **⌘S**（Windows 是 Ctrl+S） | 存檔。**沒存檔就執行＝跑舊的程式** |
| **↑**（上方向鍵） | 在終端機叫回上一次打的指令，不用重打 |
| **Control + C** | 強制停掉正在跑的程式（迴圈停不下來時用） |

## 常見狀況

| 訊息 | 意思 | 怎麼辦 |
|---|---|---|
| `command not found: python3` | 沒裝好，或裝完沒重開終端機 | 關掉終端機再開一次；還是不行就重裝 |
| `No such file or directory` | 檔名打錯，或不在那個資料夾 | 先打 `ls`（Windows 是 `dir`）看看這個資料夾有什麼 |
| 改了程式但結果沒變 | 忘了存檔 | ⌘S 再執行 |
| 程式一直印個不停 | 無窮迴圈 | Control + C |
