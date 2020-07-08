#https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/array-sum-2-725368ac/
n = int(input()) 
l = list(map(int,input().split()))
# mysum = 0
# for i in range(n) :
#     mysum += l[i]
# print(mysum)
print(sum(l))
