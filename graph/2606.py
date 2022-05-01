import sys
from collections import deque
computer=int(sys.stdin.readline()) #컴퓨터 개수
connect=int(sys.stdin.readline()) #node 개수
if connect==0:
    print("{0}".format(0))
    exit()
node={}
#1번 컴퓨터와 연결되어있으면 1, 아니라면 0
visited=[0]*(computer+1)
ans=0
#각 컴퓨터에 연결된 컴퓨터 개수를 담을 node 2중 배열 선언
for j in range(computer):
    node[j+1]=deque()
for i in range(connect):
    c1,c2=map(int, sys.stdin.readline().split())
    node[c1].append(c2)
    node[c2].append(c1)
while node[1]:
    #1번 컴퓨터의 값을 왼쪽에서부터 하나씩 빼준다.
    tmp=node[1].popleft()
    if tmp!=1 and len(node[tmp])>0:
        #1번 컴퓨터에서 가져온 컴퓨터(node[tmp])의 값을 빼고 node[1]에 추가해준다.
        while node[tmp]:
            tmp2 = node[tmp].popleft()
            node[1].append(tmp2)
    #pop한 node[1] 가장 왼쪽 컴퓨터가 방문처리 안되어있다면 방문 처리
    if visited[tmp]==0:
        visited[tmp]=1
        ans+=1
if visited[1]==1:
    ans-=1
print(ans)