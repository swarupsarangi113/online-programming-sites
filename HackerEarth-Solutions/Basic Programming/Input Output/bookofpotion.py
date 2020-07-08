#https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/sum-it-if-you-can-4867f851/
n = input()
Sum= 0
for i in range(len(n)) :
    Sum = Sum + (i+1) * int(n[i])

if Sum % 11 == 0:
    print('Legal ISBN')
else :
    print('Illegal ISBN')
