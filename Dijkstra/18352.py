import sys, heapq
import math
inf=math.inf


def dijkstra(x):
    q=[]
    heapq.heappush(q,(0,x))
    distance[x]=0
    while q:
        dist,now=heapq.heappop(q)
        if dist>distance[now]:
            continue
        for i in road[now]:
            cost=dist+i[1]
            if cost<distance[i[0]]:
                distance[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))

# n=도시 개수, m=도로 개수, k=최단거리, x=출발하는 도시
n,m,k,x= map(int, input().split())

road=[[] for _ in range(n+1)]
distance=[inf]*(n+1) #최단 경로를 담는 배열
for i in range(1,m+1):
    a,b=map(int,sys.stdin.readline().split(" "))
    road[a].append((b,1)) #a에서 b로 이동

dijkstra(x)

isNone=1
for i in range(1,n+1):
    if distance[i]==k:
        isNone=0
        print(i)
if isNone==1:
    print(-1)