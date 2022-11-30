import sys
l=[]
for i in range(5):
    l.append(int(sys.stdin.readline()))

l.sort()
print(int(sum(l)/5))
print(l[2])