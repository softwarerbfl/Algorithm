N=int(input())
n=1
if(N==1):
    print(1)
else:
    while (True):
        if (3 * n * (n + 1) + 1 >= N):
            break
        n+=1
    print(n+1)