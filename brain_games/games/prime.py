from random import randint

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_round():
    """Get is prime round."""
    correct_answer = 'yes'
    number = randint(10, 1001)
    if number < 2 or not number % 2:
        correct_answer = 'no'
    for i in range(3, number // 2 + 1):
        if not number % i:
            correct_answer = 'no'
    question = f'Question: {number}'
    return question, correct_answer
