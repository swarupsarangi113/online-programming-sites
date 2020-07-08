#https://www.hackerearth.com/practice/basic-programming/operators/basics-of-operators/practice-problems/algorithm/birthday-party-12/description/
t = int(input())
for _ in range(t) :
    n,m = list(map(int,input().split()))
    if m % n == 0 :
        print('Yes')
    else :
        print('No') 
