import sys
N=int(sys.stdin.readline()) #상근이의 카드 개수
his_card=set(map(int,sys.stdin.readline().split()))
M=int(sys.stdin.readline()) #확인해볼 카드 개수
check_card=list(map(int,sys.stdin.readline().split()))

for i in range(M):
    if check_card[i] in his_card:
        print(1,end=" ")
    else:
        print(0,end=" ")