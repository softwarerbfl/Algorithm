from collections import defaultdict
def solution(survey, choices):
    answer=''
    score=defaultdict(int)# 각 성격 유형별 점수
    for i in range(len(survey)):
        c=choices[i]
        s=survey[i]
        if c==1:
            score[s[0]]+=3
        elif c==2:
            score[s[0]]+=2
        elif c==3:
            score[s[0]]+=1
        elif c==5:
            score[s[1]]+=1
        elif c==6:
            score[s[1]]+=2
        elif c==7:
            score[s[1]]+=3
        else:
            continue
    answer+= 'R' if score['R']>=score['T'] else 'T'
    answer += 'C' if score['C'] >= score['F'] else 'F'
    answer += 'J' if score['J'] >= score['M'] else 'M'
    answer += 'A' if score['A'] >= score['N'] else 'N'
    return answer