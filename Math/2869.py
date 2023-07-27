import sys
import math
a,b,v=map(int,sys.stdin.readline().split())

day=(v-b)/(a-b) #떨어질 높이 미리 빼놓고 시작
print(math.ceil(day))