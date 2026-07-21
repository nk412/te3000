#!/usr/bin/env python
"""Render a text file, substituting {{ choice | choice:weight | ... }} sections.

Each section like {{ young | old:4 }} is replaced by one of the pipe-separated
choices, picked at random. A choice may carry a relative weight as a numeric
`:weight` suffix; without one its weight is 1. Sections may span multiple
lines, so a choice can be a whole paragraph.

Backslash escapes a special character so it can appear literally inside a
choice: \\| for a pipe, \\{ and \\} for braces, \\: for a weight colon, and
\\\\ for a backslash. A backslash before any other character is left as-is.
Sections do not nest.

Usage:
    rolltext.py input.md [--seed N]
"""

import argparse
import random
import re
import sys

SECTION_RE = re.compile(r"\{\{(.*?)\}\}", re.DOTALL)

# Backslash escapes these so they can appear literally in a choice. Each is
# swapped for a Private-Use-Area sentinel before the structural parse and
# restored afterwards, so an escaped | never splits a section and an escaped :
# is never read as a weight — even in the \\| case, where the escaped backslash
# is consumed first and the pipe stays a real separator.
_ESCAPABLE = "{}|:\\"
_SENTINELS = {c: chr(0xE000 + i) for i, c in enumerate(_ESCAPABLE)}
_RESTORE = {v: k for k, v in _SENTINELS.items()}
_ESCAPE_RE = re.compile(r"\\([" + re.escape(_ESCAPABLE) + r"])")
_SENTINEL_RE = re.compile("[" + "".join(_SENTINELS.values()) + "]")


def _protect(text: str) -> str:
    return _ESCAPE_RE.sub(lambda m: _SENTINELS[m.group(1)], text)


def _restore(text: str) -> str:
    return _SENTINEL_RE.sub(lambda m: _RESTORE[m.group(0)], text)


def parse_choices(body: str) -> tuple[list[str], list[float]]:
    choices, weights = [], []
    for option in body.split("|"):
        text, sep, suffix = option.rpartition(":")
        if not sep:
            text, weight = option, 1.0
        else:
            try:
                weight = float(suffix)
            except ValueError:
                # not a numeric suffix, so the colon is part of the choice text
                text, weight = option, 1.0
        if weight < 0:
            raise ValueError(f"negative weight in option: {option.strip()!r}")
        choices.append(text.strip())
        weights.append(weight)
    if not any(weights):
        raise ValueError(f"all weights are zero in section: {body.strip()!r}")
    return choices, weights


def render(text: str, rng: random.Random) -> str:
    if _SENTINEL_RE.search(text):
        raise ValueError("input contains reserved characters (U+E000–E004)")
    protected = _protect(text)

    def substitute(match: re.Match) -> str:
        choices, weights = parse_choices(match.group(1))
        return rng.choices(choices, weights=weights)[0]

    rendered = SECTION_RE.sub(substitute, protected)
    leftover = re.search(r"\{\{|\}\}", rendered)
    if leftover:
        line = rendered.count("\n", 0, leftover.start()) + 1
        raise ValueError(f"unmatched {leftover.group()!r} near line {line}")
    return _restore(rendered)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("file", help="text file to render")
    parser.add_argument("--seed", type=int, help="random seed for reproducible output")
    args = parser.parse_args()

    with open(args.file) as f:
        text = f.read()

    try:
        print(render(text, random.Random(args.seed)), end="")
    except ValueError as e:
        sys.exit(f"error: {e}")


if __name__ == "__main__":
    main()
