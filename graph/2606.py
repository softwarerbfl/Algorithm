import sys
computer=int(sys.stdin.readline()) #컴퓨터 개수
connect=int(sys.stdin.readline()) #node 개수
if connect==0:
    print("{0}".format(0))
    exit()
node={}
for j in range(computer):
    node[j+1]=set()
for i in range(connect):
    c1,c2=map(int, sys.stdin.readline().split())
    node[c1].add(c2)
    node[c2].add(c1)
for l in range(1,computer+1):
    if l in node[1]:
        node[1]=node[1].union(node[l])
for r in range(computer,1,-1):
    if r in node[1]:
        node[1]=node[1].union(node[r])
node[1].discard(1)
print(len(node[1]))
