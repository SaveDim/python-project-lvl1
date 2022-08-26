from brain_games.engine import *
import prompt
import random


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