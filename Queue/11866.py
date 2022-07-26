import sys
from collections import deque

n,k=map(int,sys.stdin.readline().split())

yosepus=deque()
count=n
pre=k-1 #이전에 삭제한 인덱스 번호
cur=k-1 #현재 삭제해야하는 인덱스 번호

#yosepus큐에 1~n까지의 값 넣어줌
for i in range(1,n+1):
    yosepus.append(i)
ans=[]
while True:
    ans.append(yosepus[cur])
    yosepus.remove(yosepus[cur])
    count-=1
    if count<=0:
        break
    pre=cur
    cur=(pre+(k-1))%count

print("<",end="")
print(ans[0],end="")
for i in range(1,n):
    print(f', {ans[i]}',end="")
print(">")