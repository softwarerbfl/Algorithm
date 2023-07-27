import sys
from collections import deque
dx=[-1,1,0,0,0,0]
dy=[0,0,1,-1,0,0]
dz=[0,0,0,0,1,-1]
# 여러 개의 테스트 케이스 입력받기
while True:
    # 층, 행, 열
    l, r, c = map(int, sys.stdin.readline().split())
    if l==0 and r==0 and c==0:
        break
    graph = [] # 지도
    visited=[] # 방문 여부
    # 가로, 세로, 높이
    sx, sy, sz = 0, 0, 0
    ex, ey, ez = 0, 0, 0
    # 시작 지점과 도착 지점의 좌표 얻기
    for i in range(l):
        g = []
        for j in range(r):
            line = list(input())
            g.append(line)
            if 'S' in line:
                idx=line.index('S')
                sx=idx
                sy=j
                sz=i
            if 'E' in line:
                idx = line.index('E')
                ex=idx
                ey=j
                ez=i

        graph.append(g)
        visited.append([[0]*c for _ in range(r)])
        input()
    q = deque()
    q.append([sx, sy, sz])
    visited[sz][sy][sx]=1 # 시작 지점 방문 처리
    answer=0 # 몇 번안에 도착할 수 있는지
    flag=0
    while q:
        answer+=1
        q_len=len(q)
        for i in range(q_len):
            x, y, z = q.popleft()
            for j in range(6):
                Z=z+dz[j]
                X=x+dx[j]
                Y=y+dy[j]
                # 주어진 영역 밖인 경우
                if Z<0 or X<0 or Y<0 or Z>l-1 or X>c-1 or Y>r-1:
                    continue
                # 길이 금으로 막혀 있는 경우
                if graph[Z][Y][X]=='#':
                    continue
                # 이미 방문했던 경험이 있는 경우
                if visited[Z][Y][X]==1:
                    continue
                q.append([X,Y,Z])
                visited[Z][Y][X]=1 # 방문 처리
                # 도착 지점에 도달한 경우
                if Z==ez and Y==ey and X==ex:
                    flag=1
                    print("Escaped in",answer, "minute(s).")
                    break
    # 도착지점에 도달하는 방법이 없는 경우
    if flag==0:
        print("Trapped!")