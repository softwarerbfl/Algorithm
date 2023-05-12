import sys
from collections import deque


n=int(sys.stdin.readline())

num=deque()
if n==1:
    print(0)
    exit()
if n%3==0:
    num.append(n//3)
if n%2==0:
    num.append(n//2)
num.append(n-1)
count=1
while True:
    if 1 in num:
        break
    l=len(num)
    for i in range(l):
        tmp=num.popleft()
        if tmp%3==0:
            num.append(tmp//3)
        if tmp%2==0:
            num.append(tmp//2)
        if tmp-1 not in num:
            num.append(tmp-1)
    count+=1
print(count)