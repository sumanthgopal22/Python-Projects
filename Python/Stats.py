# Activity Python:
# File: Stats.py
# Date: Jan 24, 2023
# By:      Sumanth Gopal
# Section: 002
# Team:    254
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
# all your python files the rest of the semester

def Stats(listNum):
    import math

    mean = 0
    total = 0
    std = 0

    for i in range(len(listNum)):
        total = total + listNum[i]
    mean = total / len(listNum)
    var = sum((x - mean) ** 2 for x in listNum) / len(listNum)  # How to find standard deviation#
    std = math.sqrt(var)

    print(listNum)
    print('Mean:', mean)
    print('Standard Deviation:', std)


listNum = []

numbers = 1
while numbers != 0:
    numbers = int(input('Enter a number from 1-100 to add to the list (Enter 0 to stop): '))
    listNum.append(numbers)
    if numbers == 0:
        listNum.remove(0)
        break

Stats(listNum)
