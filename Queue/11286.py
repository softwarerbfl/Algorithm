import sys
import heapq

n=int(sys.stdin.readline())
arr=[] #절댓값과 원래값을 담는 배열
abs_arr=[] #절댓값만 담는 배열
for i in range(n):
    x=int(sys.stdin.readline())

    #0을 입력한 경우
    if x==0 :
        if len(arr)!=0:
            tmp=heapq.heappop(arr)
            print(tmp[1])
        #0을 입력했는데 배열이 비어있는 경우
        else:
            print(0)

    #숫자를 입력한 경우 힙에 넣어줌
    else:
        heapq.heappush(arr,[abs(x),x])