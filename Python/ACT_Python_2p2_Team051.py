pH = float(input('Enter your pH of the solution'))
if 0 <= pH < 7:
    print('Acidic')
elif pH == 7:
    print('Neutral')
elif 7 < pH <= 14:
    print('Basic')
else:
    print('Invalid')
