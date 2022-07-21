import sys
stack=[]
k=int(sys.stdin.readline())
for i in range(k):
    num=int(sys.stdin.readline())
    if num!=0:
        stack.append(num)
    else:
        stack.pop()
sum=0
for j in range(len(stack)):
    sum+=stack[j]
print(sum)