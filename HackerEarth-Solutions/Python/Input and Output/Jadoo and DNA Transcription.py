#https://www.hackerearth.com/practice/python/getting-started/input-and-output/practice-problems/golf/jadoo-and-dna-transcription/description/?layout=old
mydict = {'G':'C','C':'G','T':'A','A':'U'}
res = ''
for i in input() :
    if i in mydict :
        res += mydict[i]
    else :
        res = 'Invalid Input'
        break
print(res)

#other method
# s = input()
# a = 'GCTA'
# b = 'CGAU'
# try :
#     print(''.join([b[a.index(i)] for i in s]))
# except :
#     print('Invalid Input')
