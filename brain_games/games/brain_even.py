#!/usr/bin/env python3
import random
# import prompt
# import brain_games.cli
from brain_games.scripts.brain_games import start_game


def main():
    brain_even()
    # name = brain_games.cli.welcome_user()
    # print('Answer "yes" if the number is even, otherwise answer "no".')
    # to_continue = True
    # while to_continue:
    #     to_continue = game(name)


# def game(name):
#     question = generate_question()
#     user_answer = prompt.string('Your answer: ')
#     if is_even(question):
#         correct_answer = 'yes'
#     else:
#         correct_answer = 'no'
#     if user_answer == correct_answer:
#         print('Correct!')
#         return False
#     else:
#         print(f"'{user_answer}' is wrong answer ;(. "
#               f"Correct answer was '{correct_answer}'.")
#         print(f"Let's try again, {name}")
#         return True


def brain_even():
    question_text = 'Answer "yes" if the number is even, otherwise answer "no".'
    start_game(generate_question, question_text)


def generate_question():
    question = random.randint(0, 100)
    # print(f'Question: {question}')
    correct_answer = 'no'
    if is_even(question):
        correct_answer = 'yes'
    return question, correct_answer


def is_even(number):
    return number % 2 == 0


if __name__ == '__main__':
    main()
