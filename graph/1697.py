import sys
from collections import deque
n, k = map(int, sys.stdin.readline().split())
cnt=0
q=deque()
visited=[0]*100001
visited[n]=1 # 시작 지점 방문 처리
q.append(n)
if n==k:
    print(0)
    exit()
while q:
    cnt+=1
    for _ in range(len(q)):
        tmp = q.popleft()
        # -1 이동
        if 0 <= tmp - 1 <= 100000 and visited[tmp - 1] == 0:
            visited[tmp - 1] = 1  # 방문 처리
            q.append(tmp - 1)
        # +1 이동
        if 0 <= tmp + 1 <= 100000 and visited[tmp + 1] == 0:
            visited[tmp + 1] = 1  # 방문 처리
            q.append(tmp + 1)
        # *2 이동
        if 0 <= tmp * 2 <= 100000 and visited[tmp * 2] == 0:
            visited[tmp * 2] = 1  # 방문 처리
            q.append(tmp * 2)
    if visited[k]==1:
        print(cnt)
        break

