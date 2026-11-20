#!/usr/bin/env python3
"""Compose the gta6-meme-x-01 meme: Vice City sunset scene + make.fun ghost
mark as the setting sun + caption text. Output: meme.png (1920x1280 PNG).

Layout (1920x1280):
  - top caption block, white bold with black stroke:
        13 YEARS. / 2 DELAYS. / 1 SICK DAY.
  - punchline in make.fun magenta with white stroke: WORTH IT.
  - the ghost mark pasted as the sun over the ocean at the end of the
    street, with a soft magenta glow, so it is worked into the scene
    (not a corner sticker) and stays recognisable when shrunk to 480px.
  - small "make.fun" tag at the bottom.
"""
from PIL import Image, ImageDraw, ImageFont, ImageFilter

ENTRY = "/home/hatch/workspace/makefun/gta6-meme-x-01-entry"
SCENE = ENTRY + "/assets/scene.png"
MARK = ENTRY + "/assets/mark-1024.png"
OUT = ENTRY + "/meme.png"

BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
MAGENTA = (196, 28, 131)  # make.fun disc magenta

base = Image.open(SCENE).convert("RGB")
W, H = base.size  # 1920 x 1280
draw = ImageDraw.Draw(base)

# --- soft magenta glow where the sun will sit (centre of the horizon) ---
sun_cx, sun_cy, sun_r = 960, 745, 165
glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
gd = ImageDraw.Draw(glow)
for i in range(60, 0, -1):
    a = int(70 * (1 - i / 60) ** 2)
    r = sun_r + i * 6
    gd.ellipse([sun_cx - r, sun_cy - r, sun_cx + r, sun_cy + r],
               fill=(255, 90, 180, a))
glow = glow.filter(ImageFilter.GaussianBlur(40))
base = Image.alpha_composite(base.convert("RGBA"), glow)
draw = ImageDraw.Draw(base)

# --- ghost mark as the sun (circular badge, transparent corners) ---
mark = Image.open(MARK).convert("RGBA").resize((sun_r * 2, sun_r * 2),
                                               Image.LANCZOS)
base.paste(mark, (sun_cx - sun_r, sun_cy - sun_r), mark)
draw = ImageDraw.Draw(base)


def centred(text, font, y, fill, stroke_fill, stroke_width):
    bbox = draw.textbbox((0, 0), text, font=font, stroke_width=stroke_width)
    tw = bbox[2] - bbox[0]
    draw.text(((W - tw) / 2, y), text, font=font, fill=fill,
              stroke_width=stroke_width, stroke_fill=stroke_fill)


# --- top caption block ---
f_big = ImageFont.truetype(BOLD, 104)
centred("13 YEARS.", f_big, 36, (255, 255, 255), (0, 0, 0), 8)
centred("2 DELAYS.", f_big, 158, (255, 255, 255), (0, 0, 0), 8)
centred("1 SICK DAY.", f_big, 280, (255, 255, 255), (0, 0, 0), 8)

# --- punchline ---
f_punch = ImageFont.truetype(BOLD, 112)
centred("WORTH IT.", f_punch, 408, MAGENTA, (255, 255, 255), 6)

# --- make.fun tag at the bottom ---
f_tag = ImageFont.truetype(BOLD, 58)
centred("make.fun", f_tag, 1152, (255, 255, 255), (0, 0, 0), 4)

base.convert("RGB").save(OUT, "PNG", optimize=True)
print("wrote", OUT, base.size)
