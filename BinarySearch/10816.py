import sys
n=int(sys.stdin.readline())
his_card=sorted(list(map(int,sys.stdin.readline().split())))
m=int(sys.stdin.readline())
check=list(map(int,sys.stdin.readline().split()))

def count(val):
    small=-1 # val보다 작은 값 중에 가장 큰 값의 인덱스
    big=n # val보다 큰 값중에 가장 작은 값의 인덱스

    #small을 구하는 과정
    start=0
    end=n-1
    while start<=end:
        mid=(start+end)//2
        if val<=his_card[mid]:
            end=mid-1
        elif val>his_card[mid]:
            start=mid+1
            small=mid
    #big을 구하는 과정
    start=0
    end=n-1
    while start<=end:
        mid=(start+end)//2
        if val<his_card[mid]:
            end=mid-1
            big=mid
        elif val>=his_card[mid]:
            start=mid+1
    return big-small-1

for value in check:
    print(count(value), end=" ")