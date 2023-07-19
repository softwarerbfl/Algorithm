from collections import deque
def solution(rank, attendance):
    answer = 0
    attend=[]
    for i in range(len(attendance)):
        if attendance[i]==True:
            attend.append([rank[i],i])
    attend.sort()
    answer=10000*attend[0][1]+100*attend[1][1]+attend[2][1]

    return answer