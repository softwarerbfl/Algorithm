import sys
import heapq
n=int(sys.stdin.readline())
w=[] # 각 로프들의 최대 중량
for _ in range(n):
    heapq.heappush(w,int(sys.stdin.readline()))

max_w=0 # 가능한 최대 중량
for i in range(n,0,-1):
    tmp=heapq.heappop(w)*i # i 개를 사용할 떄 수용 가능한 중량
    if tmp>max_w:
        max_w=tmp
print(max_w)