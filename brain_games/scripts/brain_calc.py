# -*- coding example -*-.

"""Add calc game."""

# !/usr/bin/env python

from brain_games.engine import engine
from brain_games.games import calc


def main():
    """Run calc game."""
    engine(calc)


if __name__ == '__main__':
    main()
