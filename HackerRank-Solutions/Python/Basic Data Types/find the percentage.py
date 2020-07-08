#https://www.hackerrank.com/challenges/finding-the-percentage/problem
N = int(input())
mydict = {}
for _ in range(N) :
    inputs = input().split()
    name,scores = inputs[0],inputs[1:]
    scores = list(map(float,scores))
    mydict[name] = scores
query_name = input()
query_scores = mydict[query_name]
avg_score = sum(query_scores)/len(query_scores)
print('{0:.2f}'.format(avg_score)) 
