"""Add brain_logic for each game."""


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
    action_lst = ['+', '-', '*']
    random_index = random.randint(0, len(action_lst) - 1)
    correct_answer = 0
    num_1 = random.randint(1, 101)
    num_2 = random.randint(1, 101)
    if action_lst[random_index] == '+':
        print(f'Question: {num_1} + {num_2}')
        correct_answer = num_1 + num_2
    elif action_lst[random_index] == '-':
        print(f'Question: {num_1} - {num_2}')
        correct_answer = num_1 - num_2
    elif action_lst[random_index] == '*':
        print(f'Question: {num_1} * {num_2}')
        correct_answer = num_1 * num_2
    return correct_answer


def even_game():
    """Even game code."""
    name = welcome_user()
    counter = 0
    print('Answer "yes" if number is even, otherwise answer "no".')
    for _ in range(3):
        question = random.randint(1, 101)
        if question % 2 == 0:
            correct_answer = 'yes'
        else:
            correct_answer = 'no'
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')
        get_result(answer, correct_answer, name)
        counter += 1
        if answer != correct_answer:
            break
        if counter == 3:
            print(f"Congratulations, {name}!")


def calc_game():
    """Calc game code."""
    name = welcome_user()
    print('What is the result of the expression?')
    counter = 0
    for _ in range(3):
        correct_answer = get_correct_answer()
        answer = prompt.string('Your answer: ')
        counter += 1
        get_result(answer, correct_answer, name)
        if str(answer) != str(correct_answer):
            break
    if counter == 3:
        print(f"Congratulations, {name}!")


def find_gcd():
    """Gcd game code."""
    name = welcome_user()
    counter = 0
    print('Find the greatest common divisor of given numbers.')
    for _ in range(3):
        num_1, num_2 = random.randint(1, 101), random.randint(1, 101)
        correct_answer = num_2
        print(f'Question: {num_1} {num_2}')
        while correct_answer > 0:
            if num_1 % correct_answer == 0 and num_2 % correct_answer == 0:
                break
            correct_answer -= 1
        answer = prompt.string('Your answer: ')
        get_result(answer, correct_answer, name)
        if str(answer) != str(correct_answer):
            break
        counter += 1
    if counter == 3:
        print(f"Congratulations, {name}!")


def find_skipped_number():
    """Progression game code."""
    name = welcome_user()
    counter = 0
    print('What number is missing in the progression?')
    for _ in range(3):
        num = random.randint(2, 6)
        progression = [(i * num) for i in range(2, 12)]
        random_index = random.randint(0, len(progression) - 1)
        progression[random_index] = '..'
        index = progression.index('..')
        if index != 0:
            correct_answer = progression[index - 1] + num
        else:
            correct_answer = progression[index + 1] - num
        print('Question: ', end='')
        print(*progression, sep=' ')
        answer = prompt.string('Your answer: ')
        get_result(answer, correct_answer, name)
        if str(answer) != str(correct_answer):
            break
        counter += 1
    if counter == 3:
        print(f"Congratulations, {name}!")


def is_prime():
    """Prime game code."""
    name = welcome_user()
    counter = 0
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    for _ in range(3):
        num = random.randint(2, 1001)
        for i in range(3, num):
            if num % i == 0:
                correct_answer = 'no'
                break
            else:
                correct_answer = 'yes'
        print(f'Question: {num}')
        answer = prompt.string('Your answer: ')
        get_result(answer, correct_answer, name)
        if str(answer) != str(correct_answer):
            break
        counter += 1
    if counter == 3:
        print(f"Congratulations, {name}!")
