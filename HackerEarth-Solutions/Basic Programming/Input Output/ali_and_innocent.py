#https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/cartag-948c2b02/#c227482
mystr = list(input())
vowels = ['A','E','I','O','U','Y']
count = 0
for i in range(8) :
    if mystr[i].isnumeric() and mystr[i+1].isnumeric() :
        sum = int(mystr[i]) + int(mystr[i+1])
        if sum % 2 == 0 :
            count = count + 1

if count == 4 and mystr[2] not in vowels :
    print('valid')
else :
    print('invalid')
