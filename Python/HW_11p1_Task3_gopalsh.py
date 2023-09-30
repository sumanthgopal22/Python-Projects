#Activity Python: HW
# File: HW_11p1_Task3_gopalsh.py
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


Ei = float(input('Enter the amplitude: '))
n1 = float(input('Enter intrinsic impedances 1: '))
n2 = float(input('Enter intrinsic impedances 2: '))
aI = float(input('Enter the angle of the incident wave (in Degrees): '))
aT = float(input('Enter the angle of the transmitted wave (in Degrees): '))

import math

aI = math.radians(aI)
aT = math.radians(aT)

Et = 2*(n2)
Et = Et * math.cos(aI)
Et2 = n2 * math.cos(aT)
Et2 = Et2 + (n1 * math.cos(aI))
Et3 = Et / Et2
Et = Et3 * Ei

Er = n2 * math.cos(aI)
Er = Er - (n1 * math.cos(aT))
Er2 = n2 * math.cos(aI)
Er2 = Er2 + (n1 * math.cos(aT))
Er = Er / Er2
Er = Er * Ei

print('The amplitude of the transmitted wave is Et = ' + f'{Et:.2f}' + ' V/m')
print('The amplitude of the reflected wave Er = ' + f'{Er:.2f}' + ' V/m')
