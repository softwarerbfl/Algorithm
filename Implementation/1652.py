import sys
n=int(sys.stdin.readline())
room=[]
lean1=0
lean2=0
flag1=0 # 이어지는 자리 세기
flag2=0
for _ in range(n):
    r=list(sys.stdin.readline())
    r=r[:n]
    room.append(r)

for i in range(n):
    flag1=0
    flag2=0
    for j in range(n):
        if room[i][j]=='.':
            flag1+=1
        else:
            flag1=0
        if flag1==2:
            lean1+=1

        if room[j][i]=='.':
            flag2+=1
        else:
            flag2=0
        if flag2==2:
            lean2+=1

print(lean1,lean2)
