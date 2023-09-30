dataFile = open('TempC.txt', 'r')
dataFileF = open('TempF.txt', 'w')

data = dataFile.readlines()

for i in range(len(data)):
    values = data[i].split()
    tempC = int(data[i])
    f = (tempC * (9/5)) + 32
    dataFileF.write('{0:.0f}\n'.format(f))


dataFile.close()
dataFileF.close()


