arr=list(map(int,input().split(" ")))
a=list(map(int,str(arr[0])))
b=list(map(int,str(arr[1])))
result1=100*a[2]+10*a[1]+a[0]
result2=100*b[2]+10*b[1]+b[0]
if(result1>result2):
    print(result1)
else:
    print(result2)

