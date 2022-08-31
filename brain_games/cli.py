# Add docstring.

"""Add greeting function."""

import prompt


def get_user_name():
    """Prompt user for his/her name."""
    print('Welcome to the Brain Games!')
    return prompt.string('May I have your name? ')
