import sys
a,p = map(int, sys.stdin.readline().split())
num=[a]
tmp=a # 이전 값
next_num=0 # 다음 값
find_idx=0
while True:
    next_num=0
    while True:
        x=tmp%10
        next_num+=pow(x,p)
        tmp=tmp//10
        if tmp==0:
            break
    tmp=next_num

    if tmp in num:
        find_idx=num.index(tmp)
        break
    num.append(tmp)

print(find_idx)
