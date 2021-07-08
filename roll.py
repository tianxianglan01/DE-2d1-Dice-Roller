# roll a "die" some number of times.
# roll - run it once and go into a loop
# roll 1 - produce a number 1-6 random and print it
# roll 2 - produce two numbers 1-6 and print them
# roll 3 - produce three numbers and print them.
#

import random 

def roll_dice():
    while True:
        decision = int(input('Please choose\n1. Roll Dice\n2. Exit\n'))
        if decision == 2:
            break
        elif decision == 1:
            numDice = int(input(('Please enter the number of dice to roll\n')))
            for i in range(numDice):
                print('Dice Roll ' + str(i + 1) + ': ' + str(random.randint(1, 6)))
        else:
            print("That was not a correction selection. Please Try again\n")

roll_dice()


if __name__ == 'main':
    roll_dice()