def solution(n):
    answer=[[0]*n for _ in range(n)]
    dr=[-1,0,1,0]
    dc=[0,1,0,-1]

    r, c = 0,0
    d=1
    k=n*n
    cnt=1
    answer[r][c]=cnt
    while cnt<k:
        nr=r+dr[d]
        nc=c+dc[d]
        # 앞 길이 막혀 있거나 숫자가 적힌 경우
        if nr<0 or nr>=n or nc<0 or nc>=n or answer[nr][nc]!=0:
            d=(d+1)%4
            continue
        cnt += 1
        r=nr
        c=nc
        answer[r][c]=cnt
    return answer