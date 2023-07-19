from collections import defaultdict
def solution(keymap, targets):
    answer=[]
    key_count = defaultdict(int) # 각 키를 누르기 위한 최소 횟수
    for x in keymap:
        for i in range(len(x)):
            if x[i] in key_count:
                if i+1<key_count[x[i]]:
                    key_count[x[i]]=i+1
            else:
                key_count[x[i]]=i+1

    for i in range(len(targets)):
        t=targets[i]
        score=0
        for word in t:
            if word in key_count:
                score += key_count[word]
            else:
                score = -1
                break
        answer.append(score)
    return answer
