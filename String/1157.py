user=list(input().upper())
arr=[0]*26
for i in range(65,91):
    for j in range(0,len(user)):
        if(user[j]==chr(i)):
            arr[i-65]+=1 #개수 증가시키기

count=0 #max값이 몇개 인지 카운트
for x in range(0,26):
    if arr[x]== max(arr):
        count+=1
if count>=2:
    print("?")
else:
    print(chr(arr.index(max(arr))+65))