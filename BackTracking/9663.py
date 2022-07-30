import sys
n=int(sys.stdin.readline())
ans=0 #정답
row=[0]*n #체스판

#x번째 행에 놓인 퀸이 놓여질 수 있는지 확인하는 함수
def is_promising(x):
    for i in range(x):
        if row[x]==row[i] or abs(row[x]-row[i])==abs(x-i):
            return False
    return True

#x번째 행 전체에 말놓을 수 있는지 확인
def n_queens(x):
    global ans
    if x==n:
        ans+=1
        return
    else:
        for i in range(n):
            row[x]=i
            #만약 현재 퀸을 놓으려는 위치가 promising하면
            #다음 퀸을 놓기 위한 n_queens(i+1)을 호출
            if is_promising(x):
                n_queens(x+1)
n_queens(0)
print(ans)