#https://www.hackerearth.com/practice/basic-programming/bit-manipulation/basics-of-bit-manipulation/practice-problems/algorithm/subham-and-binary-strings/submissions/
'''
the total number of zeros in the string would be the total number of integers that would be even ( as every even integer has 0 as it's least significant bit )
'''
for _ in range(int(input())) :
    n = int(input())
    s = input()
    print(s.count('0'))
