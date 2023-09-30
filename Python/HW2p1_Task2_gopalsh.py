# Activity Python:
# File: HW2p1_Task2_gopalsh.py
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


substance = input("Select a substance, Methanol, Butane, or Octane: ")

if substance == "Methanol":
    A = 8.0724
    B = 1574.99
    C = 238.87
    tMin = -16
    tMax = 91
    changeT = (tMax - tMin) / 19
    listMeth = [tMin]
    vaporP = []
    for i in range(0, 20):
        y = tMin + (i * changeT)
        y = round(y, 3)
        listMeth.insert(i, y)

    for z in range(0, 20):
        x = A - (B / (C + listMeth[z]))
        n = pow(10, x)
        n = round(n, 3)
        vaporP.insert(z, n)

    for u in range(0, 20):
        print('Temperature:', listMeth[u], '(C);', 'Pressure:', vaporP[u], '(mmHg)')

elif substance == "Butane":
    A = 6.80896
    B = 935.86
    C = 238.73
    tMin = -78
    tMax = 19
    changeT = (tMax - tMin) / 19
    listBut = [tMin]
    vaporP = []
    for i in range(0, 20):
        y = tMin + (i * changeT)
        y = round(y, 3)
        listBut.insert(i, y)

    for z in range(0, 20):
        x = A - (B / (C + listBut[z]))
        n = pow(10, x)
        n = round(n, 3)
        vaporP.insert(z, n)

    for u in range(0, 20):
        print('Temperature:', listBut[u], '(C);', 'Pressure:', vaporP[u], '(mmHg)')

elif substance == "Octane":
    A = 6.9094
    B = 1349.82
    C = 209.385
    tMin = 19
    tMax = 152
    changeT = (tMax - tMin) / 19
    listOct = [tMin]
    vaporP = []
    for i in range(0, 20):
        y = tMin + (i * changeT)
        y = round(y, 3)
        listOct.insert(i, y)

    for z in range(0, 20):
        x = A - (B / (C + listOct[z]))
        n = pow(10, x)
        n = round(n, 3)
        vaporP.insert(z, n)

    for u in range(0, 20):
        print('Temperature:', listOct[u], '(C);', 'Pressure:', vaporP[u], '(mmHg)')

elif substance != "Methanol" or "Butane" or "Octane":
    while substance != "Methanol" or "Butane" or "Octane":
        substance = input("Select a substance, Methanol, Butane, or Octane: ")
        if substance == "Methanol" or "Butane" or "Octane":
            if substance == "Methanol":
                A = 8.0724
                B = 1574.99
                C = 238.87
                tMin = -16
                tMax = 91
                changeT = (tMax - tMin) / 19
                listMeth = [tMin]
                vaporP = []
                for i in range(0, 20):
                    y = tMin + (i * changeT)
                    y = round(y, 3)
                    listMeth.insert(i, y)

                for z in range(0, 20):
                    x = A - (B / (C + listMeth[z]))
                    n = pow(10, x)
                    n = round(n, 3)
                    vaporP.insert(z, n)

                for u in range(0, 20):
                    print('Temperature:', listMeth[u], '(C);', 'Pressure:', vaporP[u], '(mmHg)')
                break

            elif substance == "Butane":
                A = 6.80896
                B = 935.86
                C = 238.73
                tMin = -78
                tMax = 19
                changeT = (tMax - tMin) / 19
                listBut = [tMin]
                vaporP = []
                for i in range(0, 20):
                    y = tMin + (i * changeT)
                    y = round(y, 3)
                    listBut.insert(i, y)

                for z in range(0, 20):
                    x = A - (B / (C + listBut[z]))
                    n = pow(10, x)
                    n = round(n, 3)
                    vaporP.insert(z, n)

                for u in range(0, 20):
                    print('Temperature:', listBut[u], '(C);', 'Pressure:', vaporP[u], '(mmHg)')
                break

            elif substance == "Octane":
                A = 6.9094
                B = 1349.82
                C = 209.385
                tMin = 19
                tMax = 152
                changeT = (tMax - tMin) / 19
                listOct = [tMin]
                vaporP = []
                for i in range(0, 20):
                    y = tMin + (i * changeT)
                    y = round(y, 3)
                    listOct.insert(i, y)

                for z in range(0, 20):
                    x = A - (B / (C + listOct[z]))
                    n = pow(10, x)
                    n = round(n, 3)
                    vaporP.insert(z, n)

                for u in range(0, 20):
                    print('Temperature:', listOct[u], '(C);', 'Pressure:', vaporP[u], '(mmHg)')
                break

