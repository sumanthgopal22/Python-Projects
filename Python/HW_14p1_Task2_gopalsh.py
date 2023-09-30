# Activity Python: HW
# File: HW_14p1_Task2_gopalsh
# Date: 12/3/2022
# By:      Sumanth Gopal
# Section: 004
# Team:    051
#
# ELECTRONIC SIGNATURE
# Sumanth Gopal
#
# The electronic signature above indicates the script
# submitted for evaluation is my individual work, and I
# have a general understanding of all aspects of its
# development and execution.
#
# A BRIEF DESCRIPTION OF WHAT THE SCRIPT OR FUNCTION DOES
# This script is a header template that will be used for
# all your python files the rest of the semester.


import random

p1 = 0
p2 = 0

while p1 < 50 or p2 < 50:
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)

    if p2 >= 50 > p1:
        print('Player 2 Wins!')
        print('Player 1 Final Score: ', p1)
        print('Player 2 Final Score: ', p2)
        break

    if p1 >= 50 > p2:
        print('Player 1 Wins!')
        print('Player 1 Final Score: ', p1)
        print('Player 2 Final Score: ', p2)
        break

    if dice1 == 5 or dice2 == 5:
        print('Player 1 Turn \n')
        print('Dice 1: ', dice1)
        print('Dice 2: ', dice2)
        print('Player 1: ', p1)
        print('\n')
        while p1 < 50 or p2 < 50:
            dice3 = random.randint(1, 6)
            dice4 = random.randint(1, 6)

            if dice3 == 5 or dice4 == 5:
                print('Player 2 Turn \n')
                print('Dice 1: ', dice3)
                print('Dice 2: ', dice4)
                print('Player 2: ', p2)
                print('\n')
                break
            elif dice3 != 5 or dice4 != 5:
                total1 = dice3 + dice4
                p2 = total1 + p2
                print('Player 2 Turn \n')
                print('Dice 1: ', dice3)
                print('Dice 2: ', dice4)
                print('Player 2: ', p2)
                print('\n')
            if p2 >= 50 > p1:
                break

    elif dice1 != 5 or dice2 != 5:
        total = dice1 + dice2
        p1 = total + p1
        print('Player 1 Turn \n')
        print('Dice 1: ', dice1)
        print('Dice 2: ', dice2)
        print('Player 1: ', p1)
        print('\n')




















