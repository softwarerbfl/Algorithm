#완전 내가 만든 규칙...(아무도 이해못할 수도 있다!)
import sys
x=int(sys.stdin.readline())
i=0
while True:
    if i*(i+1)/2<x<= (i+1)*(i+2)/2:
        #i가 홀수일 때
        if i%2==1:
            n = (i + 1) * (i + 2) / 2 - x
            print(int(i + 1 - n), end="")
            print("/", end="")
            print(int(1 + n), end="")
        #i가 짝수일 때
        else:
            n = (i + 1) * (i + 2) / 2 - x
            print(int(1 + n), end="")
            print("/", end="")
            print(int(i + 1 - n), end="")
        break
    else:
        i+=1