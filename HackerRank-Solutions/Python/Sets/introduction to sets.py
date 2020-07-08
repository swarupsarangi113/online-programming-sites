#https://www.hackerrank.com/challenges/py-introduction-to-sets/problem
def average(array):
    # your code goes here
    array = set(array)
    avg = sum(array)/len(array)
    return avg

