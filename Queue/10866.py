import sys
from collections import deque
n=int(sys.stdin.readline()) #입력할 명령어의 개수
d=deque()
order=[]
for i in range(n):
    order=sys.stdin.readline().split()
    if order[0]=="push_front": #덱의 앞에 정수 push
        d.appendleft(int(order[1]))
    elif order[0]=="push_back": #덱의 뒤에 정수 push
        d.append(int(order[1]))
    elif order[0]=="pop_front": #덱의 가장 앞에 있는 정수를 빼고 출력
        if len(d)==0:
            print(-1)
        else:
            pop = d.popleft()
            print(pop)
    elif order[0]=="pop_back": #덱의 가장 뒤에 있는 정수를 빼고 출력
        if len(d)==0:
            print(-1)
        else:
            pop = d.pop()
            print(pop)
    elif order[0]=="size": #덱에 들어있는 정수의 개수 출력
        print(len(d))
    elif order[0]=="empty": #덱이 비어있으면 1, 아니면 0
        if len(d)==0:
            print(1)
        else:
            print(0)
    elif order[0]=="front": #덱의 가장 앞의 정수 출력
        if len(d) == 0:
            print(-1)
        else:
            print(d[0])
    elif order[0]=="back": #덱의 가장 뒤의 정수 추력
        if len(d)==0:
            print(-1)
        else:
            print(d[len(d)-1])
