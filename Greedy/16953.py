import sys
a,b =map(int, sys.stdin.readline().split())
result=1
while True:
    if b%2==0:
        b=b//2
    else:
        # 일의 자리가 1인 경우
        if (b-1)%10==0:
            b=(b-1)//10
        else:
            if a!=b:
                result=-1
                break
    result += 1
    if a==b:
        break
    if b==0:
        result=-1
        break


print(result)