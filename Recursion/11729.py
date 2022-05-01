import sys
N=int(sys.stdin.readline())
def hanoi(n, a, b, c):
    if n == 1:
        print(a, c)
    else:
        hanoi(n - 1, a, c, b)
        print(a, c)
        hanoi(n - 1, b, a, c)
sum = 1
for i in range(N - 1):
    sum = sum * 2 + 1  #점화식
print(sum)
hanoi(N, 1, 2, 3)