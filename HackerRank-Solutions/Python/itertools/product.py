#https://www.hackerrank.com/challenges/itertools-product/problem?isFullScreen=true
# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
# prod = product(a,b)
# for p in prod : print(p,end = ' ')
print(*product(a, b))
