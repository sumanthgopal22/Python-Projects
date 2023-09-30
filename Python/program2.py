R1 = float(input('Resistor 1 = '))
R2 = float(input('Resistor 2 = '))
Config = input('S(Series) or P(Paralell)')
if Config == 'S':
    Rt = R1 + R2
    print('RT = {0:0.1f} \n'.format(Rt)) //formatting//
elif Config == 'P':
    Rt = (R1 * R2)/(R1 + R2)
    print('RT = {0:0.1f} \n'.format(Rt))
else:
    print('Wrong Configuration')
