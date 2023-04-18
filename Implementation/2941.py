import sys
n=int(sys.stdin.readline())
num=list(map(int, sys.stdin.readline().split()))
count1=1
count2=1
max_count=1
for i in range(n-1):
    if num[i]<num[i+1]:
        count1+=1
        if max_count<count2:
            max_count=count2
        count2=1
    elif num[i]>num[i+1]:
        count2+=1
        if max_count<count1:
            max_count=count1
        count1=1
    else:
        count1 += 1
        count2 += 1

max_count=max(count1,count2,max_count)
print(max_count)