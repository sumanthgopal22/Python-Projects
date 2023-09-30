# ENED Python IO Example


# open file
data_file = open('Example_Data.txt', 'r')
data_results = open('Example_Results.txt', 'w')

# read in the data
data = data_file.readlines()

# process the data
for k in range(len(data)):
    if k != 0:
        values = data[k].split()
        measured = float(values[1])
        if measured > 24:
            data_results.write('{0}\t{1}\t High\n'.format(values[0], values[1]))
        elif measured < 21:
            data_results.write('{0}\t{1}\t Low\n'.format(values[0], values[1]))


# close the file
data_file.close()
data_results.close()
