import sys
t=int(sys.stdin.readline())

for _ in range(t):
    a,b= map(int, sys.stdin.readline().split())
    while(True):
        if a==b:
            print(a*10)
            break
        elif a>b:
            a=int(a/2)
        else:
            b=int(b/2)
