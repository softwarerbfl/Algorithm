#bfs를 사용한 미로탐색
import sys
from collections import deque
dx=[0,0,-1,1]
dy=[1,-1,0,0]

n, m=map(int, sys.stdin.readline().split(" "))
graph=[]
for i in range(n):
    graph.append(list(map(int, input())))

move=deque()
move.append([0,0])
count=1
graph[0][0]=0
result=1
while True:
    result+=1
    tmp_count=count
    count=0 # 해당 칸수만큼 이동했을 때 노드 개수들
    for _ in range(tmp_count):
        y,x=move.popleft()

        for i in range(4):
            Y = y + dy[i]
            X = x + dx[i]
            # 영역 밖에 있거나 길이 없는 경우 스택에 넣지 않음
            if Y < 0 or X < 0 or X > m - 1 or Y > n - 1 or graph[Y][X] == 0:
                continue

            if Y == n - 1 and X == m - 1:
                print(result)
                exit()
            move.append([Y, X])
            graph[Y][X] = 0  # 방문처리
            count += 1  # 해당 칸수에서 노드 개수 증가