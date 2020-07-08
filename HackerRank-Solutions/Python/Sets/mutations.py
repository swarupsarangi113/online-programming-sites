#https://www.hackerrank.com/challenges/py-set-mutations/problem
n = int(input())
a = set(map(int,input().split()))
N = int(input())
for _ in range(N) :
    cmd,l = input().split()
    b = set(map(int,input().split()))
    cmd += '(' + 'b' + ')'
    eval('a.'+cmd)

print(sum(a))
