#Activity Python: HW
# File:Hw_13p1_Task1
# Date:11/23/2022
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

p = float(input('Enter Preasure: '))
t = float(input('Enter Temperature: '))

t = t+273.15
plog = math.log(t/273.15)
p1 = 0.006*math.exp(6293*((1/273.15) - 1/t)-0.56* plog)
p2 = 0.006*math.exp(6808*((1/273.15) - 1/t)-5.09*plog)

if t > 647.0 and p > 218.0:
    print('Super Critical Liquid')
if t < 273.15:
    
    if p > p1:
        
        print('Solid')
        
    else:
        print('Gas')

if p > p2:
    print('Liquid')
else:
    print('Gas')

   
