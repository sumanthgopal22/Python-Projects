# Activity Python: Exam
# File: E3_P25_gopalsh
# Date: 12/07/2022
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
import math

q = float(input('Enter a constant (q): '))
r = float(input('Enter a constant (r): '))
d = (q**2) + (4 * r)

if d >= 0:
    if abs(q + math.sqrt(d)/2) < 1 and abs(q - math.sqrt(d)/2) < 1:
        print('The sequence will converge')
elif d < 0:
    if abs(r) < 1:
        print('The sequence will converge')
else:
    print('Will not converge')

terms = int(input('Enter the number of terms: '))


if terms > 0:
    y0 = 2
    yneg1 = 1
    for k in range(terms):
        yn = q * (y0) + r * (yneg1)
        y0 = yn
        yneg1 = y0
elif terms <= 0:
    while terms <= 0:
        terms = int(input('Enter the number of terms: '))

round(yn, 3)
print(yn)















