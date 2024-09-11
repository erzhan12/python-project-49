#!/usr/bin/env python3
import random
from brain_games.scripts.brain_games import start_game

progression_size = 10


def main():
    brain_progression()


def brain_progression():
    question_text = "What number is missing in the progression?"
    start_game(generate_question, question_text)


def make_progression(begin, step, secret_index):
    result = list()
    for i in range(0, progression_size):
        result.append(begin + step * i)
    secret_value = str(result[secret_index])
    result[secret_index] = '..'
    return ' '.join(map(str, result)), secret_value


def generate_question():
    begin = random.randint(0, 10)
    step = random.randint(1, 10)
    secret_index = random.randint(0, progression_size - 1)
    progression, correct_answer = make_progression(begin, step, secret_index)
    return progression, correct_answer


if __name__ == '__main__':
    main()
