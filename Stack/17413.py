import sys
from collections import deque

s=sys.stdin.readline()
# s=s[:len(s)-1]
flag=0 #0이면 역순 1이면 순서대로
tmp=deque()
for i in range(len(s)):
    if s[i]=="<":
        flag=1
        for _ in range(len(tmp)):
            print(tmp.pop(),end="")
        print("<",end="")
    elif s[i]==">":
        flag=0
        for _ in range(len(tmp)):
            print(tmp.pop(),end="")
        print(s[i],end="")
    elif s[i]==" " and flag==0:
        for _ in range(len(tmp)):
            print(tmp.pop(),end="")
        print(" ",end="")
    elif s[i]=='\n':
        for _ in range(len(tmp)):
            print(tmp.pop(), end="")
    else:
        if flag==1: #순서대로
            print(s[i],end="")
        else: #역순
            tmp.append(s[i])
