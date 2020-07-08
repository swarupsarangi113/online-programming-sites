#https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/ques-2/editorial/
_,x,y = map(int,input().split())
n = list(map(int,input().split()))
status = 'YES'
for i in n :
    if i >=x and i <= y :
        status = 'YES'
    else :
        status = 'NO'
        break
print(status)
