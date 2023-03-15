import sys
n, m = map(int, sys.stdin.readline().split())
list1=[]
list2=[]

for _ in range(n):
    l=list(map(int, sys.stdin.readline().split()))
    list1.append(l)
m, k=map(int, sys.stdin.readline().split())
for _ in range(m):
    l = list(map(int, sys.stdin.readline().split()))
    list2.append(l)
result=[[0]*k for _ in range(n)]

for i in range(n):
    for j in range(k):
        for z in range(m):
            result[i][j]+=list1[i][z]*list2[z][j]
    print(" ".join(map(str,result[i])))
