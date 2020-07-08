#https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/arithmetic-progression-1-81131fa7/
import math
t = int(input())
for _ in range(t) :
    a,b,c = list(map(int,input().split()))
    B = (a+c)/2
    deviation = abs(B - b)
    print(math.ceil(deviation))
