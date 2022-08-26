import random
import prompt


def welcome_user():
    """Ask username."""
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def get_result(answer, correct_answer, name):
    """Getting user answer."""
    if answer == str(correct_answer):
        print('Correct!')
    else:
        print(f"'{answer}' is wrong answer ;(."
              f"Correct answer was '{correct_answer}'.")
        print(f"Let's try again, {name}!")


def get_correct_answer():

    num_1 = random.randint(1, 101)
    num_2 = random.randint(1, 101)

    correct_answers = {
        '+': num_1 + num_2,
        '-': num_1 - num_2,
        '*': num_1 * num_2
    }

    random_key = random.choice(list(correct_answers.keys()))
    correct_answer = correct_answers[random_key]

    print(f'Question: {num_1} {random_key} {num_2}')

    return correct_answer
