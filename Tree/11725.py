import sys

n=int(sys.stdin.readline())
parent=[0]*(n)
parent[0]=-1
node=[]
for _ in range(n-1):
    a,b=map(int, sys.stdin.readline().split())
    node.append([a,b])
    if a==1:
        parent[b-1]=1
    elif b==1:
        parent[a-1]=1

for j in range(1,n):
    print(parent[j])
