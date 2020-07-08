#https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/vc-pairs/
#t denotes the number of test cases
t = int(input())
vowels = ['a','e','i','o','u']
for _ in range(t) :
    n = int(input())
    #single string s with length n
    s = input()
    count = 0
    for i in range(len(s)-1) :
        if s[i] not in vowels and s[i+1] in vowels :
            count = count + 1
    print(count)
