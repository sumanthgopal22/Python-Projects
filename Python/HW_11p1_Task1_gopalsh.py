# Activity Python: HW
# File: HW_11p1_Task1_gopalsh.py
# Date: 11/15/2022
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


c = float(input('Enter speed of light (m/s)'))
v = float(input('Enter speed of mobile (m/s)'))
m = float(input('Enter mass of mobile (Kg)'))


import math
gam = 1 - ((v/c)**2)
Gam = 1/(math.sqrt(gam))

p = m * v

q = m * v * Gam

print('Gam: ' + f'{Gam:.2e}')
print('p: ' + f'{p:.2e}' + ' m/s')
print('q: ' + f'{q:.2e}' + ' m/s')
