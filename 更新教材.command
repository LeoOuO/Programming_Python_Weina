#!/bin/bash
# 點兩下就會執行：把老師更新的教材抓下來。
# 你寫在 mywork/ 裡的東西不會被動到。
cd "$(dirname "$0")" || exit 1

echo "============================================"
echo "   更新教材"
echo "============================================"
echo
git pull
code=$?
echo
if [ $code -eq 0 ]; then
  echo "更新完成。你的 mywork/ 資料夾沒有被動到。"
else
  echo "更新沒有成功（上面有訊息）。把整個視窗截圖給老師看就好，不要自己亂改。"
fi
echo
echo "按 Enter 關閉這個視窗。"
read -r
