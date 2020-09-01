# https://www.hackerrank.com/challenges/introduction-to-regex/problem?isFullScreen=true

import re

for t in range(int(input())) :
    match = re.fullmatch(r'^[+-]?\.?[0-9]*\.[0-9]+$',input())
    if match :
        print('True')
    else :
        print('False')
