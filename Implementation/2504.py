import sys
word=list(sys.stdin.readline())
word=word[:len(word)-1]
stack=[]
tmp=1
answer=0
for i in range(len(word)):
    if word[i]=="(":
        stack.append("(")
        tmp*=2
    elif word[i]=="[":
        stack.append("[")
        tmp*=3

    elif word[i]==")":
        # 올바르지 않은 괄호
        if not stack or stack[-1]=='[':
            answer=0
            break
        if word[i-1]=="(":
            answer+=tmp
        stack.pop()
        tmp//=2 # 곱할 줄 알고 곱해놨던 것 돌려놓기

    elif word[i]==']':
        # 올바르지 않은 괄호
        if not stack or stack[-1]=='(':
            answer = 0
            break
        if word[i-1]=='[':
            answer+=tmp
        stack.pop()
        tmp//=3 # 곱할 줄 알고 곱해놨던 것 돌려놓기

if stack:
    print(0)
else:
    print(answer)
