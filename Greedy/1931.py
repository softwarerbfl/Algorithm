# 그리디 - BOJ 1931 회의실 배정
import sys
n=int(sys.stdin.readline())
start_list=[]
end_list=[]
l_list=[]
count=1
for _ in range(n):
    start, end = map(int, sys.stdin.readline().split())
    l_list.append([end, start])

l_list.sort()
before_end=l_list[0][0] # 이전 회의 종료 시간

for i in range(1, n):
    # 이번 회의의 시작 시간이 이전 회의의 종료시간 이후인 경우
    if l_list[i][1]>=before_end :
        before_end=l_list[i][0]
        count+=1
    else:
        continue

print(count)