import sys
n, l = map(int,input().split())
taped, cnt = 0,0
for i in sorted(list(map(int,input().split()))):
    if i > taped:
        cnt += 1
        taped = i+l-1
print(cnt)