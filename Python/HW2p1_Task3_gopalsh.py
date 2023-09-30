# Activity Python:
# File: HW2p1_Task3_gopalsh.py
# Date: Jan 24, 2023
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


R = [[100, 200], [810, 560], [470, 360]]
rSeries = []
rParallel = []

for row in R:
    rSeries.append(round(row[0] + row[1], 1))
    rParallel.append(round(((row[0] * row[1]) / (row[0] + row[1])), 1), )

for i in range(len(R)):
    print('R1=', R[i][0], ';', 'R2=', R[i][1], ';', 'R-series=', rSeries[i], ';', 'R-parallel=', rParallel[i])




