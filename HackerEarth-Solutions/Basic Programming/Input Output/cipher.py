#https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/cipher-1/
import string
S = input()
N = int(input())
s = ''
a = string.ascii_lowercase
A = string.ascii_uppercase
for i in S :
    b = a.find(i)
    B = A.find(i)
    if b != -1 :
        s = s + a[(b+N)%26]
    elif B!= -1 :
        s = s + A[(B+N)%26]
    elif i.isnumeric() :
        s = s + str((int(i)+N)%10)
    else :
        s = s + i
print(s)
