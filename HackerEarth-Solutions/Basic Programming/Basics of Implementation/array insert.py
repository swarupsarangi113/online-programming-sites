#https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/array-insert/
#n is the array length, q is the no of queries
n,q = input().split()
# a is the array
a = list(map(int,input().split()))
for _ in range(int(q)) :
    v,x,y = list(map(int,input().split()))
    if v == 1 :
        a[x] = y
    elif v == 2 :
        if x <= len(a) and y <= len(a) :
            print(sum(a[x:y+1]))
        else :
            print(-1)
