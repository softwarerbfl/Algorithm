from collections import deque
def solution(maps):
    answer=0
    n=len(maps)
    m=len(maps[0])

    # 위 아래 왼쪽 오른쪽
    dx=[0,0,-1,1]
    dy=[1,-1,0,0]

    q=deque()
    q.append([0,0])
    maps[0][0]=0 # 시작지점 방문 처리
    while q:
        answer += 1
        l=len(q)

        # 현재 지점에서 방문할 수 있는 노드들 모두 방문하기
        for _ in range(l):
            y, x = q.popleft()
            for j in range(4):
                nx=x+dx[j]
                ny=y+dy[j]
                # 주어진 영역 밖인 경우
                if nx<0 or nx>=m or ny<0 or ny>=n:
                    continue
                # 벽이거나 이미 방문처리한 경험이 있는 경우
                if maps[ny][nx]==0:
                    continue
                maps[ny][nx]=0 # 방문 처리
                q.append([ny,nx])
                # 도착 지점에 도달한 경우
                if ny==n-1 and nx==m-1:
                    return answer+1
    return -1
