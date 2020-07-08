#https://www.hackerrank.com/challenges/find-a-string/problem
def count_substring(string, sub_string):
    cnt = 0
    for i in range(0,len(string)) :
        tmp = string[i : i+len(sub_string)]
        if tmp == sub_string :
            cnt += 1

    return cnt

