# Activity Python: Exam
# File: E4_P19_gopalsh.py
# Date: Feb 12 2023
# By:      Sumanth Gopal
# Section: 018
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


def Rocket(Vo, N):
    import math
    for i in range(N):
        angle = int(input('Enter a angle: '))
        if angle <= 0 or angle >= 90:
            while angle <= 0 or angle >= 90:
                angle = int(input('Enter a angle: '))
            if angle >= 0 or angle <= 90:
                break
        radians = angle * math.pi / 180
        maxH = (pow(Vo, 2)*pow(math.sin(radians), 2))/(2*9.81)
        maxH = round(maxH, 1)
        maxR = (2*(pow(Vo, 2))*math.cos(radians)*math.sin(radians))/9.81
        maxR = round(maxR, 1)
        print('Vo = {0:0}m/s\t Th = {1:0}deg\t MaxHeight = {2:0}m\t MaxRange = {3:1}m\t'.format(Vo, angle, maxH, maxR))


Rocket(10, 3)

