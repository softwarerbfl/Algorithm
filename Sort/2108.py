import sys
from collections import Counter
n=int(sys.stdin.readline())
num=[]
#정렬된 상태로 num배열 생성
for _ in range(n):
    x=int(sys.stdin.readline())
    num.append(x)
num.sort()

print(round(sum(num)/n)) #산술평균
print(int(num[n//2])) #중앙값

cnt=Counter(num)
mode=cnt.most_common(2)
if len(num)>1 and mode[0][1]==mode[1][1]:
    print(mode[1][0])
else:
    print(mode[0][0])

print(max(num)-min(num)) #범위
