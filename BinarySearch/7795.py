import sys
t=int(sys.stdin.readline())

def eat(val, b):
    start = 0
    end = len(b)-1
    res=-1  # val보다 작은 수의 index
    while start <= end:
        mid = (start+end)//2
        if val>b[mid]:
            res=mid
            start=mid+1
        else:
            end=mid-1
    return res
for _ in range(t):
    n, m = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))
    b = sorted(list(map(int, sys.stdin.readline().split())))
    count=0
    for val in a:
        count+=eat(val, b)+1
    print(count)