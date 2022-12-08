import sys
N,M=list(map(int,sys.stdin.readline().split()))

value=list(map(int,sys.stdin.readline().split()))
value.sort()
result=[]
def permut(new_val):
    if len(new_val)==M:
        result.append(new_val)
        print(' '.join(map(str,new_val)))
        return

    for i in range(0, N):
        if value[i] not in new_val:
            new_val.append(value[i])
            permut(new_val)
            new_val.pop()
permut([])
