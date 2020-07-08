#https://www.hackerrank.com/challenges/find-angle/problem
from math import *
ab = int(input())
bc = int(input())
degree = chr(176)
print(round(degrees(atan2(ab,bc))),degree,sep='')
