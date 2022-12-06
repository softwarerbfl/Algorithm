import sys
n,m=list(map(int,sys.stdin.readline().split()))
s=[]
def back_track(n,m):
    if len(s) == m:
        print(" ".join(map(str, s)))
        return
    for i in range(1,n+1):
        s.append(i)
        back_track(n,m)
        s.pop()
back_track(n,m)