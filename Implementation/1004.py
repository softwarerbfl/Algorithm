import sys
t=int(sys.stdin.readline())
for _ in range(t):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    n=int(sys.stdin.readline())
    count=0
    for i in range(n):
        cx, cy, r=map(int, sys.stdin.readline().split())
        # 둘 다 원 내부에 있는 경우
        if (x1-cx)**2+(y1-cy)**2<=r**2 and (x2-cx)**2+(y2-cy)**2<=r**2:
            continue
        # 둘 다 원 외부에 있는 경우
        elif (x1-cx)**2+(y1-cy)**2>=r**2 and (x2-cx)**2+(y2-cy)**2>=r**2:
            continue
        else:
            count+=1
    print(count)