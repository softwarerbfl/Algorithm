import sys

N,M=map(int, sys.stdin.readline().split())
#check_set의 요소중에 S집합에 포함된 요소의 개수 세기
S=set()
check_set=[]

for _ in range(N):
    S.add(sys.stdin.readline())

for _ in range(M):
    check_set.append(sys.stdin.readline())

check=0
for i in range(M):
    if check_set[i] in S:
        check+=1
print(check)