import sys
def func_sum(i,j,x,y):
    result=0
    for h in range(i-1,x):
        tmp=num_list[h]
        result+=sum(tmp[j-1:y])
    print(result)
n, m =map(int, sys.stdin.readline().split())
num_list=[]
for _ in range(n):
    l=list(map(int, sys.stdin.readline().split()))
    num_list.append(l)
k=int(sys.stdin.readline())
for _ in range(k):
    i,j,x,y=map(int, sys.stdin.readline().split())
    func_sum(i,j,x,y)