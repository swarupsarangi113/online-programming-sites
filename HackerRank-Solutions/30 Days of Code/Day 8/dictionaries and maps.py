#https://www.hackerrank.com/challenges/30-dictionaries-and-maps/problem
mydict = {}
for _ in range(int(input())) :
    name,n = input().split()
    mydict[name] = n
while True :
    try :
        name = input()
        if name in mydict :
            print(name+'='+mydict[name])
        else :
            print('Not found')
    except EOFError : break
