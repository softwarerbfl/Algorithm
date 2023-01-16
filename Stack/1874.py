import sys
from collections import deque

n=int(sys.stdin.readline())
start= [] #1부터 n까지 push pop해줄 배열
result=[] #+인지 -인지 알려줄 배열
target= deque() #만들어야하는 수열
for i in range(n):
    target.append(int(sys.stdin.readline()))
i=1
start.append(i)
result.append('+')
while(True):
    if i>=n and len(start)==0:
        break
    if len(start)==0:
        i+=1
        start.append(i)
        result.append('+')
    if start[len(start)-1]==target[0]:
        start.pop()
        target.popleft()
        result.append('-')
    else:
        i+=1
        if i>n:
            break
        else:
            start.append(i)
            result.append('+')

if result.count('-')!=n:
    print("NO")
else:
    for i in range(len(result)):
        print(result[i])