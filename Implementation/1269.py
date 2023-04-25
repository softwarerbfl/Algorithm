import sys
a, b=map(int, sys.stdin.readline().split())
a_set=set(list(map(int,sys.stdin.readline().split())))
b_set=set(list(map(int,sys.stdin.readline().split())))

count1=a_set.difference(b_set)
count2=b_set.difference(a_set)
print(len(count1)+len(count2))