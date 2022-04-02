import sys
N=int(sys.stdin.readline())
stack = [int(sys.stdin.readline()) for _ in range(N)]

for j in range(N-1,0,-1):
    if stack[j-1]<=stack[j]:
        stack.pop(j-1)
print(len(stack))