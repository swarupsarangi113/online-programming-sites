#https://www.hackerrank.com/challenges/30-review-loop/problem
t = int(input())
for _ in range(t) :
    s = input()
    odd_char = ''
    even_char = ''
    for i in range(len(s)) :
        if i % 2 == 0 :
            even_char += s[i]
        else :
            odd_char += s[i]
    print(even_char,odd_char)
