arr=[]
for i in range(3):
    arr.append(int(input()))
result=arr[0]*arr[1]*arr[2]

count=[0]*10 #0~9까지 개수 담는 배열
length=len(str(result))
while(length>=1):
    count[result//pow(10,length-1)]+=1
    result=result-(result//pow(10,length-1))*pow(10,length-1)
    length-=1

#개수 출력
for i in range(10):
    print(count[i])