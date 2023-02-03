import sys
region=int(sys.stdin.readline())
request=sorted(list(map(int, sys.stdin.readline().split())))
total=int(sys.stdin.readline())

if sum(request)<=total:
    print(max(request))
else:
    start=0
    end=max(request)
    while start<=end:
        mid=(start+end)//2
        result = 0
        for i in request:
            result+=min(i,mid)
        if result > total: # 더한 값이 예산보다 큰 경우 -> 더한 값의 크기를 줄여야하므로 end를 땡겨옴
            end=mid-1
        else:
            start=mid+1 # 더한 값이 예산보다 작거나 같은 경우 -> 더 큰 값을 찾아봐도 됨
    print(end)

