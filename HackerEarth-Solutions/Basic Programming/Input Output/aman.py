#https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/aman-mrsharma/
d = int(input())
pie = 22/7
toffee = 0
for _ in range(d) :
    radius,amount = list(map(int,input().split()))
    if 2*pie*radius <= 100 * amount :
        toffee = toffee + 1
print(toffee)
