import sys
t=int(sys.stdin.readline())
value=[0 for _ in range(101)]
value[1]=1
value[2]=1
value[3]=1
value[4]=2
value[5]=2
value[6]=3
value[7]=4
value[8]=5
value[9]=7
value[10]=9
def p(x):
    if value[x]!=0:
        return value[x]
    else:
        value[x]= p(x-1)+p(x-5)
        return value[x]
for _ in range(t):
    n=int(sys.stdin.readline())
    p(n)
    print(value[n])