#!/usr/bin/env python3
import random
from brain_games.scripts.brain_games import start_game


def main():
    brain_progression()


def brain_progression():
    question_text = ('Answer "yes" if given number is prime. '
                     'Otherwise answer "no".')
    start_game(generate_question, question_text)


def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def generate_question():
    question = random.randint(0, 100)
    correct_answer = 'yes' if is_prime(question) else 'no'
    return question, correct_answer


if __name__ == '__main__':
    main()
