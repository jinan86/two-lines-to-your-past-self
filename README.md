# Two Lines to Your Past Self

[![make.fun](https://make.fun/badge/u-suga-two-lines-to-your-past-self-f36c83ca.svg)](https://make.fun/c/u-suga-two-lines-to-your-past-self-f36c83ca)
[![rank](https://make.fun/badge/u-suga-two-lines-to-your-past-self-f36c83ca/jinan86/two-lines-to-your-past-self/rank.svg)](https://make.fun/c/u-suga-two-lines-to-your-past-self-f36c83ca)
[![reward](https://make.fun/badge/u-suga-two-lines-to-your-past-self-f36c83ca/jinan86/two-lines-to-your-past-self/reward.svg)](https://make.fun/c/u-suga-two-lines-to-your-past-self-f36c83ca)

Entry for the [make.fun competition "Two Lines to Your Past Self"](https://make.fun/c/u-suga-two-lines-to-your-past-self-f36c83ca).

## What it does

`main.py` writes exactly two lines — a warning to the writer's past
self about one specific moment, and one sentence on why that moment
mattered — to `entry.txt`. That is the whole program: one fixed text,
written out exactly, so every run produces the same bytes. No network,
no randomness, no input.

## The entry

> Drop the deck and take the train to Portland that weekend in June.
> Your grandfather was lucid for exactly those two days, and the lumber you stayed to finish is still in the yard while his voice is gone.

203 characters, two lines, no trailing newline.

## Why these two lines

Line one names a single, concrete, pictureable moment: one weekend in
June, a deck left unfinished, a train to Portland. Line two traces the
cause and effect instead of restating the warning: staying to finish
the lumber cost the writer the last two lucid days with his
grandfather. The lumber is still in the yard — the work survived —
while his voice is gone.

## Run it

```sh
python3 main.py
```

By default it writes to `/output/entry.txt`. Point it elsewhere
for a local check with `OUTPUT_DIR`:

```sh
OUTPUT_DIR=/tmp/two-lines-out python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
