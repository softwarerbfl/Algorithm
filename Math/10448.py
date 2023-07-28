import sys
t=int(sys.stdin.readline())
three_num=[x*(x+1)//2 for x in range(1,46)]
answer=[0]*1001 # 각 숫자가 삼각수의 합으로 가능한지 여부를 담는 배열
for a in three_num:
    for b in three_num:
        for c in three_num:
            if a+b+c<=1000:
                answer[a+b+c]=1 # 가능

for _ in range(t):
    num=int(sys.stdin.readline())
    print(answer[num])

