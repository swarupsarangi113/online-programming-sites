#https://github.com/swarup113/HackerRank-Solutions/tree/master/Python/Sets
t = int(input())
for _ in range(t) :
    a,b = [set(input().split()) for _ in range(4)][1::2]
    if a.issubset(b) :
        print('True')
    else :
        print('False')
