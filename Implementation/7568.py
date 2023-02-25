import sys
import heapq
n=int(sys.stdin.readline())
score=[0]*n
people=[]
s=1 # 등수 계산
for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    people.append([x,y])

for i in people:
    rank=1
    for j in people:
        #자신보다 큰 것의 개수 구하기
        if i[0]<j[0] and i[1]<j[1]:
            rank+=1
    print(rank, end=" ")