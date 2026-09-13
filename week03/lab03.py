"""Lab 03"""

import random


def generate_mad_lib(adjective: str, noun: str, verb: str) -> str:
    """Return a story containing the supplied words."""
    return f"The {adjective} {noun} {verb} across the field."


def guessing_game():
    """Run an interactive number-guessing game."""
    secret_number = random.randint(1, 100)

    while True:
        guess = int(input("Guess a number from 1 to 100: "))

        if guess < secret_number:
            print("Too low.")
        elif guess > secret_number:
            print("Too high.")
        else:
            print("Correct!")
            break
