#https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/anagrams-651/
# t is the test cases
t = int(input())

for _ in range(t) :
    a = list(input())
    b = list(input())
    common= set(a).intersection(set(b))
    l = len(a) + len(b)
    d = 0
    for i in common :
    #for each common character, minimum no of occurrance in each string to find anagram length
        d = d + min(a.count(i),b.count(i))
    print(l - 2*d)
