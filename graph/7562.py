import sys
from collections import deque
t=int(sys.stdin.readline())
# 나이트의 이동 가능한 경우의 수
dx=[1,2,1,2,-1,-2,-1,-2]
dy=[2,1,-2,-1,2,1,-2,-1]
def bfs(i,j):
    global cur_x, cur_y
    global goal_x, goal_y, count, graph

    stack=deque()
    graph[cur_x][cur_y]=1 # 방문처리
    stack.append([cur_x,cur_y])
    # 현재 위치가 목표 지점인 경우
    if cur_x==goal_x and cur_y==goal_y:
        return
    while True:
        count += 1
        len_s=len(stack)
        # 한 레벨에서 이동 가능한 곳 이동하기
        for _ in range(len_s):
            x, y=stack.popleft()
            for k in range(8):
                X = x + dx[k]
                Y = y + dy[k]
                if X < 0 or Y < 0 or X > l - 1 or Y > l - 1:
                    continue
                # 아직 방문하지 않은 곳인 경우에만 방문
                if graph[X][Y]==0:
                    graph[X][Y]=1 # 방문 처리
                    stack.append([X, Y])
        # 한 턴 다 돌고 원하는 위치 찾은 경우
        if [goal_x, goal_y] in stack:
            return


for _ in range(t):
    l=int(sys.stdin.readline())
    cur_x, cur_y=map(int, sys.stdin.readline().split())
    goal_x, goal_y=map(int, sys.stdin.readline().split())
    graph=[[0]*l for _ in range(l)]
    count=0
    bfs(cur_x,cur_y)
    print(count)