import sys
urlim = list(map(int, sys.stdin.readline().split()))
startlink=list(map(int, sys.stdin.readline().split()))
point1=0
point2=0
condition=0
for i in range(9):
    point1+=urlim[i]
    if point1>point2:
        condition=1
        break
    point2+=startlink[i]
    if point1>point2:
        condition=1
        break
# 역전패를 당한 경우
if sum(urlim)<sum(startlink) and condition==1:
    print("Yes")
else:
    print("No")
