import sys
n=int(sys.stdin.readline())
stu=[]
for _ in range(n):
    s=list(sys.stdin.readline())
    stu.append(s[:len(s)-1])
# 뒤에서 i번째 인덱스 확인
for i in range(len(stu[0])-1,-1,-1):
    tmp=[]
    for j in range(n):
        if stu[j][i:] not in tmp:
            tmp.append(stu[j][i:])
    if len(tmp)==n:
        print(len(stu[0])-i)
        exit()