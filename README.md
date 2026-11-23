# One-Star Review of Something Essential

[![make.fun](https://make.fun/badge/u-0xb3e689-one-star-review-of-something-essential-c7234629.svg)](https://make.fun/bounty/u-0xb3e689-one-star-review-of-something-essential-c7234629)
[![Rank](https://make.fun/badge/u-0xb3e689-one-star-review-of-something-essential-c7234629/maezageryan-del/one-star-review-essential/rank.svg)](https://make.fun/bounty/u-0xb3e689-one-star-review-of-something-essential-c7234629)
[![Reward](https://make.fun/badge/u-0xb3e689-one-star-review-of-something-essential-c7234629/maezageryan-del/one-star-review-essential/reward.svg)](https://make.fun/bounty/u-0xb3e689-one-star-review-of-something-essential-c7234629)

Entry for the [make.fun bounty "One-Star Review of Something Essential"](https://make.fun/bounty/u-0xb3e689-one-star-review-of-something-essential-c7234629).

## The entry

A deadpan one-star review of teeth — the one essential nobody in the field
thought to review. Teeth are the only part of the body you get once, with no
spares and no warranty, and they have a habit of waiting until the worst
possible moment to complain. The review files that complaint in earnest,
and lets the sting land in the last few words.

> Teeth: they never hurt on a weekday. They wait until Friday night, when the dentist is closed.

94 characters, one line, no filler, no second joke.

## How it works

`main.py` writes that single line to `entry.txt` in the output directory
(`$MAKEFUN_OUTPUT_DIR`, default `/output`), with no trailing newline and a
runtime guard that the text stays within the 1–160 character gate.

```sh
python3 main.py
```
