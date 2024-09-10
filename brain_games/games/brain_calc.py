#!/usr/bin/env python3
import random
from brain_games.scripts.brain_games import start_game


def main():
    brain_calc()


def brain_calc():
    question_text = "What is the result of the expression?"
    start_game(generate_question, question_text)


def eval_expression(number1, number2, operation):
    match operation:
        case '+':
            return number1 + number2
        case '-':
            return number1 - number2
        case '*':
            return number1 * number2
        # case _:


def generate_question():
    operations = ['+', '-', '*']
    num1 = random.randint(0, 100)
    num2 = random.randint(0, 100)
    operation_index = random.randint(0, 2)
    correct_answer = eval_expression(num1, num2, operations[operation_index])
    question = f"{num1} {operations[operation_index]} {num2}"
    return question, str(correct_answer)


if __name__ == '__main__':
    main()
