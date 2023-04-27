import sys
from collections import deque
def document(count, find, imp):
    queue=deque(imp)
    num=deque([i for i in range(count)])
    result=0
    while True:
        x=queue[0]
        # 이번에 인쇄하려던 문서보다 중요도가 높은 문서가 있는 경우
        if max(queue)!=x:
            a=queue.popleft()
            queue.append(a)
            b=num.popleft()
            num.append(b)
            continue
        # 이번에 인쇄하려는 문서의 중요도가 가장 높은 경우
        else:
            queue.popleft()
            tmp=num.popleft()
            result+=1
            if tmp==find:
                print(result)
                return


t=int(sys.stdin.readline())
for _ in range(t):
    n, m = map(int, sys.stdin.readline().split())
    importance=list(map(int,sys.stdin.readline().split()))
    document(n, m, importance)