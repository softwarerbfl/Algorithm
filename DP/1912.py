import sys
n = int(sys.stdin.readline())
a = list(map(int,sys.stdin.readline().split()))
sum = [a[0]]
for i in range(len(a) - 1):
    sum.append(max(sum[i] + a[i + 1], a[i + 1]))
print(max(sum))
