import sys
import heapq

n=int(sys.stdin.readline())
santa=[] #선물의 가치를 담을 heapq
visit=[]
for _ in range(n):
    place=list(map(int, sys.stdin.readline().split()))
    if len(place)==1 and place[0]==0: #아이들을 만났을 경우
        if len(santa)==0: #선물이 없는 경우
            print(-1)
        else: #선물이 있는 경우
            print(heapq.heappop(santa)*(-1))
    else: #선물 거점지일 경우
        for i in range(1,len(place)):
            heapq.heappush(santa,-place[i])
