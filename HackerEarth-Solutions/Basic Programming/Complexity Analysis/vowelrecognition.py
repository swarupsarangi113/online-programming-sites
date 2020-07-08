#https://www.hackerearth.com/practice/basic-programming/complexity-analysis/time-and-space-complexity/practice-problems/algorithm/vowel-game-f1a1047c/
from sys import stdin,stdout
v = 'aeiouAEIOU'
t = int(stdin.readline())

while (t):
    string = stdin.readline().strip()
    mysum = 0
    l = len(string)
    for i in range(l) :
        if string[i] in v :
            mysum += (i+1)*(l-i)
    stdout.write(str(mysum)+'\n')
    t -= 1
