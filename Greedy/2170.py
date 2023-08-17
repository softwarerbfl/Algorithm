# 그리디 - BOJ 2170 선 긋기
import sys
n=int(sys.stdin.readline())
draw = [] # 주어진 선
line = [] # 합쳐진 선
result = 0 # 선 길이의 합

for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    draw.append([x,y])
draw.sort()
line.append(draw[0])
cur=0 # 현재 라인 개수 - 1

for i in range(1,n):
    x, y= draw[i]
    if line[cur][0]<=x<=line[cur][1] and line[cur][1]<=y:
        line[cur][1]=y
    elif x>line[cur][1]:
        line.append([x,y])
        result += line[cur][1]-line[cur][0]
        cur += 1
result += line[cur][1]-line[cur][0]
print(result)
