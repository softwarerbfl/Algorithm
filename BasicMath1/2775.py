import sys
T=int(sys.stdin.readline())
result=[]
def people(k,n):
    homepeople=0
    if k==0:
        return n
    elif k==1:
        return n*(n+1)/2
    else:
        for i in range(1, n + 1):
            homepeople = homepeople + people(k - 1, i)
        return homepeople

for _ in range(T):
    k=int(sys.stdin.readline())
    n=int(sys.stdin.readline())
    result.append(people(k,n))

for i in range(T):
    print(int(result[i]))