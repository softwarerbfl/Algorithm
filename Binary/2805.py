import sys
#n은 나무의 수, m은 나무의 길이
n,m=map(int,sys.stdin.readline().split())
leng=list(map(int,sys.stdin.readline().split(" ")))
tmp=max(leng) #가장 높은 나무의 길이
high=max(leng) #이진탐색에 사용할 변수
low=0
result=0 #가져가려는 나무 길이

while result!=m:
    result=0
    for i in range(n):
        if leng[i]>tmp:
            result=result+(leng[i]-tmp)
        else:
            continue
    #결과가 가져가려는 길이보다 작으면 더 낮게 잘라야하므로 2로 나눔
    if result<m:
        high = tmp
        tmp=(low+high)//2
    #결과가 가져가려는 길이보다 크면 더 높게 잘라야 하므로 키워줌
    elif result>m:
        low = tmp
        tmp = (low + high) // 2
    else:
        print(tmp)
        break