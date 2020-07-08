#https://www.hackerrank.com/challenges/no-idea/problem
n,m  = input().split()
array = input().split()
a = set(input().split())
b = set(input().split())
hapiness = 0
for i in array :
    if i in a :
        hapiness += 1
    if i in b :
        hapiness -= 1
print(hapiness)
