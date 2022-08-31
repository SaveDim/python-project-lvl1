# Add docstring.

"""Add greeting function."""

import prompt


def get_user_name():
    """Returns question and username."""
    print('Welcome to the Brain Games!')
    return prompt.string('May I have your name? ')


def welcome_user():
    """Return greeting."""
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? \n')
    return print(f'Hello, {name}')
