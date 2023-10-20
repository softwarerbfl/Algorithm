import sys
from collections import deque
t=int(sys.stdin.readline())
dy=[0,0,-1,1]
dx=[1,-1,0,0]
def bfs(person, fire):
    global graph
    move = 0 # 이동 횟수
    # 사람이 이동할 수 있는 공간이 있을 때까지 확인
    while person:
        move += 1
        ### 불이 퍼져나가는 공간부터 확인
        l = len(fire)
        for i in range(l):
            y, x = fire.popleft()
            graph[y][x] = '#'  # 현재 불 위치는 벽으로 바꾸어 줌
            for f in range(4):
                Y = y + dy[f]
                X = x + dx[f]
                # 영역 밖인 경우
                if X < 0 or Y < 0 or X > w - 1 or Y > h - 1:
                    continue
                # 벽이 아닌 경우에만 불로 바꾸어 줌
                if graph[Y][X] != '#':
                    graph[Y][X] = '*'
                    fire.append([Y, X])

        ### 사람이 이동할 수 있는 공간 확인
        l = len(person)
        for _ in range(l):
            y, x = person.popleft()
            for m in range(4):
                Y = y + dy[m]
                X = x + dx[m]
                # 밖으로 탈출한 경우
                if X < 0 or Y < 0 or Y > h - 1 or X > w - 1:
                    print(move)
                    return
                # 이동할 수 있는 공간인 경우 => 큐에 삽입
                if graph[Y][X] == '.':
                    graph[Y][X]='?' # 방문 처리...나름?나중에 다시 못들어오게 하기 위해서!
                    person.append([Y, X])
        # 더 이상 사람이 이동할 수 있는 경로가 없는 경우
        if len(person) == 0:
            print("IMPOSSIBLE")
            return

for _ in range(t):
    w, h = map(int, sys.stdin.readline().split())
    graph=[]
    person=deque() # 사람의 이동 좌표
    fire=deque() # 불의 좌표

    # 좌표 입력받기
    for i in range(h):
        g=list(input())
        graph.append(g)
        # 사람 위치가 입력되었다면 사람 큐에 넣어주기
        if '@' in g:

            person.append([i, g.index('@')])
        if '*' in g:
            if g.count('*')>=2:
                for j in range(w):
                    if g[j]=='*':
                        fire.append([i,j])
            else:
                fire.append([i,g.index('*')])
    bfs(person, fire)


