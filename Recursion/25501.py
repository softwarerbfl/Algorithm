import sys
T=int(sys.stdin.readline()) #테스트케이스의 개수
count=0
def recursion(str, start, end):
    global count
    count+=1
    if start>=end:
        return 1
    elif str[start]!=str[end]:
        return 0
    else:
        return recursion(str, start+1, end-1)
def isPalindrome(str):
    return recursion(str,0,len(str)-1)

for i in range(T):
    S=list(sys.stdin.readline())
    S=S[0:len(S)-1]
    print(isPalindrome(S),count)
    count=0