import sys,heapq
inf=float('INF')

v,e=map(int,sys.stdin.readline().split())
start=int(sys.stdin.readline())
graph=[[] for _ in range(v+1)]
distance=[inf]*(v+1) #최단 길이를 담는 배열
distance[start]=0

for _ in range(e):
    s,e,l=map(int,sys.stdin.readline().split())
    graph[s].append((e,l))
q =[]
heapq.heappush(q,(0,start))
while q:
    d,now =heapq.heappop(q)
    for x in graph[now]:
        cost=d+x[1]
        if distance[x[0]]>cost:
            distance[x[0]]=cost
            heapq.heappush(q,(cost,x[0]))

for i in range(1,v+1):
    if distance[i]==inf:
        print('INF')
    else:
        print(distance[i])