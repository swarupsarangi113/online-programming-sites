#https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/seven-segment-display-nov-easy-e7f87ce0/
t = int(input())
mydict  = {'0':6,'1':2,'2':5,'3':5,'4':4,'5':5,'6':6,'7':3,'8':7,'9':6}
for _ in range(t) :
    n = input()
    matches = 0
    for i in n:
        matches = matches + mydict[i]
    if matches % 2 == 0 :
        print('1'*(matches//2))
    else :
        print('7'+'1'*(matches//2-1))
