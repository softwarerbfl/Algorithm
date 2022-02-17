num=[0]*42 #나머지의 개수
for i in range(10):
    a=int(input())
    num[a%42]+=1
count=0 #서로 다른 나머지의 개수
for j in range(42):
    if(num[j]!=0):
        count+=1

print(count)