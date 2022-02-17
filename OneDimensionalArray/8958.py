N=int(input()) #테스트 케이스 개수
score=[0]*N
for i in range(N):
    result=list(input())
    sequence = 0
    #테스트 케이스 살피기
    for j in range(0,len(result)):
        if(result[j]=="O"):
            score[i]+=1+sequence
            sequence+=1
        else:
            sequence=0
for z in range(N):
    print(score[z])