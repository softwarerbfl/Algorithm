import sys

n, d = map(int, sys.stdin.readline().split())
result=0
for i in range(1,n+1):
    num=i
    while True:
        if num == 0:
            break
        tmp = num % 10
        # 해당하는 값을 찾았을 경우
        if tmp == d:
            result += 1
        num = (num - tmp)/10
print(result)
