#https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/print-the-numbers/
N = int(input())
list1 = list(map(int,input().split()))
for i in list1 :
    print(i,end = ' ')
