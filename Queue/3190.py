import sys
N=int(sys.stdin.readline()) #보드의 크기
K=int(sys.stdin.readline()) #사과의 개수
AppleLocation=[list(map(int, input().split())) for _ in range(K)]
L=int(sys.stdin.readline())
direction=1 #1은 오른쪽, 2는 아래, 3은 왼쪽, 4는 위쪽 이런식!
now_location=[1,1] #머리 기준 좌표값
for i in range(L):
    locate=sys.stdin.readline().split()

if direction%4==1:
    now_location[1]+=int(locate[0])
elif direction%4==2:
    now_location[0]+=int(locate[0])
elif direction%4==3:
    now_location[1]-=int(locate[0])
else:
    now_location[0]-=int(locate[0])
if locate[1]=='D':
    direction+=1
else:
    direction-=1