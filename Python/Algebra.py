# Activity Python:
# File: Algebra.py
# Date: Jan 19 2023
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
# all your python files the rest of the semester.


def algebra(a1, b1, c1, a2, b2, c2):

    uniqueSol = (a1 * b2) - (a2 * b1)
    if uniqueSol == 0:
        print('There is no unique solution')
    else:
        x = ((c1 * b2) - (c2 * b1)) / uniqueSol
        y = ((a1 * c2) - (a2 * c1)) / uniqueSol
        x = round(x, 2)
        y = round(y, 2)
        print('X =', x)
        print('Y =', y)


algebra(2, 1, 5, 3, -1, 5)
# algebra(a1, b1, c1, a2, b2, c2)
