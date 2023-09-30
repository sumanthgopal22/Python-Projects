# Activity Python:
# File: CFU
# Date: 1/26/2023
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

RC = open('RC.txt', 'r')
CFU = open('CFU3p2.txt', 'w')
Max = 0
data = RC.readlines()
tau = []
for i in range(len(data)):
    dataSplit = data[i].split()
    dataConv = float(dataSplit[1])
    dataConv2 = float(dataSplit[0])
    total = dataConv2 * dataConv
    tau.append(total)
    if total > Max:
        Max = total

print('Max:', Max)

RC.close()






