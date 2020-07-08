#https://www.hackerrank.com/challenges/itertools-combinations-with-replacement/problem
from itertools import combinations_with_replacement

s,k = input().split()
res = combinations_with_replacement(sorted(s),int(k))
print(*[''.join(i) for i in res ],sep = '\n')
