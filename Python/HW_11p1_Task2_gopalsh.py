#Activity Python: HW
# File: HW_11p1_Task2_gopalsh.py
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


Vo = float(input('Enter Vo value (m/s): '))
K = float(input('Enter K value ((Kgm^2)/s): '))
m = float(input('Enter m value (Kg): '))

import math

Vo = (39.4 * Vo)**2

K = K * 15477.02
m = m * 0.07
Km = K/m

V = math.sqrt(Vo - Km)

print('V (in/s): ' + f'{V:.2f}' + ' in/s')
