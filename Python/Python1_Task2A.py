import math
a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))
d = b**2 - 4*a*c
N1 = -b + math.sqrt(d)
N2 = -b - math.sqrt(d)
D = 2*a
r1 = N1/D
r2 = N2/D
print('Root 1 = {0}'.format(r1))
print('Root 2 = {0}'.format(r2))
