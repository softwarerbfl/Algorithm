import sys
n=int(sys.stdin.readline())
my=sorted(list(map(int, sys.stdin.readline().split())))
m=int(sys.stdin.readline())
check=list(map(int,sys.stdin.readline().split()))
def have(val):
    start=0
    end=len(my)-1

    while start<=end :
        mid = int((start + end) / 2)
        if my[mid] == val:
            return 1
        elif my[mid] < val:
            start = mid + 1
        elif my[mid]>val:
            end = mid -1
    return 0


for i in range(m):
    print(have(check[i]),end=" ")