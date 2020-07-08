#https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem
n = int(input())
s = set(map(int, input().split()))
for i in range(int(input())) :
    commands = input().split()
    cmd = commands[0]
    args = commands[1:]
    if len(commands) == 1 :
        cmd += '(' + ')'
        eval('s.'+cmd)
    else :
        cmd += '(' + ','.join(args) + ')'
        eval('s.'+cmd)
print(sum(s))
