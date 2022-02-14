T=int(input())
a=[[0,0]]*T
for i in range(0,T):
    a[i]=input().split(" ")
for i in range(0,T):
    print(int(a[i][0])+int(a[i][1]))