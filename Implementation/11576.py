import sys
a,b = map(int, sys.stdin.readline().split())
m=int(sys.stdin.readline())
arr=list(map(int, sys.stdin.readline().split()))
result=0
new_arr=[]
for i in range(len(arr)):
    result+=arr[i]*(a**(len(arr)-i-1))
k=0
while True:
    tmp=result%pow(b,k+1)
    result-=tmp # 빠진 값 차감
    tmp=tmp//pow(b,k)
    new_arr.append(tmp)
    if result==0:
        break
    k+=1
print(" ".join(map(str,new_arr[::-1])))