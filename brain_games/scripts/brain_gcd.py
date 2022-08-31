# -*- coding example -*-.

"""Add gcd game."""

# !/usr/bin/env python

from brain_games.engine import engine
from brain_games.games import gcd


def main():
    """Run gcd game."""
    engine(gcd)


if __name__ == '__main__':
    main()
