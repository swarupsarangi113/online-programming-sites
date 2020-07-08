#https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/bricks-game-5140869d/
# N is the no of bricks
N = int(input())
dict1 = {'p':1,'m':2}
i = 1
count = 0
while True :
    if count + (dict1['p']*i) >= N :
        print('Patlu') 
        break
    elif count + (dict1['p']*i) + (dict1['m']*i) >= N :
        print('Motu')
        break
    else :
        count = count + (dict1['p']*i) + (dict1['m']*i)
        i = i+1
