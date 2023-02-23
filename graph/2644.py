import sys
n=int(sys.stdin.readline()) # 전체 사람
a,b = map(int, sys.stdin.readline().split()) # 촌수 계산해야 하는 사람의 번호
m=int(sys.stdin.readline()) # 부모 자식들 간의 관계의 개수
visited=[0]*(n+1)
people={i:[] for i in range(1,n+1)}
flag=0
for _ in range(m):
    x,y=map(int, sys.stdin.readline().split())
    people[x].append(y)
    people[y].append(x)

def dfs(num,result):
    global b
    global visited
    global people
    global flag

    if visited[num]==1:
        return
    if num==b:
        print(result)
        flag=1
    # 방문 처리
    visited[num]=1
    connect=people[num]
    for i in connect:
        if visited[i]==0:
            dfs(i,result+1)
dfs(a, 0)
# 촌수 계산을 할 수 없는 경우
if flag==0:
    print(-1)
