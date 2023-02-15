import sys
n=int(sys.stdin.readline())
x=list(map(int,sys.stdin.readline().split()))
sort_x=sorted(list((set(x))) )#정렬된 배열
dic={sort_x[i] : i for i in range(len(sort_x))}

for i in range(n):
    idx=dic[x[i]] #값에 해당되는 인덱스값
    print(idx, end=" ")