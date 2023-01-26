import sys
n,m = map(int, sys.stdin.readline().split())
lst, cnt = [], 0
for i in range(n):
    lst.append(sys.stdin.readline().rstrip())
for i in range(m):
    test = sys.stdin.readline().rstrip()
    for j in lst:
        if test == j[:len(test)]:
            cnt += 1
            break

print(cnt)
