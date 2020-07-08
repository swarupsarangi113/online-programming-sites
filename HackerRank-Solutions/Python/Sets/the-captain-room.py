#https://www.hackerrank.com/challenges/py-the-captains-room/problem
k = int(input())
room_list = list(map(int,input().split()))
diff = (sum(set(room_list))*k - sum(room_list))//(k-1)
print(diff)
