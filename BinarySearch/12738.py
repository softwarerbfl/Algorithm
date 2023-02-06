import sys
from  bisect import bisect_left
n=int(sys.stdin.readline())
val_list=list(map(int,sys.stdin.readline().split()))

tmp=[]

for i in range(n):
    idx=bisect_left(tmp,val_list[i])

    #가장 큰 값인 경우 추가
    if len(tmp)<=idx:
        tmp.append(val_list[i])
    #아니라면 자기 위치의 값과 치환됨
    else:
        tmp[idx]=val_list[i]
print(len(tmp))
