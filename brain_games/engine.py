from random import randint

ROUNDS_COUNT = 3


# def generate_number():
#     """Return random number from range."""
#     return randint(1, 100)
#
#
# def check_answer(user_answer, correct_answer):
#     """Check users answer."""
#     if user_answer == correct_answer:
#         message = 'Correct!'
#         return (True, message)
#     message = "'{wrong}' is wrong answer ;(. Correct answer was '{correct}'."
#     return (False, message.format(wrong=user_answer, correct=correct_answer))
#
#
# def welcome_user():
#     """Ask user for a name and print greeting."""
#     user_name = get_user_name()
#     greeting = f'Hello, {user_name}!'
#     print(greeting)
#     return user_name
#
#
# def run(game=None):
#     """Run game."""
#     print('Welcome to the Brain Games!')
#     if game:
#         print(game.DESCRIPTION)
#     print()
#     user_name = welcome_user()
#     if game:
#         print()
#         engine(user_name, game.make_question)


def engine(game):
    """Game process."""
    name = string('May I have your name? ')
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
                  f"Let's try again, {name}!")
            break
    print(f'Congratulations, {name}!')
