import sys
money=1000-int(sys.stdin.readline())
l=[500,100,50,10,5,1]
count=0
for i in l:
    count+=money//i
    money-=i*(money//i)
print(count)