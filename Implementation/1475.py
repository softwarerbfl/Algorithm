import sys
import math
n=int(sys.stdin.readline())
num=[0]*9
divide=1000000
while divide>n:
    if divide>n:
        divide=divide//10

if divide==0:
    print(1)
else:
    while True:
        if divide == 0:
            break
        tmp = n // divide
        n = n % divide
        if tmp == 9:
            num[6] += 1
        else:
            num[tmp] += 1

        divide = divide // 10

    num[6] = math.ceil(num[6] / 2)
    print(max(num))