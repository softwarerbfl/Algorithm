import sys
t=int(sys.stdin.readline())
def check(val):
    start=0
    end=n-1
    while start<=end:
        mid=(start+end)//2
        if val<note1[mid]:
            end=mid-1
        elif val>note1[mid]:
            start=mid+1
        else:
            return 1
    return 0

for _ in range(t):
    n = int(sys.stdin.readline())
    note1 = sorted(list(map(int, sys.stdin.readline().split())))
    m = int(sys.stdin.readline())
    note2 = list(map(int, sys.stdin.readline().split()))

    for i in range(m):
        print(check(note2[i]))

