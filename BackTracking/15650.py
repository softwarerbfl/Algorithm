import sys
n,m=list(map(int,sys.stdin.readline().split()))
s=[]
#dep은 첫 번째로 들어갈 값
def back_track(n,m,dep):
    if len(s) == m:
        print(" ".join(map(str, s)))
        return
    for i in range(dep,n+1): #dep부터 n까지 돌면서 출력안한값 찾기
        if i not in s:
            s.append(i)
            back_track(n,m,dep+1)
            s.pop()
        dep+=1
back_track(n,m,1)