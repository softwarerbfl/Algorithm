# 상하좌우 - 시뮬레이션
import sys
n=int(sys.stdin.readline())
move = input().split()
# 오른쪽, 왼쪽, 위, 아래
instruct = ['R','L','U','D']
moving = [[0,1],[0,-1],[-1,0],[1,0]]
x, y = 1, 1 # 초기 좌표
for i in range(len(move)):
    idx = instruct.index(move[i]) # 현재 이동할 방향의 인덱스
    nx, ny = x+moving[idx][0], y+moving[idx][1] # 다음 이동할 좌표

    # 이동 범위 밖인 경우 무시
    if nx<=0 or ny<=0 or nx>n or ny>n:
        continue
    x= nx
    y= ny

print(x,y)