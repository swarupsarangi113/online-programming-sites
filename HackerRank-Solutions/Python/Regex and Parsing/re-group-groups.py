# https://www.hackerrank.com/challenges/re-group-groups/problem

import re

pattern = re.compile(r'([a-zA-Z0-9])\1+')
matches = pattern.findall(input())
print(matches[0] if matches else -1)
