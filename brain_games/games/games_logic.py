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
        print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
        print(f"Let's try again, {name}!")


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
    """Calc game code!."""
    name = welcome_user()
    print('What is the result of the expression?')
    action_lst = ['+', '-', '*']
    counter = 0
    for _ in range(3):
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
        answer = prompt.string('Your answer: ')
        counter += 1
        get_result(answer, correct_answer, name)
        if str(answer) != str(correct_answer):
            break
    if counter == 3:
        print(f"Congratulations, {name}!")
calc_game()