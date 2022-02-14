A,B,C=input().split(" ")
A=int(A)
B=int(B)
C=int(C)
if(A==B==C):
        print(10000+A*1000)
elif(((A==B)&(B!=C))|((A==C)&(A!=B))):
        print(A*100+1000)
elif((B==C)&(A!=B)):
    print(B*100+1000)
else:
    if((A>B) & (A>C)):
        print(A*100)
    elif((B>A) & (B>C)):
        print(B*100)
    else:
        print(C*100)
