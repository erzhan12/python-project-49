#!/usr/bin/env python3
import brain_games.cli
import prompt


def start_game(generate_round_data, question_text, number_of_rounds=3):
    name = brain_games.cli.welcome_user()
    print(question_text)
    for _ in range(number_of_rounds):
        (question, correct_answer) = generate_round_data()
        print(f"Question: {question}")
        user_answer = prompt.string("Your answer: ")
        if user_answer != correct_answer:
            print(f"'{user_answer}' is wrong answer ;(."
                  f" Correct answer was '{correct_answer}'")
            print(f"Let's try again, {name}!")
            return
        print("Correct")
    print(f"Congratulations, {name}")
