#https://www.hackerrank.com/challenges/py-check-strict-superset/problem
#this is the superset
A = set(map(int,input().split()))
n = int(input())
for _ in range(n) :
    N = set(map(int,input().split()))
    if N.difference(A) == set() :
        ans = 'True'
    else :
        ans = 'False'
        break
print(ans)
