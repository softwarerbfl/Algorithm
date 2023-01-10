import sys
n=int(sys.stdin.readline())
candidate=[]
t=0
def take(cand):
    global t
    #단일 후보인 경우 종료
    if len(cand)==1:
        return
    #후보 1번이 당선되게 되면 종료
    if cand[0]==max(cand) and cand.count(cand[0])==1:
        return
    other=cand[1:]
    max_val=max(other) #현재 최대 투표수
    max_idx=other.index(max_val) #최대 투표수를 가진 후보의 index

    candidate[0]+=1
    candidate[max_idx+1]-=1
    t+=1
    take(candidate)

for i in range(n):
    candidate.append(int(sys.stdin.readline()   ))

take(candidate)
print(t)