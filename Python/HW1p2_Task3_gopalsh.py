# Activity Python:
# File: HW1p2_Task3_gopalsh.py
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

import Alloy

an = int(input('Enter a valid Alloy number (2024, 7075, or 356): '))

if an == 2024 or an == 7075 or an == 356:
    np = float(input('Enter the number of pounds you would like: '))
    Alloy.Alloy(an, np)
else:
    while an != 2024 or an != 7075 or an != 356:
        an = int(input('Enter a valid Alloy number (2024, 7075, or 356): '))

        if an == 2024 or an == 7075 or an == 356:
            np = float(input('Enter the number of pounds you would like: '))
            Alloy.Alloy(an, np)
            break

