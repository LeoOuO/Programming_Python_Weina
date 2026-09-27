#!/bin/bash
# 點兩下就會執行：把今天要練習的檔案複製到 mywork/，然後打開資料夾。
# 已經存在的檔案不會被覆蓋，所以不用擔心把自己寫過的東西蓋掉。
cd "$(dirname "$0")" || exit 1

echo "============================================"
echo "   Python 課  -  開始上課"
echo "============================================"
echo
echo "有教材的堂數："
for d in lesson0*/code; do
  n="${d%%/*}"
  echo "   ${n#lesson}) ${n}"
done
echo
read -r -p "今天上第幾堂？輸入數字（例如 1）： " num

n=$(printf "%02d" "$num" 2>/dev/null)
src="lesson${n}/code"
dst="mywork/lesson${n}"

if [ ! -d "$src" ]; then
  echo
  echo "找不到 $src ，是不是打錯數字了？"
  echo "按 Enter 關閉。"
  read -r
  exit 1
fi

mkdir -p "$dst"
copied=0
kept=0
for f in "$src"/*.py; do
  name=$(basename "$f")
  if [ -e "$dst/$name" ]; then
    kept=$((kept + 1))                 # 已經有了 = 你之前寫過的，保留
  else
    cp "$f" "$dst/$name"
    copied=$((copied + 1))
  fi
done

echo
echo "複製了 $copied 個新檔案到  $dst"
[ "$kept" -gt 0 ] && echo "保留了 $kept 個你之前寫過的檔案（沒有被覆蓋）"
echo
echo "今天要打開的檔案都在這個資料夾裡："
echo "   $(pwd)/$dst"
echo
open "$dst"
echo "按 Enter 關閉這個視窗。"
read -r
