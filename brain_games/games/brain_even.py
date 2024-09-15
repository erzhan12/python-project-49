#!/usr/bin/env python3
import random
from brain_games.scripts.brain_games import start_game


def main():
    brain_even()


def brain_even():
    question_text = 'Answer "yes" if the number is even, otherwise answer "no".'
    start_game(generate_question, question_text)


def generate_question():
    question = random.randint(0, 100)
    correct_answer = 'no'
    if is_even(question):
        correct_answer = 'yes'
    return question, correct_answer


def is_even(number):
    return number % 2 == 0


if __name__ == '__main__':
    main()
