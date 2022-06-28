# Add docstring.

"""Add new function."""

import prompt


def welcome_user():
    """Ask username."""
    name = prompt.string('May I have your name? ')
    return print(f'Hello, {name}!')
