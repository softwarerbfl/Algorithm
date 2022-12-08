import sys

n=int(sys.stdin.readline())
ability=[]
for i in range(n):
    all_list=list(map(int,sys.stdin.readline().split()))
    ability.append(all_list)

member=[x for x in range(1,n+1)]
calc=[] #능력치의 차이를 담는 리스트
def cal(dep,new_abil):
    if len(new_abil)==(n/2):
        link_idx=list(set(member)-set(new_abil))
        start=0 #스타트팀 점수
        link=0 #링크팀 점수
        for i in new_abil:
            for j in new_abil:
                if i!=j :
                    start+=ability[i-1][j-1]
        for i in link_idx:
            for j in link_idx:
                if i!=j:
                    link+=ability[i-1][j-1]
        calc.append(abs(link-start))
        return
    for i in range(dep, n+1):
        if i not in new_abil:
            new_abil.append(i)
            cal(dep+1, new_abil)
            new_abil.pop()
        dep+=1
cal(1,[])
print(min(calc))