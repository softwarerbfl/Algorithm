def solution(board):
    answer=0
    dr=[0,-1,0,1,1,1,-1,-1]
    dc=[1,0,-1,0,1,-1,1,-1]
    n=len(board[0])
    for i in range(n):
        for j in range(n):
            if board[i][j]==1:
                for d in range(8):
                    r=i+dr[d]
                    c=j+dc[d]
                    if 0<=r<n and 0<=c<n and board[r][c]!=1:
                        board[r][c]=2
    for i in range(n):
        answer+=board[i].count(0)

    return answer