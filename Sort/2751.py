import sys
N=int(sys.stdin.readline()) #수의 개수
l=[]
for i in range(N):
    l.append(int(sys.stdin.readline()))
l.sort()
for i in range(N):
    print(l[i])