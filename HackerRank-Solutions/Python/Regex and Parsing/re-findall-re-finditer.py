# https://www.hackerrank.com/challenges/re-findall-re-finditer/problem?isFullScreen=true

import re

pattern = re.compile(r'(?<=[^aeiouAEIOU])([aeiouAEIOU]{2,})[^aeiouAEIOU]')
matches = pattern.findall(input())

print('\n'.join(matches or ['-1']))
