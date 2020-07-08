#https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/min-max-3/editorial/
n = int(input())
m = list(map(int,input().split()))
b = 0
for i in range(min(m),max(m)) :
    if i in m :
        b = 1
    else :
        b = 0
        break
print('YES') if b == 1 else print('NO')
