#https://www.hackerrank.com/challenges/itertools-combinations/problem
from itertools import combinations
s,k = input().split()
s = sorted(s)
for i in range(1,int(k)+1) :
    res = combinations(s,i)
    print(*[''.join(j) for j in res],sep = '\n')
