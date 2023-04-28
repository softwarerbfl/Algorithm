import sys
x=int(sys.stdin.readline())
count=0
while x != 0:
    if x % 2 == 1:
        count += 1
    x = x // 2

print(count)