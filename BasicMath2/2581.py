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

M=int(sys.stdin.readline()) #하한
N=int(sys.stdin.readline()) #상한

all=[]
for i in range(M,N+1):
    if is_prime(i)==True:
        all.append(i)
if len(all)==0:
    print(-1)
else:
    print(sum(all))
    print(min(all))