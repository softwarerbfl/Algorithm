import sys
import heapq
n=int(sys.stdin.readline())
word=[]
word_list=[]
for i in range(n):
    w=sys.stdin.readline().strip()
    if w in word_list:
        continue
    else:
        heapq.heappush(word, [len(w), w])
        word_list.append(w)

for _ in range(len(word)):
    tmp=heapq.heappop(word)
    print(tmp[1])