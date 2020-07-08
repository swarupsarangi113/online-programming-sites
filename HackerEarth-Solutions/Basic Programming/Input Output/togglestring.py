#https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/modify-the-string/
S = input()
newstr = ''
for i in S :
    if i.isupper() :
            newstr = newstr + i.lower()
    else :
            newstr = newstr + i.upper()
print(newstr)
