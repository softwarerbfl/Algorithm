import sys
n=int(sys.stdin.readline())
cost=[]
min_cost=[[0]*3 for _ in range(n)] # 각 위치까지의 최소 비용

for _ in range(n):
    r, g, b = map(int, sys.stdin.readline().split())
    cost.append([r,g,b])

min_cost[0][0]=cost[0][0]
min_cost[0][1]=cost[0][1]
min_cost[0][2]=cost[0][2]

for i in range(1,n):
    for j in range(3):
        if j==0:
            min_cost[i][j]=min(min_cost[i-1][1],min_cost[i-1][2])+cost[i][j]
        elif j==1:
            min_cost[i][j] = min(min_cost[i - 1][0], min_cost[i - 1][2]) + cost[i][j]
        else:
            min_cost[i][j] = min(min_cost[i - 1][1], min_cost[i - 1][0]) + cost[i][j]

print(min(min_cost[n-1]))