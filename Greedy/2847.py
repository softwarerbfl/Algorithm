import sys
n=int(sys.stdin.readline())
score=[]
count=0
for _ in range(n):
    x=int(sys.stdin.readline())
    score.append(x)
for i in range(n-1,0,-1):
    # 더 어려운 스테이지의 점수가 더 큰 경우
    if score[i]>score[i-1]:
        continue
    # 더 어려운 스테이지의 점수가 더 작은 경우
    else:
        # 스코어 수정
        count+=score[i-1]-score[i]+1
        score[i-1]=score[i]-1
print(count)
