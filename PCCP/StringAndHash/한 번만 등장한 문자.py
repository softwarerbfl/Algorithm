def solution(s):
    answer = []
    s_set=set(s)
    for w in s_set:
        if s.count(w)==1:
            answer.append(w)
    answer= ''.join(sorted(answer))

    return answer