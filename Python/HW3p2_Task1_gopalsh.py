# Activity Python:
# File: HW3p2_Task1_gopalsh.py
# Date: Jan 31, 2023
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
# all your python files the rest of the semester

x = 0
vaporP = []
substances = []
temp = []
printState = ['Substance', 'T', 'P']
dataFile = open('Task1.txt', 'r')
dataRes = open('Task1_Results.txt', 'w')

data = dataFile.readlines()
dataRes.write('{0:19}\t {1:6}\t {2:10}\n'.format(printState[0], printState[1], printState[2]))
for k in range(len(data)):
    if k != 0:
        values = data[k].split()
        sub = values[0]
        subStore = sub
        A = float(values[1])
        B = float(values[2])
        C = float(values[3])
        Tmin = float(values[4])
        Tmax = float(values[5])
        T = float(values[6])
        # tString = str(T)
        tSub = T
        temp.append(T)
        substances.append(sub)
        # print(A)
        # print(B)
        # print(values)

        if Tmin <= T <= Tmax:
            x = A - (B / (C + T))
            n = pow(10, x)
            n = round(n, 2)
            n = float(n)
            nString = str(n)
            vaporP.append(nString)

        else:
            vaporP.append('-9999')

        if len(vaporP) > 24:
            for i in range(len(vaporP)):
                dataRes.write('{0:15}\t{1:9}\t{2:10}\n'.format(substances[i], temp[i], vaporP[i]))


dataFile.close()
dataRes.close()


