import random
import math

N = int(input('Enter the amount of times you want to flip a coin: '))
tails = int(0)
heads = int(0)
Ntot = N

while N > 0:
    flip = random.randint(0,1)
    N = N-1
    
    if flip == 0:
        tails = tails+1
        
    if flip == 1:
        heads = heads+1
    

#print('Heads: ' + heads)
#print('Tails: ' + tails)

print('Heads: ', (heads/Ntot)*100)
print('Tails: ', (tails/Ntot)*100)
        
