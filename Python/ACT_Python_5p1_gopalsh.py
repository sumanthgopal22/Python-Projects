import random

numTimes = int(input('Input the number of times you want to roll the dice: '))
sumDice = []
count = 0

if numTimes < 0:
    while numTimes < 0:
        numTimes = int(input('Input the number of times you want to roll the dice: '))
        if numTimes >= 0:
            break
else:
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    for dice1 in range(numTimes):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        totalDie = dice1 + dice2
        sumDice.append(totalDie)
        if totalDie == 7:
            count = count + 1
        # count = sumDice.count(7)

    print(sumDice)
    print("Number of times 7 appears:", count)









