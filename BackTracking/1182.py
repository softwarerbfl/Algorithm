import sys

n,s=list(map(int, sys.stdin.readline().split()))

val=list(map(int,sys.stdin.readline().split()))
count=0 #부분 집합의 개수

def sub_sum(index, sum):
    global count

    if index>=n:
        return
    sum+=val[index]
    if sum==s:
        count+=1
    sub_sum(index+1, sum)
    sub_sum(index+1, sum-val[index])
sub_sum(0,0)
print(count)