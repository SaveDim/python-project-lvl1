from brain_games.engine import welcome_user, get_result
import prompt
import random


def is_prime():
    """Prime game code."""
    correct_answer = ''
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
