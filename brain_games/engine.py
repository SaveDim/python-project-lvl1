from random import randint

from brain_games.cli import get_user_answer, get_user_name

NUMBER_OF_ROUNDS = 3


def generate_number():
    """Return random number from range."""
    return randint(1, 100)


def check_answer(user_answer, correct_answer):
    """Check users answer."""
    if user_answer == correct_answer:
        message = 'Correct!'
        return (True, message)
    message = "'{wrong}' is wrong answer ;(. Correct answer was '{correct}'."
    return (False, message.format(wrong=user_answer, correct=correct_answer))


def welcome_user():
    """Ask user for a name and print greeting."""
    user_name = get_user_name()
    greeting = f'Hello, {user_name}!'
    print(greeting)
    return user_name


def run(game=None):
    """Run game."""
    print('Welcome to the Brain Games!')
    if game:
        print(game.DESCRIPTION)
    print()
    user_name = welcome_user()
    if game:
        print()
        engine(user_name, game.make_question)


def engine(user_name, play):
    """Game engine process."""
    correct_answers = 0
    while correct_answers < NUMBER_OF_ROUNDS:
        question, correct_answer = play()
        print(question)
        res, msg = check_answer(get_user_answer(), correct_answer)
        print(msg)
        if not res:
            print(f"Let's try again, {user_name}!")
            return
        correct_answers += 1
    print(f'Congratulations, {user_name}!')
