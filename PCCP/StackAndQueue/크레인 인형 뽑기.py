from collections import deque
def solution(board, moves):
    answer=0
    n=len(board)
    stack=deque()
    top=0
    for line in moves:
        i=0
        while i<n:
            # 뽑을 인형이 있는 경우
            if board[i][line-1]!=0:
                # 같은 인형이 있는 경우
                if top==board[i][line-1]:
                    stack.pop()
                    answer+=2
                else:
                    stack.append(board[i][line-1])
                # 스택이 비어있는 경우
                if len(stack)==0:
                    top=0
                else:
                    top = stack[len(stack) - 1]
                board[i][line - 1] = 0
                break
            i+=1

    return answer