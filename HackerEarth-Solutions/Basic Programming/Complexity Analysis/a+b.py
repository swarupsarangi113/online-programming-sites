#https://www.hackerearth.com/practice/basic-programming/complexity-analysis/time-and-space-complexity/practice-problems/algorithm/a-b-4/
import sys
for _ in range(12) :
    try :
        a,b = input().split()
    except EOFError :
        sys.exit()
    print(int(a)+int(b))
