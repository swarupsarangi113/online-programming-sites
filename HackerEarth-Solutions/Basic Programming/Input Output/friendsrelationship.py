#https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/friends-relationship-1/
t = int(input())
for _ in range(t) :
    n = int(input())
    for i in range(1,n+1) :
        print((i)*'*',((n-i)*2)*'#',(i)*'*',sep = '')
