import sys
N=int(sys.stdin.readline())
transmitter= list(map(int,sys.stdin.readline().split(' ')))
receiving_set=[0]*N
for i in range(N-1,-1,-1):
    for j in range(i-1,-1,-1):
        if transmitter[j]>transmitter[i]:
            receiving_set[i]=j+1
            break
for i in range(N):
    print(receiving_set[i],end=' ')