# Add docstring.

"""Add greeting function."""

import prompt


def welcome_user():
    """Ask username."""
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def get_answer():
    """Getting user answer."""
