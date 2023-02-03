import sys
n=int(sys.stdin.readline())
a=sorted(list(map(int,sys.stdin.readline().split())))
m=int(sys.stdin.readline())
b=list(map(int,sys.stdin.readline().split()))

def binary_search(v,l):
    first = 0
    end= len(l)-1
    while(first<=end):
        mid = int((first+end)/2)
        if v==l[mid]:
            print(1)
            return
        elif v>l[mid]:
            first=mid+1
        elif v<l[mid]:
            end=mid-1
    print(0)
    return
for i in range(m):
    binary_search(b[i],a)