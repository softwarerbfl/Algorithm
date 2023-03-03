import sys
n=int(sys.stdin.readline())
count=0
tmp=n//5
if n==1 or n==3:
    print(-1)
    exit()
# 5원 주고 남은 돈이 짝수인 경우
if (n%5)%2==0:
    count+=tmp # 5원 개수 더하기
    n=n%5
# 5월 주고 남은 돈이 홀수인 경우
else:
    count+=(tmp-1)
    n=(n%5)+5

tmp=n//2
count+=tmp # 2원 개수 더하기
print(count)