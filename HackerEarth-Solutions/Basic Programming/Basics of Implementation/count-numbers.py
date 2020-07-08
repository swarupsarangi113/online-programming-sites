#https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/count-numbers-46/submissions/

for _ in range(int(input())) :
    n = int(input())
    num = ''
    numlist = []
    c = 0
    #we'll add a char 'p' in the end of the input string so that we can get the last number if it is present there ex : bh45yt72
    for i in (input() + 'p') :
        if i.isdigit() :
            num += i
        else:
            numlist.append(num)
            num = ''
    print(len([i for i in numlist if i.isdigit()]))      
