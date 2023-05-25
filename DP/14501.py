import sys
n=int(sys.stdin.readline())
work=[]
ans=[0 for _ in range(n+1)]
for i in range(n):
    t, p = map(int, sys.stdin.readline().split())
    work.append([t,p])

for i in range(n-1,-1,-1):
    if i+work[i][0]>n:
        ans[i]=ans[i+1]
    else:
        ans[i]=max(ans[i+1], work[i][1]+ans[i+work[i][0]])

print(ans[0])