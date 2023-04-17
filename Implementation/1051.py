import sys
n, m =map(int, sys.stdin.readline().split())
graph=[]
def find_rect(y,x):
    global min_size
    now=graph[y][x] # 현재 위치의 값
    size=1 # 현재 위치에서 만들 수 있는 사각형의 최대 넓이

    for b in range(x,m):
        if graph[y][b]==now:
            diff=b-x
            x1,y1=b,y+diff
            x2,y2=x,y+diff
            # 정사각형이 범위 밖에 생기는 경우
            if x1>m-1 or y1>n-1 or y2>n-1 or x2>m-1:
                continue
            # 정사각형이 만들어지는 경우
            if graph[y1][x1]==now and graph[y2][x2]==now:
                tmp=(diff+1)**2
                if tmp>size:
                    size=tmp
    # 이번에 구한 정사각형의 넓이가 최대인 경우
    if size>min_size:
        min_size=size


for _ in range(n):
    r=list(sys.stdin.readline())
    r=r[:m]
    r=list(map(int, r))
    graph.append(r)
min_size=1
for i in range(n):
    for j in range(m):
        if (m-j+1)**2<=min_size:
            continue
        find_rect(i,j)
print(min_size)