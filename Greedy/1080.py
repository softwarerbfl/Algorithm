import sys
n, m = map(int, sys.stdin.readline().split())
# 숫자를 빈칸없이 연속으로 입력받은 것을 따로따로 저장하고 싶은 경우에는 input()사용
a=[list(map(int, input())) for _ in range(n)]
b=[list(map(int, input())) for _ in range(n)]

# 행렬 뒤집는 메소드
def convert(q,w,arr):
    for x in range(q, q+3):
        for y in range(w,w+3):
            arr[x][y]=1-arr[x][y]
count=0
for i in range(n-2):
    for j in range(m-2):
        # 정답행렬과 다르면 3*3 행렬 값 변환
        if a[i][j]!=b[i][j]:
            convert(i,j,a)
            count+=1

for i in range(n):
    for j in range(m):
        if a[i][j] != b[i][j]:
            print(-1)
            exit()

print(count)

