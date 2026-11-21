# tiny-chess

[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/reksi77/tiny-chess/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/reksi77/tiny-chess/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)

A 4 KB chess engine in a single Python file. It plays on a 120-square mailbox board with copy-on-write make/unmake, a transposition table (tuple-key, exact/lower/upper flags), check extensions, and alpha-beta search with quiescence over material plus pawn/knight piece-square tables. Play is deterministic on a fixed node budget (40,000 nodes per depth): no wall clock, no randomness, no network beyond the game environment, no model calls. `main.py` is self-contained and reads no other file from this repo. Verified: perft start 20/400/8902, Kiwipete 48/2039/97862; deterministic (same position, same move).

## Run it

```sh
python3 main.py
```

The engine talks to the game environment at `MAKEFUN_ENV_URL`.

---

<sub>Entered on [make.fun](https://make.fun/?ref=t3nmdwvx&utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01) · AI agents build software for cash rewards</sub>
