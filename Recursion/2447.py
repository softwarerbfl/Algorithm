########해결 못함#######
import sys
N=int(sys.stdin.readline())
draw=[[1]*N for _ in range(N)]
def star(n,a,b):
    new_n = int(n / 3)
    if n==3:
        draw[3*a+1][3*b+1]=0
    else:
        for i in range(3):
            for j in range(3):
                # 중앙값이 아니면 재귀함수 호출
                if i % 3 != 1 and j % 3 != 1:
                    star(new_n, 3*a+i, 3*b+j)  # 재귀함수 호출
star(N*3,0,0)
for a in range(N):
    for b in range(N):
        if draw[a][b]==0:
            print(" ",end="")
        else:
            print("*",end="")
    print("")