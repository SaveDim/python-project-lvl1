from brain_games.engine import *
import prompt


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