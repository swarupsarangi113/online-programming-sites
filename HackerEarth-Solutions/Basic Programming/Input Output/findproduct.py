# https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/find-product/
# n denotes the size of the array
n = int(input())
answer = 1
# to print N space seperated integers denoting the elements of the array
list1 = list(map(int,input().strip().split()))
for i in range(n) :
    answer = (answer * list1[i]) % (1000000007)
print(answer) 
