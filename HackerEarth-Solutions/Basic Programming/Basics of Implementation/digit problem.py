#https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/digit-problem/#c229344
x, k = input().split()
x = list(x)
count = int(k)
for i in range(len(x)):
    if x[i] != '9' and count != 0 : 
        x[i] = '9'
        count -= 1
print(''.join(x))
