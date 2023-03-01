import sys
# - 부분으로 나눠서 0번째 인덱스 제외 나머지 모두 빼기
oper=sys.stdin.readline().split("-")
result=sum(list(map(int,oper[0].split("+"))))

for i in range(1,len(oper)):
    tmp=oper[i].split("+")
    tmp=sum(list(map(int, tmp)))
    result-=tmp
print(result)