import sys
count=0 # 계산해야 하는 수업의 개수 카운팅
sum_score=0
for _ in range(20):
    name, num, score = sys.stdin.readline().split()
    num=int(num[0])
    if score=='P':
        continue
    elif score=='A+':
        sum_score+=4.5*num
    elif score=='A0':
        sum_score+=4*num
    elif score=='B+':
        sum_score+=3.5*num
    elif score=='B0':
        sum_score+=3*num
    elif score=='C+':
        sum_score+=2.5*num
    elif score=='C0':
        sum_score+=2*num
    elif score=='D+':
        sum_score+=1.5*num
    elif score=='D0':
        sum_score+=1*num
    else:
        sum_score+=0
    count+=num

print(sum_score/count)