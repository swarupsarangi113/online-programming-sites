#https://www.hackerrank.com/challenges/30-scope/problem?isFullScreen=true
class Difference:
    def __init__(self, a):
        self.__elements = a

    # Add your code here
    def computeDifference(self) :
        self.maximumDifference = abs(max(a) - min(a))

# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
