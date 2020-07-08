#https://www.hackerrank.com/challenges/nested-list/problem
N = int(input())
newlist = []
scorelist = []
for _ in range(N) :
    name = input()
    grade = float(input())
    newlist.append([name,grade])
    scorelist.append(grade)
second_low = sorted(set(scorelist))[1]
for name,grade in sorted(newlist) :
    if grade == second_low :
        print(name)
