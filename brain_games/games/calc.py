from brain_games.engine import *
import prompt


def calc_game():
    """Calc game code."""
    name = welcome_user()
    print('What is the result of the expression?')
    counter = 0
    for _ in range(3):
        correct_answer = get_correct_answer()
        answer = prompt.string('Your answer: ')
        get_result(answer, correct_answer, name)
        if str(answer) != str(correct_answer):
            break
        counter += 1
    if counter == 3:
        print(f"Congratulations, {name}!")
