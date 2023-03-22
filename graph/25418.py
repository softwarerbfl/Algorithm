import sys
a, k =map(int, sys.stdin.readline().split())
cnt=0
while True:
    if a==k:
        print(cnt)
        break

    if k%2 == 0 and k >= a*2:
        k = int(k/2)
    else:
        k-=1
    cnt+=1
