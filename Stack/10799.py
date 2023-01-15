import sys
from collections import deque

stick = deque(sys.stdin.readline())
count_stick=0
tmp_lazer=0 #레이저 연속 여부 확인
flag=0 # 이전 입력 값이 (인지 )인지 확인
tmp_stick=0 #이전에 쌓인 ( 개수

for i in range(len(stick)):
    tmp=stick.popleft()
    #막대의 시작 부분인 경우
    if tmp == '(':
        tmp_lazer=0
        flag=1
        tmp_stick+=1
    #레이저인 경우
    elif tmp == ')' and flag==1:
        if tmp_lazer==0:
            count_stick += tmp_stick -1   # 이전에 있던 막대의 갯수
            tmp_stick-=1
        #레이저 연속 두 번인 경우
        else:
            tmp_stick-=1
        tmp_lazer=1
        flag=0
    #막대의 끝부분인 경우
    elif tmp == ')':
        count_stick+=1
        tmp_stick-=1
        tmp_lazer=0
        flag=0
print(count_stick)