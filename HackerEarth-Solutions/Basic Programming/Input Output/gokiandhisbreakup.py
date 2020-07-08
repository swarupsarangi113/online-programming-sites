#https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/tds-and-his-breakup/
N = int(input())
X = int(input())
for _ in range(N) :
    Y = int(input())
    print('YES') if Y >= X else print('NO')
