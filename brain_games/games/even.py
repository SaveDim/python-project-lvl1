from brain_games.engine import generate_number

DESCRIPTION = 'Answer "yes" if number even otherwise answer "no".'


def make_question():
    """Generate game question."""
    number = generate_number()
    question = f'Question: {number}'
    answer = correct_answer(number)
    return (question, answer)


def correct_answer(number):
    """Return expected answer."""
    return 'no' if number % 2 else 'yes'
