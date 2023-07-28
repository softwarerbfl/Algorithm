import sys
from collections import deque
n=int(sys.stdin.readline())
item=[x for x in range(n,0,-1)]
item=deque(item)
while item:
    find_sum=item.pop() # find_sum의 분해합 구하기
    tmp=find_sum
    num = []
    for cnt in range(6, -1, -1):
        # 자리수: cnt+1
        if find_sum // (10 ** cnt) > 0:
            for i in range(1, cnt + 2):
                num.append(find_sum % 10)
                find_sum = find_sum // 10

            if tmp+sum(num)==n:
                print(tmp)
                exit()
print(0)
