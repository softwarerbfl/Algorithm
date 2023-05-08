import sys
paper = [[0 for _ in range(101)] for _ in range(101)]
answer = 0
for _ in range(4):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            paper[i][j] = 1

for p in paper:
    answer += sum(p)
print(answer)