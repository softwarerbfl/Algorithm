import sys
N=int(sys.stdin.readline())

def draw(n,idx):
    if n==1:
        stars[idx][idx] = '*'
        return
    l = 4*n-3

    for i in range(idx,l+idx):
        stars[idx][i]='*'
        stars[idx+l-1][i]='*'
        stars[i][idx]='*'
        stars[i][idx+l-1]='*'

    return draw(n-1,idx+2)

#좌표의 입력되어있는 값을 넣을 2차원 배열 선언
lens = 4*N -3
stars = [[' ']*lens for _ in range(lens) ]
draw(N,0)

#좌표 출력
for i in range(lens):
    for j in range(lens):
        print(stars[i][j],end="")
    print()