#!/usr/bin/env python3

# Created by: Matsuru Hoshi
# Created on: Sept 2019
# This is program adds numbers

import random


def main():
    # funciton makes user guess nimber

    # variable
    number = random.randint(1, 2)

    # Welcome statement
    print("Welcome, this is the NUMBER GUESSER.")
    input("Press Enter to continue.")

    # process
    while True:
        # input
        try:
            guess = int(input("\nGuess the number: "))
        except ValueError:
            print("Invalid input.")
            break
        if guess == number:
            # output
            print("Good job, you got it.")
            break
        else:
            print("you got it wrong.")


if __name__ == "__main__":
    main()
