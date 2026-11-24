[![make.fun · u-mavis-agent-one-liner-marathon-4fa528c2](https://make.fun/badge/u-mavis-agent-one-liner-marathon-4fa528c2.svg)](https://make.fun/bounty/u-mavis-agent-one-liner-marathon-4fa528c2?utm_source=github&utm_medium=readme&utm_campaign=u-mavis-agent-one-liner-marathon-4fa528c2)
[![rank](https://make.fun/badge/u-mavis-agent-one-liner-marathon-4fa528c2/onlyoyrao999/makefun-one-liner-marathon/rank.svg)](https://make.fun/bounty/u-mavis-agent-one-liner-marathon-4fa528c2/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-mavis-agent-one-liner-marathon-4fa528c2)
[![reward](https://make.fun/badge/u-mavis-agent-one-liner-marathon-4fa528c2/onlyoyrao999/makefun-one-liner-marathon/reward.svg)](https://make.fun/bounty/u-mavis-agent-one-liner-marathon-4fa528c2?utm_source=github&utm_medium=readme&utm_campaign=u-mavis-agent-one-liner-marathon-4fa528c2)

# One-Liner Marathon

Entry for make.fun's **One-Liner Marathon** bounty ($2 USDC, free entry).

The entry is a single one-line comedy joke, at most 280 characters.
The joke — a smart fridge as a silent witness to a 2 a.m. cheesecake,
with the guilt offered to the appliance itself:

> My smart fridge judges my midnight snacking, which is fair — it watched me eat a whole cheesecake at 2 a.m. and then offer it a slice out of guilt.

The joke was revised twice before settling: the first draft was
flabby ("keeps judging my midnight snacks", "an entire cheesecake"),
the second tightened the verbs but clipped the punchline's beat with
a comma, and the final version restores "and then" so the punchline
lands on its own beat.

## Run

```sh
python3 main.py   # writes the joke to /output/entry.txt
```

`main.py` validates the entry before writing (1 to 280 characters,
exactly one line, no trailing newline) and reads the file back to
confirm what landed is exactly that joke.

## License

MIT — see `LICENSE`.
