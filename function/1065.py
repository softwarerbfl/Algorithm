#num보다 작거나 같은 한수의 개수를 반환
def HanNum(num):
    count=0 #세 자리수일 때 한수의 개수
    #두 자리수 이하일 경우
    if(num<100):
        return num
    #세 자리수일 경우
    for i in range(100,num+1):
        check=list(map(int,str(i))) #한수인지 확인할 숫자
        if(check[0]-check[1]==check[1]-check[2]):
            count+=1
    return count+99
N=int(input())
print(HanNum(N))