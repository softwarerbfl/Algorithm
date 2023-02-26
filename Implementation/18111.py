import sys
n, m, b = map(int, sys.stdin.readline().split())
graph=[]
for _ in range(n):
    height=list(map(int, sys.stdin.readline().split()))
    graph.append(height)
count={} # 각 블럭의 개수를 딕셔너리 형태로 가진다.
time={} # 각 블럭의 높이에 맞추는데 걸리는 시간
for i in range(n):
    for j in range(m):
        if graph[i][j] in count.keys():
            count[graph[i][j]]+=1
        else:
            count[graph[i][j]]=1
for k in range(min(count.keys()),max(count.keys())+1):
    time[k]=0
    block=0
    for tmp_k in count.keys():
        if k==tmp_k:
            continue
        # 블럭을 뺴야 하는 경우
        elif k<tmp_k:
            time[k]+=(tmp_k-k)*count[tmp_k]*2
            block-=count[tmp_k]*(tmp_k-k)
        # 블럭을 쌓아야 하는 경우
        elif k>tmp_k:
            time[k]+=abs(tmp_k-k)*count[tmp_k]
            block+=count[tmp_k]*abs(tmp_k-k)
    # 사용해야 하는 블럭이 사용 가능 블럭 개수를 초과한 경우
    if block>b:
        time.pop(k)

result_time=min(time.values()) # 걸리는 최소 시간

key_list=list(time.keys()) # key들의 리스트
key_values=list(time.values()) # value들의 리스트

print(result_time, end=" ")
max_height=0
# 같은 시간이 걸리는 경우의 수가 여러 개인 경우
if key_values.count(result_time)>1:
    for i in range(len(key_values)):
        if key_values[i]==result_time:
            # 만약 높이가 가장 높은 경우
            if key_list[i]>max_height:
                max_height=key_list[i]
        else:
            continue
    print(max_height)

else:
    print(key_list[key_values.index(result_time)])
