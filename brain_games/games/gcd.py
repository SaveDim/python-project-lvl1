from math import gcd
from random import randint

DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def get_round():
    """Generate game question."""
    num1 = randint(1, 101)
    num2 = randint(1, 101)
    question = f'Question: {num1} {num2}'
    correct_answer = str(gcd(num1, num2))
    return question, correct_answer
