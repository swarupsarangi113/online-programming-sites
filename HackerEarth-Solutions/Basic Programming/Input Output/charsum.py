#https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/char-sum-2d3a6ab5/
mydict = {}
j = 1
for i in range(97,123) :
    mydict[chr(i)] = j
    j = j + 1
S = input()
Sum = 0
for i in S :
    Sum = Sum + mydict[i]
print(Sum)
