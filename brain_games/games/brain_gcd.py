#!/usr/bin/env python3
import random
from brain_games.scripts.brain_games import start_game


def main():
    brain_gcd()


def brain_gcd():
    question_text = "Find the greatest common divisor of given numbers."
    start_game(generate_question, question_text)


def calc_gcd(a, b):
    a, b = abs(a), abs(b)
    if a == 0 and b == 0:
        return None  # GCD undefined
    while b:
        a, b = b, a % b
    return a


def generate_question():
    num1 = random.randint(0, 100)
    num2 = random.randint(0, 100)
    correct_answer = calc_gcd(num1, num2)
    question = f"{num1} {num2}"
    return question, str(correct_answer)


if __name__ == '__main__':
    main()
