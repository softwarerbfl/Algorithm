import sys
from collections import deque

n=int(sys.stdin.readline())
card=deque()
count= n
#카드가 쌓여있는 더미 생성
for i in range(n):
    card.append(i+1)
while True:
    if count<=1:
        print(card[0])
        break
    card.popleft()
    tmp=card[0]
    card.popleft()
    card.append(tmp)
    count-=1