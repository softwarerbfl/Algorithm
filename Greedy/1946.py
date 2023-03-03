import sys
t=int(sys.stdin.readline())
for _ in range(t):
    n=int(sys.stdin.readline())
    score=[]
    for i in range(n):
        a,b = map(int, sys.stdin.readline().split())
        score.append([a,b])
    score.sort()
    tmp=score[0][1]
    count=1
    for j in range(1, n):
        if score[j][1]<tmp:
            count+=1
            tmp=score[j][1]
    print(count)

