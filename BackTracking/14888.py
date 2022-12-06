import sys

N=int(sys.stdin.readline())
val_list=list(map(int,sys.stdin.readline().split())) #숫자
#연산자(+,-,*,/)
oper_list=list(map(int,sys.stdin.readline().split()))


result=[]

#val은 남은 숫자 배열, oper은 남은 연산자
def calc(val,oper):
    #계산식이 생성된 경우
    if len(val)==1:
        result.append(val[0])
    for i in range(len(oper)):
        #연산자가 있고 그게 아직 사용안된 경우
        if oper[i]>0:
            if i==0:
                value=val[0]+val[1]
            elif i==1:
                value=val[0]-val[1]
            elif i==2:
                value=val[0]*val[1]
            elif i==3:
                value=int(val[0]/val[1])
            new_val=val[2:N+1]
            new_val.insert(0,value) #새로운 숫자 리스트 생성
            oper_list[i]=oper_list[i]-1 #연산자 사용 처리
            calc(new_val,oper_list)
            oper_list[i]=oper_list[i]+1 #연산자 사용 복구

calc(val_list,oper_list)
print(max(result))
print(min(result))