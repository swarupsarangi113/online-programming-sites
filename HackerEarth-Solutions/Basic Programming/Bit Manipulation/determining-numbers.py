#https://www.hackerearth.com/practice/basic-programming/bit-manipulation/basics-of-bit-manipulation/practice-problems/algorithm/find-the-numbers-75f24949/submissions/
# n = int(input())
# a = [int(i) for i in input().split()]
# mydict = {}
# res = []
# for i in a :
#         mydict[i] = a.count(i)
# for key,value in mydict.items() :
#         if value == 1 :
#                 res.append(key)
# for key in sorted(res) :
#         print(key,end = ' ')

from collections import Counter
n = int(input())
a = [int(i) for i in input().split()]
counts = Counter(a)
res = []
for key,value in counts.items() :
        if value == 1 : 
                res.append(key)
for key in sorted(res) :
        print(key,end = ' ')
