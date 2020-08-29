# https://www.hackerrank.com/challenges/python-time-delta/problem?isFullScreen=true
#!/bin/python3

import math
import os
import random
import re
import sys
from datetime import datetime as dt

# Complete the time_delta function below.
def time_delta(t1, t2):
    for i in range(t) :
        t1 = dt.strptime(t1,'%a %d %b %Y %X %z')
        t2 = dt.strptime(t2,'%a %d %b %Y %X %z')
        td = t1 - t2
        return str(abs(int(td.total_seconds())))
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()
