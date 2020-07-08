#https://www.hackerearth.com/practice/python/getting-started/numbers/practice-problems/algorithm/binary-sequence-dbaf9d61/description/
for _ in range(int(input())) :
    x,y,a,b = map(int,input().split())
    if x*y == a+b :
        print('Yes')
    else :
        print('No')
