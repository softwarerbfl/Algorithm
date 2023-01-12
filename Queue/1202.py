import sys
import heapq
n,k=map(int,sys.stdin.readline().split())
max_weight=[] #가방에 담을 수 있는 최대 무게
current_value=0
crystal=[]

for i in range(n):
    m,v=map(int,sys.stdin.readline().split())
    heapq.heappush(crystal, [m,v]) #무게를 기준으로 오름차순 정렬되도록 함

for i in range(k):
    max_weight.append(int(sys.stdin.readline()))
max_weight.sort() #가방 무게 수용치 오름차순 정렬
tmp=[]
for m in max_weight:
    #보석이 있고 들어갈 수 있으면 일단 빼내서 tmp에 가치만 넣음
    #pop했을 떄 큰 값이 나오도록 - 붙여서 저장
    while crystal and m>=crystal[0][0]:
        heapq.heappush(tmp, -heapq.heappop(crystal)[1])
    #들어온게 있다면 value를 합산
    if tmp:
        current_value-=heapq.heappop(tmp)
    #없다면 break하고 다음 가방 확인
    else:
        break
print(current_value)