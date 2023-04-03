import sys
from collections import deque

n=int(sys.stdin.readline())
a=list(map(int,sys.stdin.readline().split()))
count=0
q=deque()
q.append(0) # 0번인덱스에서 시작
visit=[0]*n
visit[0]=1 # 방문 처리
if n==1:
    print(0)
    exit()
while q:
    count+=1
    # 현재 이동 가능한 위치들 하나씩 꺼내기
    for _ in range(len(q)):
        tmp=q.popleft()
        # 점프 가능한 위치 하나씩 꺼내보기
        for j in range(1,a[tmp]+1):
            if tmp+j>n-1:
                continue
            # 이미 방문한 경우 넘기기
            if visit[tmp+j]==1:
                continue
            visit[tmp+j]=1 # 방문 처리
            q.append(tmp+j)
    if visit[n-1]==1:
        break
# 목적지에 방문하지 못한 경우
if visit[n-1]==0:
    print(-1)
    exit()


print(count)