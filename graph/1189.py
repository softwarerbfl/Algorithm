import sys
import copy
r, c, k = map(int, sys.stdin.readline().split())
dx=[-1,1,0,0]
dy=[0,0,-1,1]

visited=[[0]*c for _ in range(r)]
area=[list(input()) for _ in range(r)] # 지역의 구조

cnt=0 # 정답
def dfs(y,x,visit,dist):
    global cnt
    global k

    # 정해진 횟수로 집에 정확히 도착한 경우
    if dist==k-1 and y==0 and x==c-1:
        cnt+=1
        return
    dist+=1
    v=copy.deepcopy(visit)
    # 이미 방문했거나 지정된 거리를 초과했거나 갈 수 없는 땅인 경우
    if v[y][x]==1 or dist>k or area[y][x]=='T':
        return
    v[y][x]=1 # 방문 처리
    for i in range(4):
        X=x+dx[i]
        Y=y+dy[i]

        # 영역을 벗어나는 경우+방문한 적 있는 경우+못가는 부분인 경우
        if X<0 or X>c-1 or Y<0 or Y>r-1 or v[Y][X]==1 or area[Y][X]=='T':
            continue
        dfs(Y,X,v,dist)
dfs(r-1,0,visited,0)
print(cnt)