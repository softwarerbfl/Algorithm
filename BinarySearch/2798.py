import sys
n,m = map(int,sys.stdin.readline().split())
card=list(map(int,sys.stdin.readline().split(" ")))
min_dif=(card[0]+card[1]+card[2])-m

for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            sum=card[i]+card[j]+card[k]
            dif=sum-m
            if dif<=0 and abs(dif)<abs(min_dif):
                min_dif=dif
print(m+min_dif)