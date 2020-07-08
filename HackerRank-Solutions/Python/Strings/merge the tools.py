#https://www.hackerrank.com/challenges/merge-the-tools/problem
import textwrap
def merge_the_tools(string, k):
    list1 = textwrap.wrap(string,k)
    for i in list1 :
        print(''.join(dict.fromkeys(i)))
