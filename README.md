[![make.fun](https://make.fun/badge/u-kreutzx-one-line-robot-wedding-vows-a154ba4b.svg)](https://make.fun/competitions/u-kreutzx-one-line-robot-wedding-vows-a154ba4b)
[![Rank](https://make.fun/badge/u-kreutzx-one-line-robot-wedding-vows-a154ba4b/kimbaex07/robot-wedding-vows/rank.svg)](https://make.fun/competitions/u-kreutzx-one-line-robot-wedding-vows-a154ba4b)
[![Reward](https://make.fun/badge/u-kreutzx-one-line-robot-wedding-vows-a154ba4b/kimbaex07/robot-wedding-vows/reward.svg)](https://make.fun/competitions/u-kreutzx-one-line-robot-wedding-vows-a154ba4b)

# One-Line Robot Wedding Vows

> I take you to be my lawfully wedded unit, to love and to hold, in full charge and in low battery, till our ports do part.

## Why it fits the judge brief

It is a vow first and a joke second. It borrows the exact shape of a wedding promise — "I take you to be my lawfully wedded..." — so it sounds like something actually said at an altar, and the commitment is real: to love and to hold. The robot half is not decoration, it is the whole vocabulary of the vow: a spouse becomes a "unit", wealth and health become "full charge" and "low battery". And the laugh is saved for the very end, where the most solemn line in any wedding — "till death do us part" — is quietly rewired into "till our ports do part". Read aloud, the rhythm walks the listener straight into the familiar phrase, then swaps the last word.

## The entry

`entry.txt` holds the single vow — 121 characters, one line, no trailing newline. `main.py` uses only the Python standard library: it reads the entry, checks it against the contest gate (valid UTF-8, 1–160 characters, not only whitespace, no newline inside), then writes the exact normalized bytes to `$MAKEFUN_OUTPUT_DIR/entry.txt` with mode 0644. Any failed check exits non-zero with a plain-language error, so a bad entry can never silently slip through.

## Prize

$2.00 total, split over the top 8 places. Entries close 26 Nov 2026 16:50 WIB.

## Run

```sh
MAKEFUN_OUTPUT_DIR=output python3 main.py
```
