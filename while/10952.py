import sys

i=0
a=[]
while(True):
    a.append(list(map(int,sys.stdin.readline().split(" "))))
    if(a[i][0]==a[i][1]==0):
        break
    i+=1
for x in range(i):
    print(a[x][0]+a[x][1])