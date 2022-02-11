t,m=input().split(" ")
t=int(t)
m=int(m)
if(m<45):
    if(t==0):
        print(23,m+15)
    else:
        print(t-1,m+15)
else:
    print(t,m-45)