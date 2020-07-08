#https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/mojtaba-prepares-contest-29b2a044/
# no of test cases
t = int(input())

testcase = []
for i in range(t) :
        #cost of balloons
        cost = list(map(int,input().split()))
        # n denotes the no of participants
        n = int(input())
        price1 = 0
        price2 = 0
        status = []
        for _ in range(n) :
                # status of each participant, total n participants 
                status = list(map(int,input().split()))
                price1 = price1 +(cost[0]*status[0]) + (cost[1]*status[1])
                price2 = price2 +(cost[0]*status[1]) + (cost[1]*status[0])
        testcase.append(min(price1,price2))

for j in testcase:
        print(j)
