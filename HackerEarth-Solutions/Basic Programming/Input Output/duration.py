#https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/duration/
n = int(input())
for _ in range(n) :
    sh,sm,eh,em = list(map(int,input().split()))
    diff_h = eh - sh
    diff_m = em - sm
    if diff_m < 0 :
        diff_m = diff_m + 60
        diff_h = diff_h - 1
    print(diff_h,diff_m)            
