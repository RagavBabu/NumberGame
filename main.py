# coding=utf-8
# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import random


def main():
    print('This is a number game, guess the correct number between 1 and 100 to win ')
    x = random.randint(1, 101)
    while True:
        guess = input('Guess a number\n')
        if guess == x:
            print('Congratulations, You win')
            break
        else:
            if guess > x:
                print('Your guess is too high')
            else:
                print('Your guess is too low')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
