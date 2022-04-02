import sys
N=int(sys.stdin.readline())
Q = [i for i in range(1,N+1)]
while True:
    print(Q[0],end=" ")
    Q.pop(0)
    if len(Q)==0:
        break
    Q.append(Q[0])  #맨 뒤에 추가해주고
    Q.pop(0) #앞에꺼는 삭제
    if len(Q)==0:
        break