# 1이 될 때까지
import sys
n, k = map(int, sys.stdin.readline().split())
count=0
# n이 1이 될 때까지 실행
while n!=1:
    if n%k==0: # 나눌 수 있으면 나누기
        n=n/k
    else:
        n=n-1 # 아니면 빼기
    count+=1
print(count)