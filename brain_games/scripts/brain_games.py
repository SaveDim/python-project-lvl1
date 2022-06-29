# -*- coding example -*-.

"""Add greeting to the game."""

#!/usr/bin/env python

from brain_games.cli import welcome_user


def main():
    """Print greet and ask username."""
    # Simple script logic.
    print('Welcome to the Brain Games!')
    welcome_user()


if __name__ == '__main__':
    main()
