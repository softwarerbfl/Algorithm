import sys
from collections import deque

n=int(sys.stdin.readline())
result=0

def good_word(word):
    tmp_word = deque()
    if len(word)%2==1:
        return 0
    top=word.pop() #a
    while(True):
        if len(word)==0:
            if good_word(tmp_word)==1:
                return 1

        tmp=word.pop() #b
        print(word)
        if tmp==top:
            top=word.pop()
            continue
        else:
            tmp_word.append(top)
            top=tmp
            continue



for i in range(n):
    word=deque(sys.stdin.readline())
    word.pop() #뒤에 \n 삭제
    result+=good_word(word)
print(result)