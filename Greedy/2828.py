import sys

n, m = map(int, sys.stdin.readline().split())
j = int(sys.stdin.readline())
loc = []
for _ in range(j):
    x = int(sys.stdin.readline())
    loc.append(x)
left=1
right=m
result=0
if loc[0]<=right:
    result=0
else:
    result+=(loc[0]-right)
    left+=(loc[0]-right)
    right+=(loc[0]-right)
for i in range(1,j):
    l=loc[i]
    if left<=l<=right:
        continue
    elif l>right:
        result+=l-right
        left+=l-right
        right+=l-right
    elif l<left:
        result+=left-l
        right-=left-l
        left -= left - l
print(result)