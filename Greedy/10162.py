import sys
t=int(sys.stdin.readline())
button=[60*5,60,10]
result=[]
for i in range(3):
    result.append(t//button[i])
    t=t-button[i]*result[i]
if t!=0:
    print(-1)
else:
    print(" ".join(map(str,result)))