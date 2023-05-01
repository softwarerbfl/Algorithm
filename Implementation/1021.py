import sys
from collections import deque
n, m = map(int, sys.stdin.readline().split())
find_num=list(map(int, sys.stdin.readline().split()))
num=deque([i for i in range(1,n+1)])
result=0

while True:
    if len(find_num)==0:
        break
    # 뽑은 수가 찾는 수라면
    if num[0] == find_num[0]:
        find_num.remove(num[0])
        num.popleft()
        continue
    # 존재하지 않는다면
    idx = num.index(find_num[0])
    # 2번 수행을 해야 하는 경우
    if idx<len(num)-idx:
        x=num.popleft()
        num.append(x)
        result+=1
    # 3번 수행을 해야 하는 경우
    else:
        x=num.pop()
        num.appendleft(x)
        result+=1
print(result)