import sys
n = int(sys.stdin.readline())
friend = []
result=[0] * (n) # 사람마다 친구의 수

def dfs(num):
    global visit
    tmp=friend[num]
    for i in range(n):
        # 친구라면 친구 처리
        if tmp[i]=='Y':
            visit[i]=1
            for j in range(n):
                if friend[i][j] == 'Y' and visit[j] == 0:
                    visit[j]=1
for _ in range(n):
    l=list(sys.stdin.readline())
    friend.append(l[:n])
for k in range(n):
    visit = [0] * (n)
    dfs(k)
    result[k] = sum(visit)

if max(result)==0:
    print(0)
else:
    print(max(result)-1)