import sys
from collections import deque
n=int(sys.stdin.readline())
info=0
q = deque()
while info!=-1:
    info = int(sys.stdin.readline())
    if info>0:
        if len(q)<n:
            q.append(info)
    elif info==0:
        q.popleft()
    else:
        break

if len(q)>0 :
    print(' '.join(map(str, q)))
else:
    print("empty")