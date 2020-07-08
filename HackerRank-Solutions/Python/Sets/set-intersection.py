#https://www.hackerrank.com/challenges/py-set-intersection-operation/problem
eng,fre = [set(input().split()) for _ in range(4)][1::2]
print(len(eng&fre))
