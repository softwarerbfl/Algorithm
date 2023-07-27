import sys
from collections import deque

f, s, g, u, d = map(int, sys.stdin.readline().split())
visited=[0]*(f+1) # 해당 층 방문 여부
q=deque()
q.append(s)
visited[s]=1 # 현재 위치 방문처리
button=0 # 버튼 클릭 수
if s==g:
    print(button)
    exit()
while q:
    q_len=len(q)
    button+=1
    for i in range(q_len):
        stair=q.popleft()
        up=stair+u
        down=stair-d
        # 해당 층으로 올라갈 수 있고 방문한 적이 없는 경우
        if 1<=up<=f and visited[up]!=1:
            q.append(up)
            visited[up]=1
        if 1<=down<=f and visited[down]!=1:
            q.append(down)
            visited[down]=1
    if g in q:
        print(button)
        exit()
print("use the stairs")

