# 시각 - 완전 탐색
import sys

n=int(sys.stdin.readline())

# 3이 하나이상 포함되는 경우의 수 = 전체 경우의 수 - 3이 포함되지 않는 경우의 수
all_case=(n+1)*6*10*6*10 # 전체 경우의 수
if n<3:
    case=(n+1)*5*9*5*9
elif n==3:
    case=3*5*9*5*9
elif 3<n<13:
    case=n*(5*9*5*9)
elif n==13:
    case=12*(5*9*5*9)
elif 13<n<23:
    case=(n-1)*(5*9*5*9)
elif n==23:
    case=21*5*9*5*9
print(all_case-case)

