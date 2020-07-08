#https://www.hackerearth.com/practice/basic-programming/operators/basics-of-operators/practice-problems/algorithm/going-to-office-e2ef3feb/submissions/
#d is the distance from home to office
d = int(input())

# Oc is the cost for first Of km
#Od is for every km afterwards
Oc,Of,Od = list(map(int,input().split()))

#Cs is speed/min
#Cb is the base fare
#Cm is the cost of every min spent in taxi
#Cd is the cost of each kilometer u ride
Cs,Cb,Cm,Cd= list(map(int,input().split()))

#for online taxi, total cost is
o_cost = Oc + (d-Of)*Od

#for classic taxi total cost is
c_cost = Cb + (d//Cs)*Cm + (Cd * d)

if o_cost > c_cost :
    print('Classic Taxi')
else :
    print('Online Taxi')
