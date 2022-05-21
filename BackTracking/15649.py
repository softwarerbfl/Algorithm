import sys

n, m = map(int, sys.stdin.readline().split(" "))
def track(num):
    if num == m:
        print(" ".join(map(str, arr)))
        return
    for i in range(1, n + 1):
        if(visited[i]==False):
            visited[i]=True
            arr.append(i)
            track(num+1)
            visited[i]=False
            arr.pop()
arr = []
visited=[False]*(n+1) #0번 인덱스 안쓰기 위해서 n+1개
track(0)