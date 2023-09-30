# Activity Python: HW
# File: HW_14p1_Task1_gopalsh
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
d1 = int(input('Enter a digit: '))
d2 = int(input('Enter a digit: '))
d3 = int(input('Enter a digit: '))
d4 = int(input('Enter a digit: '))

noD = 0
oneD = 0
twoD = 0
threeD = 0
fourD = 0
for i in range(1000):
    overall = 0
    g1 = random.randint(0, 9)
    g2 = random.randint(0, 9)
    g3 = random.randint(0, 9)
    g4 = random.randint(0, 9)
    if g1 == d1:
        overall = overall + 1
    if g2 == d2:
        overall = overall + 1
    if g3 == d3:
        overall = overall + 1
    if g4 == d4:
        overall = overall + 1

    if overall == 0:
        noD = noD + 1
    elif overall == 1:
        oneD = oneD + 1
    elif overall == 2:
        twoD = twoD + 1
    elif overall == 3:
        threeD = threeD + 1
    else:
        fourD = fourD + 1

print('Number of tries with no digits found: ', noD)
print('Number of tries with one digit found: ', oneD)
print('Number of tries with two digits found: ', twoD)
print('Number of tries with three digits found: ', threeD)
print('Number of digits with four digits found: ', fourD)








