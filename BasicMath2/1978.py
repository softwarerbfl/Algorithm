import sys

#소수 판별 함수
def is_prime(n):
    count=0
    for i in range(1,n+1):
        if n%i==0:
            count+=1
    if count==2:
        return True
    else:
        return False

N=int(sys.stdin.readline())
val=list(map(int,sys.stdin.readline().split()))
prime=0 #소수의 개수 카운팅
for i in range(N):
    if is_prime(val[i])==True:
        prime+=1
print(prime)