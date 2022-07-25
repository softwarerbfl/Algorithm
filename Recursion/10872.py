import sys
n=int(sys.stdin.readline())
def fac(n):
    if n>0:
        return fac(n-1)*n
    else:
        return 1
result=fac(n)
print(result)