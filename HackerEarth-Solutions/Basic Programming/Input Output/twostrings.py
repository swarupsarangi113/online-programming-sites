#https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/two-strings-4/
t = int(input())
for _ in range(t) :
    s1,s2 = input().split()
    if sorted(list(s1)) == sorted(list(s2)) :
        print('YES')
    else :
        print('NO')
