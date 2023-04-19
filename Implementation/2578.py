import sys
graph=[]
speak=[]
bingo=0
tmp=0
def find_s(num):
    global graph
    for y in range(5):
        for x in range(5):
            if graph[y][x]==num:
                return y,x
def check_x():
    global tmp
    tmp=0 # 대각선 빙고의 최종 개수
    count=0
    for a, b in [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4]]:
        if graph[a][b] == 0:
            count += 1
    if count == 5:
        tmp += 1
    count = 0
    for a, b in [[0, 4], [1, 3], [2, 2], [3, 1], [4, 0]]:
        if graph[a][b] == 0:
            count += 1
    if count == 5:
        tmp += 1
for _ in range(5):
    l=list(map(int, sys.stdin.readline().split()))
    graph.append(l)
for _ in range(5):
    l=list(map(int, sys.stdin.readline().split()))
    speak.extend(l)

for i in range(4):
    s=speak[i]
    # s의 위치를 찾는다.
    y,x=find_s(s)
    # 방문 처리
    graph[y][x] = 0

for i in range(4, 25):
    s = speak[i]
    y, x = find_s(s)
    graph[y][x] = 0 # 방문 처리
    # 세로 확인
    count = 0
    for h in range(5):
        if graph[y][h] == 0:
            count += 1
    # 빙고인 경우
    if count == 5:
        bingo += 1 # 빙고를 부르게 한 숫자의 인덱스 번호 출력
    # 가로 확인
    count = 0
    for w in range(5):
        if graph[w][x] == 0:
            count += 1
    # 빙고인 경우
    if count == 5:
        bingo += 1

    # 대각선에 존재하는 좌표인 경우
    if x == y or x+y == 4:
        check_x()
    # 빙고 갯수 확인
    if bingo+tmp >= 3:
        print(i+1)
        break
