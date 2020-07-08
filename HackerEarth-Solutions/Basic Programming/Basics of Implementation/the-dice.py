#https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/the-dice-d4dc5b11/submissions/
s = input()
c = 0
for i in s :
    if s[-1] == '6' :
        c = -1
        break
    elif i != '6' :
        c += 1
    else :
        continue
print(c)
