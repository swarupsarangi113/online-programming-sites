#https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/rain-41f57695/submissions/
import math
t = int(input())
for _ in range(t) :
    l,r,s = list(map(int,input().split()))
    a,b = math.ceil(l/s),math.floor(r/s)
    if a*s in range(l,r+1) and b*s in range(l,r+1) :
        print(a,b)
    else :
        print(-1,-1)
