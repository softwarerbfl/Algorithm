import sys
n=int(sys.stdin.readline())
tmp1=0
tmp2=1
if n==0:
    print(tmp1)
elif n==1:
    print(tmp2)
else:
    for i in range(2,n+1):
        tmp2,tmp1 = tmp2+tmp1,tmp2
    print(tmp2)
