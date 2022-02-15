#예외처리하는 while문
import sys
i=0
a=[]
while(True):
    try:
        a.append(list(map(int,sys.stdin.readline().split(" "))))
        i+=1
    except:
        break
for x in range(i):
    print(a[x][0]+a[x][1])