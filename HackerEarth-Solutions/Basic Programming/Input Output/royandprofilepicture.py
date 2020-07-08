#https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/roy-and-profile-picture/
# L is the length of the side of square
L = int(input())

# N is the number of photos 
N = int(input())
#An empty list to append the results and print it on screen 
output = []
for _ in range(N) :
    # dimensions represented by W and H
    W,H = list(map(int,input().strip().split()))
    if W < L or H < L :
            output.append('UPLOAD ANOTHER')
    else :
        if (W == L and H == L) or (W == H) :
            output.append('ACCEPTED')
        else :
            output.append('CROP IT')

for j in output :
    print(j)
