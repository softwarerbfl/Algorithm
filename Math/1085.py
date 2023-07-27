import sys

x, y, w, h = map(int, sys.stdin.readline().split())

min_dist=min([x, y, w-x, h-y])
print(min_dist)