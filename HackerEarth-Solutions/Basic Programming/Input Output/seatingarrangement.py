#https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/seating-arrangement-1/
# t denotes number of test cases
t = int(input())
mydict = {

6:[1,'WS'],5:[3,'MS'],4:[5,'AS'],3:[7,'AS'],2:[9,'MS'],1:[11,'WS'],
0:[-11,'WS'],11:[-9,'MS'],10:[-7,'AS'],9:[-5,'AS'],8:[-3,'MS'],7:[-1,'WS']

        }
for _ in range(0,t) :
    # n denotes the seat number
    n = int(input())
    # total number of seats is 108
    if n <= 108 :
        # seat_no = n + mydict[n%12][0]
        print(n + mydict[n%12][0] ,mydict[n%12][1])
