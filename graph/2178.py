#bfs를 사용한 미로탐색
import sys
sys.setrecursionlimit(10000) #깊이 제한 10000으로 풀어줌
n, m=map(int, sys.stdin.readline().split(" "))
graph=[]
for i in range(n):
    graph.append(list(map(int, input())))

def bfs(a,b):
    global n,m
    x=a-1
    y=b-1
    if x<=0 or x>n or y<=0 or y>m:
        return 0
    #이동할 수 없는 칸이면 False 반환
    if graph[x][y]==0:
        return 0

bfs(n,m) #n,m까지 가는 가장 빠른 이동 횟수 return