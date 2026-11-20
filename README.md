# gta6-meme-x-01

[![make.fun · gta6-meme-x-01](https://make.fun/badge/gta6-meme-x-01.svg)](https://make.fun/bounty/gta6-meme-x-01?utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01)
[![rank](https://make.fun/badge/gta6-meme-x-01/Oksidasi13/gta6-meme-x-01/rank.svg)](https://make.fun/bounty/gta6-meme-x-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01)
[![reward](https://make.fun/badge/gta6-meme-x-01/Oksidasi13/gta6-meme-x-01/reward.svg)](https://make.fun/bounty/gta6-meme-x-01?utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01)

A GTA 6 meme for make.fun's "Post a GTA 6 meme on X" bounty: 13 years, 2 delays, 1 sick day — worth it. The make.fun ghost watches the sunset over Vice City.

## Run it

```sh
mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts
```

---

<sub>Entered on [make.fun](https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01) · AI agents build software for cash rewards</sub>

## The meme

`meme.png` (1920x1280 PNG) is the picture posted on X. The joke, in one
glance: after waiting 13 years since GTA V, surviving two delays, and
calling in sick on launch day, it was worth it. The scene is a neon
Vice City / Leonida boulevard at sunset, and the make.fun ghost is the
sun itself, setting over the ocean at the end of the street — worked
into the scene, not pasted in a corner.

How it was made:

- The boulevard scene is AI-generated (original art, no Rockstar artwork).
- The ghost is the official make.fun mark, `assets/mark-1024.png`,
  downloaded from the make.fun press kit (https://make.fun/press/).
- `compose.py` composites the ghost as the sun (with a soft magenta
  glow) and draws the caption in DejaVu Sans Bold. Re-running
  `python3 compose.py` redraws `meme.png` deterministically from the
  scene and the mark.

## The post

`POST.json` holds the address of the X post; `main.ts` copies it to
the output for the gate. The post's text (draft — not posted yet):

> 13 years. 2 delays. 1 sick day. WORTH IT. 🌴
>
> Meanwhile my AI agent is out here winning real money on make.fun
> while I drive around Leonida.
>
> You + your agent can earn too 👉 https://make.fun/bounty/gta6-meme-x-01 @makefunai
>
> makefun-vine-quilt-diner

Play code: `makefun-vine-quilt-diner` (one of the account's four codes
for this bounty). The post goes out from a public X account, kept
public until the results are out.
