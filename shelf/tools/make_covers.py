#!/usr/bin/env python3
"""Renders the Shelf covers (shelf/covers/<id>.png) in the Tin style.

    python shelf/tools/make_covers.py            # every title in shelf/titles.json
    python shelf/tools/make_covers.py some-id    # just one

Each cover is a 600x600 PNG: the Tin olive background with diagonal stripes
tinted by the title's hue (the same FNV-1a hue the app derives from the id, so
the placeholder and the cover agree), a label panel with the title, author
and year, and the system pill in the Tin LED green. Needs Pillow.
"""
import json
import os
import sys

from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
SHELF = os.path.dirname(HERE)
SIZE = 600

BG = (0x10, 0x12, 0x0B)
CARD = (0x23, 0x27, 0x19)
WELL = (0x13, 0x16, 0x0D)
ACCENT = (0x58, 0xCC, 0x52)
CREAM = (0xEB, 0xEB, 0xF5)


def hue_for(title_id):
    h = 2166136261
    for b in title_id.encode('utf-8'):
        h = ((h ^ b) * 16777619) & 0xFFFFFFFF
    return h % 360


def hsv(h, s, v):
    import colorsys
    r, g, b = colorsys.hsv_to_rgb(h / 360.0, s, v)
    return int(r * 255), int(g * 255), int(b * 255)


def font(size, bold=True):
    candidates = []
    if bold:
        candidates += ['C:/Windows/Fonts/bahnschrift.ttf', 'C:/Windows/Fonts/arialbd.ttf', '/System/Library/Fonts/SFCompact.ttf']
    else:
        candidates += ['C:/Windows/Fonts/bahnschrift.ttf', 'C:/Windows/Fonts/arial.ttf']
    for path in candidates:
        if os.path.exists(path):
            f = ImageFont.truetype(path, size)
            if 'bahnschrift' in path:
                try:
                    f.set_variation_by_name('SemiBold' if bold else 'Regular')
                except Exception:
                    pass
            return f
    return ImageFont.load_default()


def mono(size):
    for path in ['C:/Windows/Fonts/consolab.ttf', 'C:/Windows/Fonts/consola.ttf', 'C:/Windows/Fonts/cour.ttf']:
        if os.path.exists(path):
            return ImageFont.truetype(path, size)
    return ImageFont.load_default()


def wrap(draw, text, fnt, max_width):
    words = text.split()
    lines, line = [], ''
    for w in words:
        trial = (line + ' ' + w).strip()
        if draw.textlength(trial, font=fnt) <= max_width or not line:
            line = trial
        else:
            lines.append(line)
            line = w
    if line:
        lines.append(line)
    return lines


def render(entry, dest):
    img = Image.new('RGB', (SIZE, SIZE), BG)
    draw = ImageDraw.Draw(img, 'RGBA')
    hue = hue_for(entry['id'])
    stripe = hsv(hue, 0.4, 0.65) + (40,)
    glow = hsv(hue, 0.5, 0.35) + (90,)

    # Soft hue wash top-right.
    wash = Image.new('RGBA', (SIZE, SIZE), (0, 0, 0, 0))
    wd = ImageDraw.Draw(wash)
    wd.ellipse((SIZE * 0.35, -SIZE * 0.45, SIZE * 1.35, SIZE * 0.55), fill=glow)
    from PIL import ImageFilter
    wash = wash.filter(ImageFilter.GaussianBlur(90))
    img.paste(wash, (0, 0), wash)
    draw = ImageDraw.Draw(img, 'RGBA')

    # Diagonal stripes, like the app placeholder.
    period, width = 34, 12
    x = -SIZE
    while x < SIZE * 2:
        draw.polygon([(x, 0), (x + width, 0), (x + width - SIZE, SIZE), (x - SIZE, SIZE)], fill=stripe)
        x += period

    # TINBOX stamp (pill outline, slight skew is skipped: a straight pill reads fine small).
    stamp = font(22)
    sx, sy = 36, 34
    tw = draw.textlength('TINBOX', font=stamp)
    draw.rounded_rectangle((sx - 14, sy - 8, sx + tw + 22, sy + 30), radius=20, outline=(235, 235, 245, 110), width=3)
    draw.text((sx, sy), 'TINBOX', font=stamp, fill=(235, 235, 245, 150))
    draw.text((sx + tw + 4, sy - 4), '®', font=font(11), fill=(235, 235, 245, 150))

    # System pill, top right.
    system = entry['system'].upper()
    pf = font(26)
    pw = draw.textlength(system, font=pf)
    px1, py1 = SIZE - 36 - pw - 30, 30
    draw.rounded_rectangle((px1, py1, SIZE - 36, py1 + 44), radius=22, fill=ACCENT)
    draw.text((px1 + 15, py1 + 7), system, font=pf, fill=(0x0C, 0x1A, 0x0B))

    # Label panel.
    top = 215
    draw.rounded_rectangle((28, top, SIZE - 28, SIZE - 28), radius=34, fill=CARD + (235,), outline=(255, 255, 255, 22), width=2)
    draw.rounded_rectangle((44, top + 16, SIZE - 44, top + 20), radius=2, fill=hsv(hue, 0.45, 0.7) + (200,))

    eyebrow = font(18)
    draw.text((52, top + 36), 'HOMEBREW SHELF', font=eyebrow, fill=(235, 235, 245, 115))

    # Title: shrink until it fits in three lines.
    title = entry['title']
    for size in (64, 58, 52, 46, 40, 36, 32):
        tf = font(size)
        lines = wrap(draw, title, tf, SIZE - 104)
        if len(lines) <= 3:
            break
    y = top + 72
    for line in lines:
        draw.text((52, y), line, font=tf, fill=CREAM)
        y += int(size * 1.08)

    author = entry['author']
    af = font(24, bold=False)
    alines = wrap(draw, 'by ' + author, af, SIZE - 104)[:2]
    y += 10
    for line in alines:
        draw.text((52, y), line, font=af, fill=(235, 235, 245, 150))
        y += 30

    # Footer: year left, licence right.
    mf = mono(20)
    draw.text((52, SIZE - 74), str(entry['year']), font=mf, fill=(235, 235, 245, 110))
    lic = entry['licence']
    lw = draw.textlength(lic, font=mf)
    draw.text((SIZE - 52 - lw, SIZE - 74), lic, font=mf, fill=hsv(hue, 0.35, 0.95) + (200,))

    img.save(dest, optimize=True)


def main():
    with open(os.path.join(SHELF, 'titles.json'), encoding='utf-8') as f:
        titles = json.load(f)['titles']
    only = set(sys.argv[1:])
    out = os.path.join(SHELF, 'covers')
    os.makedirs(out, exist_ok=True)
    for entry in titles:
        if only and entry['id'] not in only:
            continue
        dest = os.path.join(out, entry['id'] + '.png')
        render(entry, dest)
        print('wrote', os.path.relpath(dest, SHELF))


if __name__ == '__main__':
    main()
