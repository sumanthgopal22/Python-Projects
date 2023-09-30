# Activity Python: Exam
# File:
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

dataFile = open('Robot.txt', 'r')
dataRes = open('E4_gopalsh.txt ', 'w')
data = dataFile.readlines()
xVal = []
yVal = []
for k in range(len(data)):
    if k != -1:
        values = data[k].split()
        x = float(values[0])
        y = float(values[1])
        xVal.append(x)
        yVal.append(y)
acceptX = 0
acceptY = 0
xIdeal = 19.3125
yIdeal = 59
for i in range(len(xVal)):
    xError = 0
    yError = 0
    if 19.5 >= xVal[i] >= 19.125:
        acceptX = acceptX + 1
        xError = xVal[i] - xIdeal
        round(xError, 2)
    if 58 <= yVal[i] <= 59:
        acceptY = acceptY + 1
        yError = yVal[i] - yIdeal
        round(yError, 2)

    dataRes.write('{0:2}\t{1:2}\n'.format(xError, yError))

total = acceptX + acceptY

print('Total x and y pos. = {0:1}\t x pos. = {1:2}\t y pos. = {2:1}\t '.format(total, acceptX, acceptY,))


dataFile.close()
dataRes.close()















