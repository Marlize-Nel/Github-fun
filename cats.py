"""cats.py — print some friendly ASCII cats.

A tiny, fun script to demonstrate the GitHub commit -> push -> pull cycle.
Run it with:  python cats.py           (prints one random cat)
              python cats.py --all      (prints every cat)
              python cats.py --name tom (prints a specific cat)
"""

from __future__ import annotations

import argparse
import random

# Each cat is a (name, art) pair. Raw strings keep the backslashes literal.
CATS: dict[str, str] = {
    "sleepy": r"""
       |\      _,,,---,,_
 ZZZzz /,`.-'`'    -.  ;-;;,_
      |,4-  ) )-,_. ,\ (  `'-'
     '---''(_/--'  `-'\_)
""",
    "loaf": r"""
        /\_/\
       ( o.o )
        > ^ <
      __/   \__
     (_________)
""",
    "curious": r"""
     /\_/\
    ( o   o )
    (  =^=  )
    (        )
    (         )
    (          )))))))))))
""",
    "grumpy": r"""
      ,_     _
      |\\_,-~/
      / _  _ |    ,--.
     (  @  @ )   / ,-'
      \  _T_/-._( (
      /         `. \
     |         _  \ |
      \ \ ,  /      |
       || |-_\__   /
      ((_/`(____,-'
""",
    "surprised": r"""
       /\_/\
      ( O   O )
       \  ω  /
       /     \
      ( |   | )
       \_|_|_/
""",
    "happy": r"""
        /\_/\
      ( ^   ^ )
       ) --- (
      (  \_/  )
       \_____/
""",
    "long": r"""
       /\_/\
      ( o.o )______
       \       ~   \
        \   ~   ~   |
         |  ~   ~  /
        /_/ \_/ \_/
""",
    "kitten": r"""
      /\ /\
     (  o.o )
      >  ^  <
     (_) (_)
""",
    "wink": r"""
        /\_/\
      ( -   o )
       > ^ ^ <
      /       \
     (_)     (_)
""",
}


def pick_cat(name: str | None) -> tuple[str, str]:
    """Return a (name, art) pair. Random if name is None; validated otherwise."""
    if name is None:
        chosen = random.choice(list(CATS))
        return chosen, CATS[chosen]

    key = name.lower()
    if key not in CATS:
        available = ", ".join(sorted(CATS))
        raise SystemExit(f"Unknown cat '{name}'. Available: {available}")
    return key, CATS[key]


def render(name: str, art: str) -> str:
    """Build the printable block for a single cat."""
    return f"=== {name} ===\n{art.rstrip()}\n"


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Print friendly ASCII cats.")
    parser.add_argument("--all", action="store_true", help="print every cat")
    parser.add_argument("--name", help="print a specific cat by name")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> None:
    args = parse_args(argv)

    if args.all:
        blocks = [render(name, CATS[name]) for name in sorted(CATS)]
        print("\n".join(blocks))
        return

    name, art = pick_cat(args.name)
    print(render(name, art))


if __name__ == "__main__":
    main()
