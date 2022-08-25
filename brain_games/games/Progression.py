from engine import *
import prompt
import random


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