#https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/find-factorial/
n = int(input())
fac = 1
if n >= 1 and n <= 10 :
    for i in range(1,n+1)[::-1] :
        fac = fac*i
    print(fac)
