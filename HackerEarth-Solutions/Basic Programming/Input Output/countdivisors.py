#https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/count-divisors/
# it will contain 3 seperate integers l,r and k
myint = list(map(int,input().strip().split()))
count = 0
for i in range(myint[0],myint[1]+1) :
    if i % myint[2] == 0 :
        count = count + 1

print(count)
