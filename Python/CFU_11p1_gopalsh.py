#Activity Python: CFU
# File: CFU_11p1_gopalsh.py 
# Date:    31 Oct 2022
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



g = float(input('input the acceleration due to gravity (m/s^2):'))

O = float(input('input the angle in degrees:'))


R = float(input('input the range (m):'))

import math
O = math.radians(O)
V = (g *(R * (math.sin(O)**(2))))**(1/2)

print('Your velocity is {0:.2f} \n'.format(V))
