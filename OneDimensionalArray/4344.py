C=int(input())
ratio=[0]*C #비율을 담을 배열
for i in range(C):
    arr=list(map(int,input().split(" ")))
    mean = (sum(arr)-arr[0]) / arr[0]  # 평균
    honor=0
    for s in range(1,arr[0]+1):
        if(arr[s]>mean):
            honor+=1
    ratio[i]=honor/arr[0]*100
for j in range(C):
    print("{0:0.3f}%".format(ratio[j]))
