"""Add brain_calc game."""

import random
import prompt


def calc_game():
    """Calc game code and greeting."""
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('What is the result of the expression?')
    action_lst = ['+', '-', '*']
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
        if str(answer) == str(correct_answer):
            print('Correct!')
        elif str(answer) != str(correct_answer):
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            return print(f"Let's try again, {name}!")
    print(f"Congratulations, {name}!")
calc_game()
