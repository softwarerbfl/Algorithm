import sys
area=int(sys.stdin.readline())
minus=0 # 깎일 영역의 넓이
all_data={i:[] for i in range(1,5)}
# 첫 입력값 가지고 있기
first_direction, first_l, = map(int, sys.stdin.readline().split())

tmp_direction=first_direction
tmp_l=first_l
all_data[tmp_direction].append(tmp_l)

flag=0 # 예외처리용
minus_case=[[2,4],[1,3],[3,2],[4,1]] # 시계 방향으로 도는 경우들

for i in range(1,6):
    direction, l=map(int, sys.stdin.readline().split())
    all_data[direction].append(l)

    # 이전의 입력받은 방향과 이번에 입력받은 방향이 시계방향인 경우 minus 영역
    if [tmp_direction, direction] in minus_case:
        minus = tmp_l*l # 깎일 영역 정하기

    tmp_l=l
    tmp_direction=direction
# 시계 방향인 경우가 없었다면 첫 번째와 마지막 값이 minus영역
if minus==0:
    minus=tmp_l*first_l

result=(sum(all_data[1])*sum(all_data[3])-minus)*area
print(result)