import sys
sys.setrecursionlimit(10000000)
n=int(sys.stdin.readline())
normal_area=0 # 정상인 사람이 본 구역의 수
abnormal_area=0 # 적록색약인 사람이 본 구역의 수
dx=[-1,1,0,0]
dy=[0,0,-1,1]
color=[]
for _ in range(n):
    l=list(input())
    color.append(l)
# 빨강, 초록은 1로, 파랑은 0으로 방문 처리
def dfs_r(y,x):
    global color
    if color[y][x]!='R':
        return
    color[y][x] = 1
    for c in range(4):
        X=x+dx[c]
        Y=y+dy[c]
        if X<0 or Y<0 or X>n-1 or Y>n-1:
            continue
        if color[Y][X]=='R':
            dfs_r(Y, X)

def dfs_g(y,x):
    global color
    if color[y][x]!='G':
        return
    color[y][x] = 1
    for c in range(4):
        X=x+dx[c]
        Y=y+dy[c]
        if X<0 or Y<0 or X>n-1 or Y>n-1:
            continue
        if color[Y][X] == 'G':
            dfs_g(Y, X)

def dfs_b(y,x):
    global color
    if color[y][x]!='B':
        return
    color[y][x] = 0
    for c in range(4):
        X=x+dx[c]
        Y=y+dy[c]
        if X<0 or Y<0 or X>n-1 or Y>n-1:
            continue
        if color[Y][X]=='B':
            dfs_b(Y, X)
# 현재 좌표와 방문한 곳의 색
def dfs_sick(y,x,c):
    # 이미 방문한 경우
    if color[y][x]==2:
        return
    color[y][x]=2 # 방문 처리
    for k in range(4):
        X=x+dx[k]
        Y=y+dy[k]
        if X<0 or Y<0 or X>n-1 or Y>n-1:
            continue
        if color[Y][X]==c:
            dfs_sick(Y,X,c)

for i in range(n):
    for j in range(n):
        if color[i][j]=='R':
            dfs_r(i,j)
            normal_area += 1
        elif color[i][j]=='G':
            dfs_g(i,j)
            normal_area += 1
        elif color[i][j]=='B':
            dfs_b(i,j)
            normal_area += 1

for i in range(n):
    for j in range(n):
        if color[i][j]!=2:
            dfs_sick(i,j,color[i][j])
            abnormal_area+=1
print(normal_area, abnormal_area)