import sys
N=int(sys.stdin.readline())
Q=[]
for i in range(0,N):
    order=sys.stdin.readline().split()
    if order[0]=='push':
        Q.append(order[1])
    elif order[0]=='pop':
        if len(Q)==0:
            print('-1')
        else:
            print(Q[0])
            Q.pop(0)
    elif order[0]=='size':
        print(len(Q))
    elif order[0]=='empty':
        if len(Q)==0:
            print(1)
        else:
            print(0)
    elif order[0]=='front':
        if len(Q) == 0:
            print('-1')
        else:
            print(Q[0])
    else:
        if len(Q)==0:
            print('-1')
        else:
            print(Q[len(Q)-1])