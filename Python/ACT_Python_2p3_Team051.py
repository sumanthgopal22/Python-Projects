K1 = float(input('Enter a spring constant 1: '))
K2 = float(input('Enter a spring constant 2: '))
Ft = float(input('Enter a total force: '))
config = input('Enter P (Parallel) or S (Series): ')
import math
if K1 < 0:
    K1 = float(input('Enter a spring constant 1: '))
elif K2 < 0:
    K2 = float(input('Enter a spring constant 2: '))

if config == 'S': #Series
    Keq = 1 / ((1/K1) + (1/K2))
    F1 = Ft
    F2 = Ft
    x1 = F1/K1
    x2 = F2/K2
    Xt = x1 + x2

    print('Keq = {0:0.1f} \n'.format(Keq))
    print('F1 = {0:0.1f} \n'.format(F1))
    print('F2 = {0:0.1f} \n'.format(F2))
    print('X1 = {0:0.2f} \n'.format(x1))
    print('X2 = {0:0.2f} \n'.format(x2))
    print('Xt = {0:0.2f} \n'.format(Xt))

elif config == 'P': #Parallel
    Keq = K1 + K2
    F1 = K1 * x1
    F2 = K2 * x2
    Ft = F1 + F2
    x1 = Xt
    x2 = Xt

    print('Keq = {0:0.1f} \n'.format(Keq))
    print('F1 = {0:0.1f} \n'.format(F1))
    print('F2 = {0:0.1f} \n'.format(F2))
    print('X1 = {0:0.1f} \n'.format(x1))
    print('X2 = {0:0.1f} \n'.format(x2))
    print('Xt = {0:0.1f} \n'.format(Xt))
