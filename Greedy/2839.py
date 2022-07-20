import sys

N=int(sys.stdin.readline())
five=0
three=0
five=int(N/5) #5kg짜리 봉지 개수(최대 개수)
salt=N
while True:
    salt=N-5*five
    if five<0:
        print(-1)
        break
    if salt % 3 != 0: #남은 설탕이 3으로 나누어 떨어지지 않는 경우
        five=five-1
        continue
    else: #남은 설탕이 3으로 나누어 떨어질 경우
        three=int(salt/3)
        print(three+five)
        break