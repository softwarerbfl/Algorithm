# 그리디 - BOJ 15903 카드 합체 놀이
import sys
n, m=map(int, sys.stdin.readline().split())
num=list(map(int, sys.stdin.readline().split()))

for _ in range(m):
    min_n1=min(num) # 가장 작은 값
    num.remove(min_n1)
    min_n2=min(num) # 두 번째로 작은 값
    num[num.index(min_n2)]=min_n1+min_n2;
    num.append(min_n1+min_n2)

print(sum(num))