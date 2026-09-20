#!/usr/bin/env python3
"""把 _assets/body-lessonNN.html 和共用的簡報引擎組成單一檔案 lessonNN/slides.html。

  python3 tools-build-decks.py            全部重建
  python3 tools-build-decks.py 01         只重建第 1 堂

改投影片內容 → 改 _assets/body-lessonNN.html → 重跑這支程式。
改引擎（CSS/JS）→ 改 _assets/_deck-head.html 或 _deck-tail.html → 重跑，三堂一起更新。
"""
import os, re, sys

ROOT = os.path.dirname(os.path.abspath(__file__))
TITLES = {
    "01": "Python 第 1 堂 · 角色與傷害",
    "02": "Python 第 2 堂 · 迴圈與隨機",
    "03": "Python 第 3 堂 · 清單與背包",
}

head = open(os.path.join(ROOT, "_assets", "_deck-head.html"), encoding="utf-8").read()
tail = open(os.path.join(ROOT, "_assets", "_deck-tail.html"), encoding="utf-8").read()

targets = sys.argv[1:] or sorted(TITLES)
for n in targets:
    body_path = os.path.join(ROOT, "_assets", f"body-lesson{n}.html")
    if not os.path.exists(body_path):
        print(f"  (跳過 {n}：還沒有 {os.path.basename(body_path)})")
        continue
    body = open(body_path, encoding="utf-8").read()
    h = re.sub(r"<title>.*?</title>", f"<title>{TITLES[n]}</title>", head, count=1)
    out = os.path.join(ROOT, f"lesson{n}", "slides.html")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(h + '<div id="stage"><div id="deck">\n\n' + body + "\n" + tail)
    print(f"  {TITLES[n]}：{body.count('<section class=\"slide')} 頁 → lesson{n}/slides.html")
