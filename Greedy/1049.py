import sys
n, m =map(int, sys.stdin.readline().split())

min_pack=1000
min_one=1000
result=0
for _ in range(m):
    pack, one = map(int, sys.stdin.readline().split())
    if pack < min_pack:
        min_pack=pack
    if one < min_one:
        min_one = one
# 패키지로 사는 것이 이득인 경우
if min_pack/6 <min_one:
    result += min_pack*(n//6)
    n=n%6
    if n*min_one>min_pack:
        result+=min_pack
    else:
        result+=n*min_one
# 패키지로 사는 것이 손해인 경우
else:
    result = min_one*n
print(result)