#https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/its-magic/
N = int(input())
list1 = list(map(int,input().split()))
output = []
sum_list=sum(list1)
for i in range(N) :
    if (sum_list - list1[i]) % 7 == 0 :
        output.append(list1[i])

if len(output) == 0 :
    print(-1)
else :
    min_number = min(output)
    print(list1.index(min_number))
