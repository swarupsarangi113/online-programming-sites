#https://www.hackerrank.com/challenges/capitalize/problem


# Complete the solve function below.
def solve(s) :
    s = list(s)
    s[0] = s[0].upper()
    for i in range(0,len(s)) :
        if s[i] == ' ' :
            s[i+1] = s[i+1].upper()
    
    s = ''.join(s)
    return s


