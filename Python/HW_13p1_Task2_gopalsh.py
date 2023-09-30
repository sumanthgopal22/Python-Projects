#Activity Python:HW
# File:Hw_13p1_Task2
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

metal = input('Enter the type of metal (Al, Co or Cr): ')
cs = input('Crystal structure (BCC, FCC or HCP): ')

if cs == 'FCC' and metal == 'Al':
    ma = 26.98 / 6.022e23
    cd = (ma * 4)/((4/math.sqrt(2) * 0.1431e-7)**3)
    cd = round(cd, 3)
    print('The calculated density of Al with FCC structure is ', cd)
    diff = (abs(2.7-cd)/2.7)*1
    if diff > 0.05:
        print('Inputed crystal may be incorrect')
    elif diff <= 0.05:
        print('The difference is <= 5%, thus FCC is the right crystal structure')

if cs == 'FCC' and metal == 'Co':
    ma = 58.93/ 6.022e23
    cd = (ma * 4)/((4/math.sqrt(2) * 0.1253e-7)**3)
    cd = round(cd,3)
    print('The calculated density of Co with FCC structure is ', cd)
    diff = (abs(8.9-cd)/8.9) * 1
    if diff > 0.05:
        print('Inputed crystal may be incorrect')
    elif diff <= 0.05:
        print('The difference is <= 5%, thus FCC is the right crystal structure')
        
if cs == 'FCC' and metal == 'Cr':
    ma = 52.00/ 6.022e23
    cd = (ma * 4)/((4/math.sqrt(2) * 0.1249e-7)**3)
    cd = round(cd,3)
    print('The calculated density of Al with FCC structure is ', cd)
    diff = (abs(2.7-cd)/2.7)*1
    if diff > 0.05:
        print('Inputed crystal may be incorrect')
    elif diff <= 0.05:
        print('The difference is <= 5%, thus FCC is the right crystal structure')

if cs == 'BCC' and metal == 'Al':
    ma = 26.98/ 6.022e23
    cd = (ma * 2)/((4/math.sqrt(3)*(0.1431e-7))**3)
    cd = round(cd,3)
    print('The calculated density of Al with BCC structure is ', cd)
    diff = (abs(2.7-cd)/2.7)*1
    if diff > 0.05:
        print('Inputed crystal may be incorrect')
    elif diff <= 0.05:
        print('The difference is <= 5%, thus BCC is the right crystal structure')

if cs == 'BCC' and metal == 'Co':
    ma = 58.93/ 6.022e23
    cd = (ma * 2)/((4/math.sqrt(3)*(0.1253e-7))**3)
    cd = round(cd,3)
    print('The calculated density of Co with BCC structure is ', cd)
    diff = (abs(8.9-cd)/8.9)*1
    if diff > 0.05:
        print('Inputed crystal may be incorrect')
    elif diff <= 0.05:
        print('The difference is <= 5%, thus BCC is the right crystal structure')

if cs == 'FCC' and metal == 'Cr':
    ma = 52.00/ 6.022e23
    cd = (ma * 2)/((4/math.sqrt(3)*(0.1249e-7))**3)
    cd = round(cd,3)
    print('The calculated density of Al with BCC structure is ', cd)
    diff = (abs(7.2-cd)/7.2)*1
    if diff > 0.05:
        print('Inputed crystal may be incorrect')
    elif diff <= 0.05:
        print('The difference is <= 5%, thus BCC is the right crystal structure')

if cs == 'HCP' and metal == 'Al':
    ma = 26.98/ 6.022e23
    a = 2*0.1431e-7
    c = 1.63 * a
    cd = (ma * 6)/((3*math.sqrt(3)* c * (a)**2)/2)
    cd = round(cd,3)
    print('The calculated density of Al with FCC structure is ', cd)
    diff = (abs(2.7-cd)/2.7)*1
    if diff > 0.05:
        print('Inputed crystal may be incorrect')
    elif diff <= 0.05:
        print('The difference is <= 5%, thus FCC is the right crystal structure')

if cs == 'HCP' and metal == 'Co':
    ma = 58.93/ 6.022e23
    a = 2*0.1253e-7
    c = 1.63 * a
    cd = (ma * 6)/((3*math.sqrt(3)* c * (a)**2)/2)
    cd = round(cd,3)
    print('The calculated density of Al with FCC structure is ', cd)
    diff = (abs(8.9-cd)/8.9)*1
    if diff > 0.05:
        print('Inputed crystal may be incorrect')
    elif diff <= 0.05:
        print('The difference is <= 5%, thus FCC is the right crystal structure')

if cs == 'HCP' and metal == 'Cr':
    ma = 52.00/ 6.022e23
    a = 2*0.1249e-7
    c = 1.63 * a
    cd = (ma * 6)/((3*math.sqrt(3)* c * (a)**2)/2)
    cd = round(cd,3)
    print('The calculated density of Al with FCC structure is ', cd)
    diff = (abs(7.2-cd)/7.2)*1
    if diff > 0.05:
        print('Inputed crystal may be incorrect')
    elif diff <= 0.05:
        print('The difference is <= 5%, thus FCC is the right crystal structure')
