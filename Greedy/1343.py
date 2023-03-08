import sys
x=sys.stdin.readline().split()
x=x[0].split(".")

for i in range(len(x)):
    l=len(x[i])
    # x가 홀수 개인 경우
    if len(x[i])%2!=0:
        print(-1)
        exit()
    # x의 개수가 4로 나누어지는 경우
    if l%4==0:
        x[i]='A'*len(x[i])
    else:
        tmp='AAAA'*(l//4)
        l=l%4
        tmp+='B'*l
        x[i]=tmp
# 신기하게 가운데 . 개수가 자동으로 맞춰진다.
print('.'.join(x))