from prompt import string
from brain_games.cli import get_user_name

ROUNDS_COUNT = 3


def engine(game):
    """Game common process."""
    name = get_user_name()
    question, correct_answer = game.get_round()
    print(f'Hello, {name}!')
    print(f'{game.DESCRIPTION}')
    for _ in range(ROUNDS_COUNT):
        print(f'Question: {question}')
        answer = string('Your answer:  ')
        if answer == correct_answer:
            print('Correct!')
            question, correct_answer = game.get_round()
        else:
            print(f"'{answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'\n"
                f"Let's try again, {name}!",
                )
            return
    print(f'Congratulations, {name}!')
