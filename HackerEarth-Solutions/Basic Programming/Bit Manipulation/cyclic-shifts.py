#https://www.hackerearth.com/practice/basic-programming/bit-manipulation/basics-of-bit-manipulation/practice-problems/algorithm/lets-shift-2-36d90caa/editorial/
for _ in range(int(input())) :
    n,m,c = input().split()
    n = bin(int(n))[2:].zfill(16)
    res = ''
    m = int(m)
    if c == 'L' :
        res = n[m:] + n[:m]
    else :
        res = n[-m:] + n[:-m]

    print(int(res,2))
