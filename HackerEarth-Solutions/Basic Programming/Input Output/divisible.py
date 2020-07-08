#https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/divisibe-or-2d8e196a/
N = int(input())
A = input().split()
mysum = ''
for i in range(N//2) :
    mysum = mysum + A[i][0]
for j in range(N//2,N) :
    mysum = mysum + A[j][-1]
if int(mysum) % 11 == 0 :
    print('OUI')
else :
    print('NON')
