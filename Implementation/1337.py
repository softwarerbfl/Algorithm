import sys
n=int(sys.stdin.readline())
num=[]
for _ in range(n):
    x=int(sys.stdin.readline())
    num.append(x)

num.sort()
connect=1
max_connect=1
for i in range(0,n):
    up=num[i]+4
    down=num[i]
    connect=1
    for j in range(i,n):
        if down<num[j]<=up:
            connect+=1
    if connect>max_connect:
        max_connect=connect
print(5-max_connect)