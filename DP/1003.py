import sys
t=int(sys.stdin.readline())
f=[[0,0] for _ in range(41)]
f[0]=[1,0]
f[1]=[0,1]
def fibo(num):
    global n
    if num==0 or num==1:
        return
    if f[num]!=[0,0]:
        return
    for i in range(2,num+1):
        f[i][0]=f[i-1][0]+f[i-2][0]
        f[i][1]=f[i-1][1]+f[i-2][1]

for _ in range(t):
    n=int(sys.stdin.readline())
    fibo(n)
    print(f[n][0], f[n][1])
