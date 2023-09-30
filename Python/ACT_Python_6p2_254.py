snowFile = open('Snow_Fall.txt', 'r')

data = snowFile.readlines()

snowVal = 0
for i in range(len(data)):
    #print(data[i])
    snowVal = data[i].split()
    #print(snowVal)
    snowF = float(data[1])
    print(snowF)

snowFile.close()
