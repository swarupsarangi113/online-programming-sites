#https://www.hackerearth.com/practice/basic-programming/bit-manipulation/basics-of-bit-manipulation/practice-problems/algorithm/mystery-30/editorial/
'''
the output is the no of '1's in the binary representation on input
'''
from sys import stdin
while True :
    try :
        n = int(input())
        print(bin(n).count('1'))
    except EOFError :
        break
