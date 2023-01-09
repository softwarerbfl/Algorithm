import sys
import heapq
n=int(sys.stdin.readline())
array=[]
for i in range(n):
    x=int(sys.stdin.readline())
    if x == 0 and len(array) > 0:
        p=heapq.heappop(array)
        print(p)
    elif x==0 and len(array)==0:
        print(0)
    elif x != 0 :
        heapq.heappush(array, x)
