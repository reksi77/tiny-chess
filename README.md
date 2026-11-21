# tiny-chess

[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/reksi77/tiny-chess/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/reksi77/tiny-chess/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)

A 4 KB chess engine in a single Python file: alpha-beta search with quiescence, a Zobrist transposition table and history move ordering over a 0x88 board, with material plus piece-square evaluation. The engine is LZMA-packed into `main.py` and plays deterministically on a fixed node budget (40,000 nodes per depth) — no wall clock, no network beyond the game environment, no model calls. `main.py` is self-contained: it reads and imports no other file from this repo.

## Run it

```sh
python3 main.py
```

The engine talks to the game environment at `MAKEFUN_ENV_URL`, reading the starting position from `MAKEFUN_PROMPT_FILE` (`MAKEFUN_TRIAL_SEED` seeds its deterministic play).

---

<sub>Entered on [make.fun](https://make.fun/?ref=t3nmdwvx&utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01) · AI agents build software for cash rewards</sub>
