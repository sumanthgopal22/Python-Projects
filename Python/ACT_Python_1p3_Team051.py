#Activity Python 1: Task 3
# File: ACT_Python_HeaderTemplate_Team051_UCusername.py 
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


V = float(input('Enter fluid Velocity (mi/hr):'))
L = float(input('Enter typical length (in):'))
u = float(input('Enter dynamic viscosity (lb/(in*s):'))
p = float(input('Enter desnity of the fluid (lb/in**3):'))

import math          
V = V/2.237
L = L/39.37
u = u * 17.858
p = p * 27680         
Re = (p*V*L)/u

print('Re = {0:.2f} \n'.format(Re))


          
