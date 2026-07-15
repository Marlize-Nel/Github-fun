# Github-fun

A tiny project to practice the GitHub commit → push → pull cycle. It ships a fun
script that prints friendly ASCII cats.

## Usage

Run from the project root:

```bash
python3 cats.py            # print one random cat
python3 cats.py --all      # print every cat
python3 cats.py --name loaf # print a specific cat by name
```

Available cats: `sleepy`, `loaf`, `curious`, `grumpy`, `surprised`, `happy`,
`chonk`, `kitten`, `wink`.

## GitHub Actions

`.github/workflows/cats.yml` runs the script on GitHub to print the cats in CI.
