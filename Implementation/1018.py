import sys
n, m = map(int, sys.stdin.readline().split())
graph=[]

# 시작 지점의 좌표
def search(start_h,start_w):
    global result
    tmp=0
    # 왼쪽 위에 좌표가 B로 시작하는 경우 확인
    # 짝수줄 확인
    for i in range(start_h,start_h+8,2):
        for j in range(start_w, start_w+8):
            if (j-start_w)%2==0 and graph[i][j]!='B':
                tmp+=1
            elif (j-start_w)%2==1 and graph[i][j]!='W':
                tmp+=1

    # 홀수줄 확인
    for i in range(start_h+1,start_h+8,2):
        for j in range(start_w, start_w+8):
            if (j-start_w)%2==0 and graph[i][j]!='W':
                tmp+=1
            elif (j-start_w)%2==1 and graph[i][j]!='B':
                tmp+=1
    result[start_h][start_w] = tmp
    tmp = 0
    # 왼쪽 위에 좌표가 W로 시작하는 경우 확인
    # 짝수줄 확인
    for i in range(start_h,start_h+8,2):
        for j in range(start_w, start_w+8):
            if (j-start_w)%2==0 and graph[i][j]!='W':
                tmp+=1
            elif (j-start_w)%2==1 and graph[i][j]!='B':
                tmp+=1
    # 홀수줄 확인
    for i in range(start_h+1, start_h + 8, 2):
        for j in range(start_w, start_w + 8):
            if (j-start_w) % 2 == 0 and graph[i][j] != 'B':
                tmp += 1
            elif (j-start_w) % 2 == 1 and graph[i][j] != 'W':
                tmp += 1
    # 둘 중 바꿔야하는 값이 더 작은 걸로 return
    if tmp<result[start_h][start_w]:
        result[start_h][start_w]=tmp
        return
    else:
        return
for _ in range(n):
    l=list(sys.stdin.readline())
    graph.append(l[:m])

result=[[0]*(m-7) for _ in range(n-7)]
min_result=n*m
for x in range(n-7):
    for y in range(m-7):
        search(x,y)
    min_tmp=min(result[x])
    if min_tmp<min_result:
        min_result=min_tmp

print(min_result)