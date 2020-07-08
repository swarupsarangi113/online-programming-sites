#https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/is-zoo-f6f309e7/
#enter a word 
word = input()
x = 0
y = 0
# maximum length of word must be 20
if len(word) <= 20 :
    for i in word:
        if i == 'z' :
            x = x + 1
        else :
            y = y + 1

if x == y/2 :
    print('Yes')
else :
    print('No')
