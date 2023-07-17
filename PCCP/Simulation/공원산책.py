def solution(park, routes):
    dr=[-1,0,1,0]
    dc=[0,1,0,-1]
    d={"N":0,"E":1,"S":2, "W":3}
    n=len(park)
    m=len(park[0])
    for i in range(n):
        for j in range(m):
            if park[i][j]=="S":
                r=i # 시작 지점의 행
                c=j # 시작 지점의 열
                break

    for i in range(len(routes)):
        op, k = routes[i].split()
        direction=d[op] # 방향
        cnt=0
        ignore=0
        nr,nc=r,c
        # 주어진 방향으로 주어진 칸 수 만큼 이동
        while cnt<int(k):
            cnt+=1
            nr = nr+dr[direction]
            nc = nc+dc[direction]
            # 주어진 영역 밖이거나 장애물이 있는 경우
            if nr<0 or nr>=n or nc<0 or nc>=m or park[nr][nc]=="X":
                ignore=1 # 해당 명령 무효화
                break
        if ignore==0:
            r=nr
            c=nc
    return [r,c]
