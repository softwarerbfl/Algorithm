import sys
height=[]
for i in range(9):
    height.append(int(sys.stdin.readline()))
height.sort()
for a in range(0,3):
    for b in range(a+1,4):
        for c in range(b+1, 5):
            for d in range(c+1, 6):
                for e in range(d+1, 7):
                    for f in range(e+1, 8):
                        for g in range(f+1,9):
                            if height[a] + height[b] + height[c] + height[d] + height[e] + height[f] + height[g] == 100:
                                print(height[a])
                                print(height[b])
                                print(height[c])
                                print(height[d])
                                print(height[e])
                                print(height[f])
                                print(height[g])
                                exit()