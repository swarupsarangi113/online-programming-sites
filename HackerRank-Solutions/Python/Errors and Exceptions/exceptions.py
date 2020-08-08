#https://www.hackerrank.com/challenges/exceptions/problem
t = int(input())
for _ in range(t) :
    try :
        a,b = map(int,input().split())
        print(a // b)
    except Exception as e :
        print('Error Code:',e) 
