import sys

N=int(sys.stdin.readline())
l=[]
for i in range(N):
    l.append(int(sys.stdin.readline()))

for i in range(N):
    for j in range(i,N):
        if l[i]>l[j]:
            l[i], l[j]=l[j],l[i]
    print(l[i])
