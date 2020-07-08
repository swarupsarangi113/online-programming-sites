#https://www.hackerrank.com/challenges/python-lists/problem
n = int(input())
l = []
for _ in range(n) :
    commands = input().split()
    cmd  = commands[0]
    args = commands[1:]
    if cmd != 'print' :
        cmd = cmd + "(" + ','.join(args) + ")"
        eval('l.'+cmd)
    else :
        print(l)
