#https://www.hackerrank.com/challenges/30-binary-numbers/problem
#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    n = max(bin(n)[2:].split('0'))
    print(n.count('1'))
