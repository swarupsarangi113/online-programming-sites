#https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/play-with-numbers-2/description/

from sys import stdin,stdout
n,q = map(int,stdin.readline().split())

N = [int(x) for x in input().split()]

for i in range(1,n) :
    N[i] += N[i-1]

for _ in range(q) :
    l,r = map(int,stdin.readline().split())    
    if l == 1 :
        mysum = N[r-1]
    else : 
        mysum = N[r-1] - N[l-2]
    print(mysum//(r-l+1))
