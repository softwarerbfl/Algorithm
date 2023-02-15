import sys
n=int(sys.stdin.readline())

neg=[]
pos=[]
zero=0

result=0
for _ in range(n):
    x=int(sys.stdin.readline())
    if x==1:
        result+=1
    elif x>0:
        pos.append(x)
    elif x<0:
        neg.append(x)
    else:
        zero+=1

neg.sort(reverse=True)
pos.sort()

if len(pos)%2==1:
    for i in range(len(pos)//2):
        a=pos.pop()
        b=pos.pop()

        result+=a*b
    result+=pos.pop()
else:
    for i in range(len(pos)//2):
        a = pos.pop()
        b = pos.pop()
        result += a * b
if len(neg)%2==1:
    for i in range(len(neg)//2):
        a=neg.pop()
        b=neg.pop()
        result+=a*b
    if zero==0:
        result+=neg.pop()
    else:
        result+=0
else:
    for i in range(len(neg)//2):
        a=neg.pop()
        b=neg.pop()
        result+=a*b

print(result)