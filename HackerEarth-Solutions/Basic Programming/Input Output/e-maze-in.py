#https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/e-maze-in-1aa4e2ac/
mystr = input()
#inital coordinate
x,y = 0,0
for i in mystr:
    if i == 'L' :
        x = x - 1
    elif i == 'R' :
        x = x + 1
    elif  i == 'D' :
        y = y - 1 
    else :
        y = y + 1

print(x,y)
