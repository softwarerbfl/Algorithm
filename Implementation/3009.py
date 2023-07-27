import sys
from collections import defaultdict
l=[]
result_x=0
result_y=0
for _ in range(3):
    x, y = map(int, sys.stdin.readline().split())
    l.append([x,y])
if l[0][0]==l[1][0]:
    result_x=l[2][0]
elif l[0][0]==l[2][0]:
    result_x=l[1][0]
else:
    result_x=l[0][0]
if l[0][1]==l[1][1]:
    result_y=l[2][1]
elif l[0][1]==l[2][1]:
    result_y=l[1][1]
else:
    result_y=l[0][1]
print(result_x,result_y)
