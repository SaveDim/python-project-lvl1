from random import choice, randint

DESCRIPTION = 'What is the result of the expression?'


def get_round():
    """Generate game question."""
    num_1 = randint(1, 101)
    num_2 = randint(1, 101)

    correct_answers = {
        '+': num_1 + num_2,
        '-': num_1 - num_2,
        '*': num_1 * num_2
        }

    random_key = choice(list(correct_answers.keys()))
    correct_answer = correct_answers[random_key]
    question = f'Question: {num1} {random_key} {num2}'

    return question, correct_answer
