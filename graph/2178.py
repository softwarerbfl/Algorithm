import sys
sys.setrecursionlimit(10000) #깊이 제한 10000으로 풀어줌
def dfs(x,y):
    if x<=-1 or x>=n or y<=-1 or y>=m:
        return False
    if graph[x][y]==0:
        graph[x][y]=1
        dfs(x,y+1) #상
        dfs(x,y-1) #하
        dfs(x-1,y) #좌
        dfs(x+1,y) #우

        return True
    return False
n, m=map(int, input().split())
graph=[]
for i in range(n):
    graph.append(list(map(int, input())))

