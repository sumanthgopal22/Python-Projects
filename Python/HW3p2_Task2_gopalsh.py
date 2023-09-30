dataFile = open('Task2.txt', 'r')
dataRes = open('Task2_Results.txt', 'w')
printState = ['Year', 'JanAvg', 'JulyAvg']
janArray = []
juneArray = []
yearsArray = []
averageJan = []
averageJul = []
year = 1949
average1 = 0
data = dataFile.readlines()


def addingTempJan(year_value):
    startV = 0
    endV = 31
    total_Temp = 0
    for y in range(len(yearsArray)):
        if yearsArray[y] == year_value:
            for p in range(startV, endV):
                total_Temp = janArray[p] + total_Temp
            total_Temp = total_Temp / 31
            total_Temp = round(total_Temp, 1)
            averageJan.append(total_Temp)
        startV = startV + 31
        endV = endV + 31


def addingTempJul(year_value):
    startV = 0
    endV = 31
    total_Temp = 0
    for y in range(len(yearsArray)):
        if yearsArray[y] == year_value:
            for p in range(startV, endV):
                total_Temp = juneArray[p] + total_Temp
            total_Temp = total_Temp / 31
            total_Temp = round(total_Temp, 1)
            averageJul.append(total_Temp)
        startV = startV + 31
        endV = endV + 31


for h in range(73):
    year = year + 1
    yearsArray.append(year)

for k in range(len(data)):
    if k != -1:
        values = data[k].split()
        years = int(values[0])
        jan = float(values[1])
        june = float(values[2])
        janArray.append(jan)
        juneArray.append(june)

year = 1949
for i in range(73):
    year = year + 1
    addingTempJan(year_value=year)
    addingTempJul(year_value=year)

dataRes.write('{0:2}\t{1:8}\t{2:12}\n'.format(printState[0], printState[1], printState[2]))

for i in range(73):
    dataRes.write('{0:1}\t{1:6}\t{2:10}\n'.format(yearsArray[i], averageJan[i], averageJul[i]))

dataFile.close()
dataRes.close()
