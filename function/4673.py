def d(n):
    length=len(str(n))
    num=n
    for i in range(length):
        num=num+(n//pow(10,length-1-i))
        n=n-(n//pow(10,length-1-i))*pow(10,length-1-i)
    return num

none_self=[0]*10000 #0~9999까지 각 숫자별 생성자의 개수
for start in range(1,9999):
    end=d(start)
    if(end>=10000):
        pass
    else:
        none_self[end]=none_self[end]+1
for i in range(1,10000):
    if(none_self[i]==0):
        print(i)
