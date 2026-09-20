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

## Tab 或空白鍵「有時候按不出來」

這是初學最常見的卡關，**九成不是壞掉**。照順序測：

### 第 0 步：先確認是不是 VS Code 的問題
打開「文字編輯」（TextEdit）或任何一個輸入框，按 Tab 和空白鍵。

- **那裡也失常** → 跳到下面的「輸入法」與「鍵盤硬體」。
- **只有 VS Code 失常** → 看「VS Code 設定」。

### 輸入法（空白鍵最常見的原因）
螢幕右上角的輸入法如果是**注音／拼音**，空白鍵是拿來「選字」的，不會打出空格。
寫程式時一定要切回 **ABC／英文**（按 **Caps Lock** 或 **⌃空白鍵** 切換）。

### Tab 按了沒反應、或跳到別的區域
這就是 **Tab Moves Focus 模式**：Tab 不再縮排，改成在視窗各區域之間移動焦點。

1. 看視窗最下面的狀態列，會出現 **"Tab Moves Focus"**。
2. 按 **⌃⇧M**（Control + Shift + M）關掉；或 ⇧⌘P 搜尋 `Toggle Tab Key Moves Focus`。
3. 一勞永逸：把 `notes/vscode-student-settings.json` 貼進設定，裡面有
   `"editor.tabFocusMode": false` 和 `"editor.accessibilitySupport": "off"`
   （VS Code 偵測到螢幕閱讀器／輔助使用時，也會自動把 Tab 變成切換焦點）。

### 空白鍵卡住，點一下別的地方再點回來就好
這是**焦點跑掉**，不是鍵盤壞掉——游標看起來在編輯器裡，其實鍵盤輸入被別的元件接走了。

1. 先試：⇧⌘P 執行 `Developer: Toggle Keyboard Shortcuts Troubleshooting`，
   再按幾次空白鍵和 Tab，看 Output 面板記錄到什麼——
   有記錄到但沒反應＝被某個指令吃掉；完全沒記錄＝焦點不在編輯器。
2. 關掉硬體加速（Intel Mac 上這個很常見）：⇧⌘P → `Preferences: Configure Runtime Arguments`，
   在 `argv.json` 加一行 `"disable-hardware-acceleration": true`，重開 VS Code。
3. 還是有的話，找是哪個擴充套件：⇧⌘P → `Help: Start Extension Bisect`，
   它會自動二分法關擴充套件，幾輪就能指出兇手。
4. 順手把 VS Code 更新到最新版。

### AI 補完（順便處理）
裝了 Copilot／Gemini Code Assist 的話，出現灰色建議文字時 Tab 會變成「接受建議」。
初學階段建議直接關掉——不然是它在寫程式，不是她。同一份設定檔已經幫你關好。

### 鍵盤硬體
2016～2019 年的 MacBook Pro（**蝶式鍵盤**）有公認的問題：某些鍵會**間歇性沒反應或連打**，
空白鍵特別常見。判斷方式：

- 接一個**外接鍵盤**試試，外接正常＝內建鍵盤的問題。
- 「文字編輯」裡也一樣失常，而且跟輸入法無關 → 幾乎可以確定是硬體。

Apple 曾有「鍵盤服務計畫」免費更換（自購買日起 4 年內），現在多半已過期，
可以帶去 Apple 直營店或授權維修中心查一下機器的保固狀態。
上課的臨時解法：**接一個外接鍵盤**就好，不影響進度。

## 常見狀況

| 訊息 | 意思 | 怎麼辦 |
|---|---|---|
| `command not found: python3` | 沒裝好，或裝完沒重開終端機 | 關掉終端機再開一次；還是不行就重裝 |
| `No such file or directory` | 檔名打錯，或不在那個資料夾 | 先打 `ls`（Windows 是 `dir`）看看這個資料夾有什麼 |
| 改了程式但結果沒變 | 忘了存檔 | ⌘S 再執行 |
| 程式一直印個不停 | 無窮迴圈 | Control + C |
| Tab 沒有縮排，反而補出一整行程式 | AI 補完搶走了 Tab | 看上面「Tab 或空白鍵按不出來」 |
| 空白鍵打不出空格 | 輸入法在注音模式 | 按 Caps Lock 切回英文 |
