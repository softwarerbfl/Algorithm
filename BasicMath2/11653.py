import sys

N=int(sys.stdin.readline())
i=2
while N!=1:
    if N%i==0: #N이 i로 나누어지는 경우
        print(i)
        N=N/i
    else: #N이 i로 나누어지지 않는 경우
        i+=1