# Activity Python:
# File: Alloy.py
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


def Alloy(an, np):
    al = 0
    cu = 0
    mg = 0
    mn = 0
    si = 0
    zn = 0

    if an == 2024:
        al = 0.935 * np
        cu = 0.044 * np
        mg = 0.015 * np
        mn = 0.006 * np
    if an == 7075:
        al = 0.903 * np
        cu = 0.016 * np
        mg = 0.025 * np
        zn = 0.056 * np
    if an == 356:
        al = 0.927 * np
        mg = 0.003 * np
        si = 0.07 * np

    print("Al:", 1.08 * al, "Cu:", 3.81 * cu, 'Mg:', 5.27 * mg, 'Mn:', 4 * mn, 'Si:', 5 * si, 'Zn:', 1.35 * zn)


Alloy(356, 3)
