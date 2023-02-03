import sys
n=int(sys.stdin.readline())
line=list(map(int, sys.stdin.readline().split()))
max_count=0 #정답
for i in range(n):
    count=0
    idx=0
    max=line[i]
    while idx<5:
        idx+=1
        if line[idx]<max:
            continue
        else:
            count+=1
            max=line[idx]
    print(count)
    if count>max_count:
        max_count=count

print(max_count)