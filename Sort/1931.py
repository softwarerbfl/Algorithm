import sys
import heapq
n=int(sys.stdin.readline())
time=[]

for i in range(n):
    start, end=map(int, sys.stdin.readline().split())
    time.append([start,end])
time.sort()

before_start=0
before_end=0
count=0 # 회의 개수
for i in range(n):
    if time[i][0]>=before_start and time[i][1]<before_end:
        before_start=time[i][0]
        before_end=time[i][1]

    elif time[i][0]>=before_end:
        before_end=time[i][1]
        before_start=time[i][0]
        count+=1
print(count)