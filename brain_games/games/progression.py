from random import choice, randint

DESCRIPTION = 'What number is missing in the progression?'


def make_progression():
    """Generate arithemtic progression."""
    initial_number = randint(1, 100)
    delta = randint(1, 25)
    length = 10
    maximum_number = (delta * length) + initial_number
    return range(initial_number, maximum_number, delta)


def make_question():
    """Generate game question."""
    prog = make_progression()
    secret = choice(prog)
    progression = ' '.join([
        '..' if num == secret else str(num) for num in prog
    ])
    question = f'Question: {progression}'
    return (question, str(secret))
