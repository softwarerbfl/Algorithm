import sys
n=int(sys.stdin.readline())
triangle=[]
result=[]
for i in range(n):
    t=list(map(int, sys.stdin.readline().split()))
    triangle.append(t)
    result.append([0 for _ in range(i+1)] )
result[0][0]=triangle[0][0]
for i in range(1,n):
    for j in range(i+1):
        if j==0:
            result[i][j]=triangle[i][j]+result[i-1][0]
        elif j==i:
            result[i][j]=triangle[i][j]+result[i-1][i-1]
        else:
            result[i][j]=max(result[i-1][j-1],result[i-1][j])+triangle[i][j]

print(max(result[n-1]))