import sys
N=int(sys.stdin.readline())
mine=sorted(list(map(int,sys.stdin.readline().split(" "))))
start=min(mine)
end=max(mine)

M=int(sys.stdin.readline())
find=list(map(int,sys.stdin.readline().split(" ")))
ans= {}
def binary(x,mine,startIdx,endIdx):
    if x not in mine:
        return 0
    middle=(startIdx+endIdx)//2
    if x==mine[middle]:
        return N[startIdx:endIdx].count(x)
    elif x>mine[middle]:
        binary(x,mine,middle,endIdx)


