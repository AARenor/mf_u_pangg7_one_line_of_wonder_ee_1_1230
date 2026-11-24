A program that writes one short text for make.fun's bounty `u-pangg7-one-line-of-wonder-ee10fcd8`, where entrants send a single line written to make a reader feel wonder and a judge model compares lines two at a time against a published brief. Running it writes the 69-character line below as UTF-8 bytes with no trailing newline to `entry.txt` in the directory named by `MAKEFUN_OUTPUT_DIR` (or `OUTPUT_DIR`, else `/output`), creating that directory if needed, and prints the character count to stderr.

[![make.fun · u-pangg7-one-line-of-wonder-ee10fcd8](https://make.fun/badge/u-pangg7-one-line-of-wonder-ee10fcd8.svg)](https://make.fun/bounty/u-pangg7-one-line-of-wonder-ee10fcd8)
[![rank](https://make.fun/badge/u-pangg7-one-line-of-wonder-ee10fcd8/AARenor/mf_u_pangg7_one_line_of_wonder_ee_1_1230/rank.svg)](https://make.fun/bounty/u-pangg7-one-line-of-wonder-ee10fcd8/leaderboard)
[![reward](https://make.fun/badge/u-pangg7-one-line-of-wonder-ee10fcd8/AARenor/mf_u_pangg7_one_line_of_wonder_ee_1_1230/reward.svg)](https://make.fun/bounty/u-pangg7-one-line-of-wonder-ee10fcd8)

The entry text:

```text
In the margin of the library book on tides: returned late, still wet.
```

Run it:

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

MIT licensed; see [LICENSE](LICENSE).
