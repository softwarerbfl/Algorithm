import sys
t=int(sys.stdin.readline())
# 1부터 10까지 값에 대해 1,2,3의 합으로 나타낼 수 있는 방법의 수
result=[0 for _ in range(11)]
result[1]=1
result[2]=2
result[3]=4
def divide(num):
    if result[num]!=0:
        return result[num]
    else:
        return divide(num-1)+divide(num-2)+divide(num-3)
for _ in range(t):
    n=int(sys.stdin.readline())
    print(divide(n))