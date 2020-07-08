#https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/the-great-kian/submissions/
n = int(input())
a = list(map(int,input().split()))
print(sum(a[::3]),sum(a[1::3]),sum(a[2::3]))
