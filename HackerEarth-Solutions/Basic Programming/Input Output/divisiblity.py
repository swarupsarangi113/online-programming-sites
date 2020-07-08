#https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/divisible-or-not-81b86ad7/
N = int(input())
A = input().split()
last_digit = ''
for i in range(N) :
    last_digit = last_digit + A[i][-1]
if int(last_digit) % 10 == 0 :
    print('Yes')
else :
    print('No')
    
###TRICK###
# if last element of the list ends with zero, then it is divisble by 10
