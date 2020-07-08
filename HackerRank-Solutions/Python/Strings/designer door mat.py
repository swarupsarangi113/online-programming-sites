#https://www.hackerrank.com/challenges/designer-door-mat/problem
N,M = input().split()
N = int(N)
M = int(M)
for i in range(N) :
    l = N // 2
    if i < l :
        print('-'*3*(l-i),'.|.'*(2*i+1),'-'*3*(l-i),sep = '')
    elif i > l :
        print('-'*3*(i-l),'.|.'*(2*(2*l-i)+1),'-'*3*(i-l),sep = '')
    else :
        mystr = 'WELCOME'
        print('-'*((M - len(mystr))//2)+mystr+'-'*((M - len(mystr))//2),sep = '')
