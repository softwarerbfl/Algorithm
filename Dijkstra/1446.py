import sys,heapq,math
inf=math.inf
n,D=map(int,sys.stdin.readline().split())
graph=[[] for _ in range(D+1)]

for i in range(D):
    graph[i].append((i+1,1))
for _ in range(n):
    start,end,l =map(int,sys.stdin.readline().split())
    #도착지점이 고속도로보다 길면 graph에 추가하지 않는다.
    if end>D : continue
    graph[start].append((end,l))

#최단경로를 담는 배열
distance=[inf]*(D+1)
distance[0]=0
q=[]
heapq.heappush(q,(0,0))
while q:
    d,now=heapq.heappop(q)
    if distance[now]<d: continue

    for x in graph[now]:
        cost=d+x[1]
        #최단거리 발견시 update
        if distance[x[0]]>cost:
            distance[x[0]]=cost
            heapq.heappush(q,(cost,x[0]))
print(distance[D])