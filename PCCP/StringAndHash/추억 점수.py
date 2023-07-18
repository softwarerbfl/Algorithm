from collections import defaultdict
def solution(name, yearning, photo):
    answer = []
    # 각 사람의 그리움의 정도를 담는 배열
    people=defaultdict(int)
    for n in range(len(name)):
        people[name[n]]=yearning[n]
    for i in range(len(photo)):
        score=0
        for j in photo[i]:
            score+=people[j]
        answer.append(score)
    return answer