import sys
n=int(sys.stdin.readline())
arr=list(map(int, sys.stdin.readline().split()))

if arr==sorted(arr):
    print(-1)
else:
    for i in range(n-1, 0, -1):
        if arr[i] < arr[i-1]:
            target=i-1 # 뒤에서부터 찾을 때 값이 앞>뒤인 것 찾기
            break

    for i in range(n-1,0,-1):
        if arr[i]<arr[target]:
            arr[i], arr[target]= arr[target], arr[i]
            break

    # target의 앞부분은 그대로 두고 그 뒤 부분은 가장 큰 값을 만들어야 하므로 reverse=True로 정렬
    arr=arr[:target+1]+sorted(arr[target+1:], reverse=True)
    print(" ".join(map(str,arr)))



