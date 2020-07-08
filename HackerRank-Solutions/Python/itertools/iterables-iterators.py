#https://www.hackerrank.com/challenges/iterables-and-iterators/problem?isFullScreen=true
from itertools import combinations
n = int(input())
elements = [i for i in input().split()]
k = int(input())
total,c = 0,0
res = list(combinations(elements,k))
for element in res :
    if 'a' in element : c += 1

print('{0:3f}'.format(c/len(res)))