#https://www.hackerrank.com/challenges/itertools-permutations/problem
from itertools import permutations
s,k = input().split()
res = permutations(sorted(s),int(k))
for i in (res) : print(''.join(i))
