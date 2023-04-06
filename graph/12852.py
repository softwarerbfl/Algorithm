import sys
from collections import deque
n=int(sys.stdin.readline())

def bfs(v):
    q = deque()
    q.append([v])
    while q:
        num_list = q.popleft()
        tmp_num = num_list[0]  # 맨 마지막에 넣은 숫자
        if tmp_num % 3 == 0:
            q.append([tmp_num // 3]+num_list)
            if tmp_num//3==1:
                return num_list
        if tmp_num % 2 == 0:
            q.append([tmp_num // 2]+num_list)
            if tmp_num//2==1:
                return num_list
        q.append([tmp_num - 1]+num_list)
        if tmp_num-1==1:
            return num_list


result = bfs(n)
result.insert(0,1)
print(len(result)-1)
print(" ".join(map(str, result[::-1])))