view = input('Input a specific Orthographic view (Front, Top or Right): ')
if view == 'Front':
    print('Dimensions are height and width')

elif view == 'Top':
    print('Dimensions are width and depth')

elif view == 'Right':
    print('Dimensions are depth and height')

else:
    print('The view chosen is not valid')
    view = input('Input a specific Orthographic view (Front, Top or Right): ')
