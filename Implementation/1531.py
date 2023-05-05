import sys
n, m = map(int, sys.stdin.readline().split())
graph=[[0]*100 for _ in range(100)]
count=0
for _ in range(n):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    for i in range(x1,x2+1):
        for j in range(y1,y2+1):
            graph[i-1][j-1]+=1
for i in range(100):
    for j in range(100):
        if graph[i][j]>m:
            count+=1
print(count)
