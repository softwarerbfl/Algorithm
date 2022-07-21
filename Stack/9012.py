import sys
t=int(sys.stdin.readline())
result=[]

for i in range(t):
    ps=list(sys.stdin.readline())
    ps.pop()
    #스택 양끝이 )또는 (이거나 입력받은 문자열이 홀수개인경우 NO
    if ps[len(ps)-1]=="(" or ps[0]==")" or len(ps)%2==1:
        result.append("NO")
        continue
    stack=[]
    check=1 #2번연속 break확인을 위한 변수
    #괄호 탐색
    for i in range(len(ps)):
        if ps[i]=='(':
            stack.append(1)
        else:
            #스택에 지울 값이 없는 경우 -> (가 없는데 )가 있는 경우
            if len(stack)<=0:
                result.append("NO") #(보다 )가 많은 경우
                check=0
                break
            stack.pop()
    if check==0:
        continue
    if len(stack)>0:
        result.append("NO") #다 지웠는데 stack에 괄호가 남아있는 경우
        continue
    result.append("YES")
for i in range(t):
    print(result[i])