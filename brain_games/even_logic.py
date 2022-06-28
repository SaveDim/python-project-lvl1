"""Add brain_even game."""


import random
import prompt


def even_game():
    """Even game code and greeting."""
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if number is even, otherwise answer "no".')
    for _ in range(3):
        question = random.randint(1, 101)
        if question % 2 == 0:
            correct_answer = 'yes'
        else:
            correct_answer = 'no'
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')
        if (answer == 'yes' and question % 2 == 0) or (answer == 'no' and question % 2 != 0):
            print('Correct!')
        elif answer != correct_answer:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            return print(f"Let's try again, {name}!")
    print(f"Congratulations, {name}!")

