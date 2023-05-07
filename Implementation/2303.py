import sys
n=int(sys.stdin.readline())
max_num=[]
sum
def check(l):
    result=0
    for i in range(3):
        for j in range(i+1,4):
            for k in range(j+1,5):
                tmp=(l[i]+l[j]+l[k])%10
                if tmp>result:
                    result=tmp
    return result
for _ in range(n):
    num=list(map(int, sys.stdin.readline().split()))
    max_num.append(check(num))
if max_num.count(max(max_num))>1:
    for i in range(n-1,-1,-1):
        if max_num[i]==max(max_num):
            print(i+1)
            break
else:
    print(max_num.index(max(max_num))+1)
