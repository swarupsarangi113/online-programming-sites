#https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/psychic-powers/submissions/
n = input()
if n.find('000000') == -1 and n.find('111111') == -1 :
    print('Good luck!')
else :
    print('Sorry, sorry!') 
# n = input()
# if '0'*6 in n or '1'*6 in n:
#     print('Sorry, sorry!')
# else :
#     print('Good luck!') 
