#https://www.hackerrank.com/challenges/the-minion-game/problem
def minion_game(string):
    # your code goes here
    kevin,stuart,l = 0,0,len(string)
    for i in range(l) :
        if string[i] in 'AEIOU' :
            kevin += (l-i)
        else :
            stuart += (l-i)
    if kevin > stuart :
        print('Kevin',kevin)
    elif kevin < stuart :
        print('Stuart',stuart)
    else :
        print('Draw')

