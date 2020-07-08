#https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/split-house-547be0e9/
'''
QUESTION EXPLANATION :
No two houses(H) should be together, if yes then print NO
If no house(H) is together then replace (.)dot by (B) , and print YES with final array
'''
n = int(input())
village = list(input())

for i in range(n) :
    if village[i] == '.' :
        village[i] = 'B'
count = 0
for i in range(n-1) :
    if village[i] == 'H' :
        if village[i+1] == 'H' :
            count += 1

if count != 0 :
    print('NO')
else :
    print('YES')
    print(''.join(village))
