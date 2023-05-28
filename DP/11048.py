import sys
n, m = map(int, sys.stdin.readline().split())
graph=[]
result=[[0 for _ in range(m)]for _ in range(n)]

for _ in range(n):
    g=list(map(int, sys.stdin.readline().split()))
    graph.append(g)

result[0][0]=graph[0][0]
# 첫 째줄 값 초기화
for x in range(1,m):
    result[0][x]=result[0][x-1]+graph[0][x]
# 다음 줄 부터 비교해가며 값 구하기
for i in range(1,n):
    for j in range(0,m):
        x1=i-1
        y1=j
        x2=i
        y2=j-1
        tmp1=0 # 위의 값
        tmp2=0 # 왼쪽 값
        if 0<=x1<=n-1 and 0<=y1<=m-1:
            tmp1=result[x1][y1]
        if 0 <= x2 <= n - 1 and 0 <= y2 <= m - 1:
            tmp2=result[x2][y2]
        result[i][j]=graph[i][j]+max(tmp1,tmp2)

print(result[n-1][m-1])