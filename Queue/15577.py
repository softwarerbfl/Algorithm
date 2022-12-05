import sys
import heapq
N=int(sys.stdin.readline())
# value=[]
# for _ in range(N):
#     value.append(int(sys.stdin.readline()))
# value.sort()
# avg=value[0]
# for i in range(1,N):
#     avg=(avg+value[i])/2
# print(avg)

heap=[]

for _ in range(N):
    heapq.heappush(heap,int(sys.stdin.readline()))
avg=heapq.heappop(heap)
for _ in range(N-1):
    avg=(avg+heapq.heappop(heap))/2
print(avg)