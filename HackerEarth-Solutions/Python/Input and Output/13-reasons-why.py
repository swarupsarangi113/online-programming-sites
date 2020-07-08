#https://www.hackerearth.com/practice/python/getting-started/input-and-output/practice-problems/algorithm/its-easy-1/description/
a,b,c = map(int,input().split())
a,b = b,a
print(a * c,c + b)
