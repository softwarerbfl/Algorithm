import sys
while True:
    b, n = map(int, sys.stdin.readline().split())
    if n==0 and b==0 :
        break
    min_dist=b
    num=1
    while num**n<=b:
        if abs(num**n-b)<min_dist:
            min_dist=abs(num**n-b)
            if (num+1)**n>b:
                break
        num+=1
    if (num+1)**n-b<min_dist:
        print(num+1)
    else:
        print(num)