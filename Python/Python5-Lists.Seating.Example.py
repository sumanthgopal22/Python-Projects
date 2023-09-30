# ENED1120, Python Lists, In-Class Example


# define seating chart
Seating = [[40, 50, 50, 50, 40],
           [40, 50, 50, 50, 40],
           [30, 40, 40, 40, 30],
           [20, 30, 30, 30, 20],
           [10, 20, 20, 20, 10]]

Rows = ['A', 'B', 'C', 'D', 'E']

Repeat = 'Yes'

prompt = input('Would you like to search for a specific seat, or search for a range of seats under a certain amount? '
               'seat / price')
if prompt == 'seat':
    column = int(input('What column? '))
    row = int(input('What row? '))

    row_num = Rows.index(row)
    col_num = column - 1

    if Seating[row_num][col_num] == 0:
        print('Seat is taken!')
    else:
        print("Seat (row)(column) is (Seats[row_num][col_num])")
else:
    allowed_price = []
    allowed_seats = []
    price = int(input('What is the maximum price?'))

    for row in range(len(Seating)):
        for col in range(Seating[row]):
            if Seating[row][col] <= price:
                row_name = Rows[row] + str(col)
                allowed_seats.append(seat_name)
                allowed_price.append(Seating[row][col])

    for seat in range(len(allowed_seats)):
        print('{0} is $(1)'.format(allow seats[seats], allowed_prices[seat]))




