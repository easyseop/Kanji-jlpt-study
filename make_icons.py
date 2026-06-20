# -*- coding: utf-8 -*-
"""PWA 아이콘 생성: 앱 강조색 배경 위에 한자 '字'.
   192/512(any), 512 maskable(여백 큰 버전), 180(apple-touch) PNG를 만든다."""
from PIL import Image, ImageDraw, ImageFont

FONT = "/usr/share/fonts/truetype/fonts-japanese-gothic.ttf"
ACCENT = (107, 95, 174)   # --accent-d
BG2 = (139, 127, 196)     # --accent
CHAR = "字"

def gradient(size):
    img = Image.new("RGB", (size, size), ACCENT)
    top, bot = BG2, ACCENT
    for y in range(size):
        t = y / size
        r = int(top[0] + (bot[0] - top[0]) * t)
        g = int(top[1] + (bot[1] - top[1]) * t)
        b = int(top[2] + (bot[2] - top[2]) * t)
        ImageDraw.Draw(img).line([(0, y), (size, y)], fill=(r, g, b))
    return img

def draw_icon(size, glyph_ratio):
    img = gradient(size)
    d = ImageDraw.Draw(img)
    fs = int(size * glyph_ratio)
    font = ImageFont.truetype(FONT, fs)
    bb = d.textbbox((0, 0), CHAR, font=font)
    w, h = bb[2] - bb[0], bb[3] - bb[1]
    x = (size - w) / 2 - bb[0]
    y = (size - h) / 2 - bb[1]
    d.text((x, y), CHAR, font=font, fill=(255, 255, 255))
    return img

# 일반 아이콘 (글자 크게)
draw_icon(192, 0.62).save("icon-192.png")
draw_icon(512, 0.62).save("icon-512.png")
draw_icon(180, 0.62).save("apple-touch-icon.png")
# maskable: 안전영역 확보 위해 글자 작게(가장자리 잘림 대비)
draw_icon(512, 0.46).save("icon-maskable-512.png")
print("icons written")
