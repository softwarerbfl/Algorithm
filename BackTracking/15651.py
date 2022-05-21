import sys

n, m = map(int, sys.stdin.readline().split(" "))
def track(num):
    if num == m:
        print(" ".join(map(str, arr)))
        return
    for i in range(1, n + 1):
        arr.append(i)
        track(num + 1)
        arr.pop()

arr = []
track(0)