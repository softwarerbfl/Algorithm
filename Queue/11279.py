import sys
import heapq
n=int(sys.stdin.readline())
array=[]
for i in range(n):
    x=int(sys.stdin.readline())
    if x==0 and len(array)>0:
        p=heapq.heappop(array)
        print(-p) #거꾸로 정렬되는 것을 노리기 위해 음수로 저장
    elif x==0 and len(array)==0:
        print(0)
    else:
        heapq.heappush(array,-x)