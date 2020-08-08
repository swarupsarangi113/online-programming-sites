import re
for t in range(int(input())) :
    s = input()
    try :
        re.compile(s)
    except Exception as e :
        print('False')
    else :
        print('True')
