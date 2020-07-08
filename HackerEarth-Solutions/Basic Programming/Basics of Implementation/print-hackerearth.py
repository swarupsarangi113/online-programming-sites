#https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/print-hackerearth/submissions/
_ = int(input())
mystr = input()
mydict = {}
for i in 'hackert' :
    mydict[i] = mystr.count(i)
for i in ('h','a','e','r') :
    mydict[i] = mydict[i]//2
print(min(mydict.values()))
