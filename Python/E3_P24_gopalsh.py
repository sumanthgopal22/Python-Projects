# Activity Python: Exam
# File: E3_P24_gopalsh
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

model = input('Enter model type (Linear, Power, or Exponential): ')


if model == 'Linear' or 'linear':

    x1 = float(input('Enter x1: '))
    y1 = float(input('Enter y1: '))
    x2 = float(input('Enter x2: '))
    y2 = float(input('Enter y2: '))
    m = (y2 - y1) / (x2 - x1)
    b = y1 - (m * x1)
    m = round(m, 4)
    b = round(b, 4)
    print('y =', m, 'x +', b)

elif model == 'Power' or 'power':

    x1 = float(input('Enter x1: '))
    y1 = float(input('Enter y1: '))
    x2 = float(input('Enter x2: '))
    y2 = float(input('Enter y2: '))
    m = (math.log10(y2) - math.log10(y1)) / (math.log10(x2) - math.log10(x1))
    m = round(m, 4)
    b = 10 ** (math.log10(y2)) - (m * math.log10(x1))
    b = round(b, 4)
    print('y = ', b, 'x^', m)

elif model == 'Exponential' or 'exponential':

    x1 = float(input('Enter x1: '))
    y1 = float(input('Enter y1: '))
    x2 = float(input('Enter x2: '))
    y2 = float(input('Enter y2: '))

    m = (math.log(y2) - math.log(y1)) / (x2 - x1)
    m = round(m, 4)
    b = math.exp(math.log(y1) - (m * x1))
    b = round(b, 4)
    print('y = ', b, 'e^', m, 'x')

elif model != 'Linear' or model != 'Power' or model != 'Exponential':
    print('Model type invalid :(')






