import sys
from collections import deque

n=int(sys.stdin.readline())
queue=deque()
count=0
proc=[]

for i in range(n):
    orders=list(sys.stdin.readline().split())
    if orders[0]=='push':
        queue.append(int(orders[1]))
        count+=1
    elif orders[0]=='pop':
        if count<=0:
            proc.append(-1)
        else:
            proc.append(queue.popleft())
            count-=1
    elif orders[0]=='size':
        proc.append(count)
    elif orders[0]=='empty':
        if count<=0:
            proc.append(1)
        else:
            proc.append(0)
    elif orders[0]=='front':
        if count<=0:
            proc.append(-1)
        else:
            proc.append(queue[0])
    elif orders[0]=='back':
        if count<=0:
            proc.append(-1)
        else:
            proc.append(queue[count-1])

for i in range(len(proc)):
    print(proc[i])