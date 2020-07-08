#https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/doctors-secret/
length,pages = list(map(int,input().split()))
if length <=23 and pages in range(500,1001) :
    print('Take Medicine')
else :
    print('Don\'t take Medicine')
