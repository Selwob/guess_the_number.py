#! python3
# guess_the_number.py - A simple number guessing game against the computer.

import random
import sys


def play_again():
    print('Would you like to play again? y or n: ')
    again = input()
    if again.lower() == 'y':
        start_game()
    elif again.lower() == 'n':
        sys.exit()
    else:
        play_again()


def start_game():
    print('I am thinking of a number between 1 and 20. You have 5 guesses. Good Luck!')

    secret_number = random.randint(1, 20)
    guesses_left = 5

    while guesses_left > 0:
        guess = None

        while True:
            try:
                guess = int(input('Please enter an integer: '))
            except ValueError:
                continue
            else:
                break

        if guess == secret_number:
            print('Congratulations, you guessed that the secret number was %s!' % str(secret_number))
            play_again()

        elif guess > secret_number:
            print('Too high, try again.')
            guesses_left -= 1
            print('You have %s guesses left.' % guesses_left)

        elif guess < secret_number:
            print('Too low, try again.')
            guesses_left -= 1
            print('You have %s guesses left.' % guesses_left)

    print('Sorry, you lose. The secret number was %s.' % secret_number)
    play_again()

start_game()
