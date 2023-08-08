import sys
n, m, k =map(int, sys.stdin.readline().split())
num=list(map(int, sys.stdin.readline().split()))
num.sort(reverse=True)

one_set=k*num[0]+num[1]
result=one_set*(m//(k+1))+(m%(k+1))*num[0]

print(result)