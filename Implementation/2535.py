import sys
n=int(sys.stdin.readline())
arr=[]
for _ in range(n):
    nation, num, score=map(int, sys.stdin.readline().split())
    arr.append([score,nation,num])
arr.sort(reverse=True)
nation_num=[]
for i in range(n):
    # 금메달, 은메달 수상자
    if i==0 or i==1:
        print(" ".join(map(str, [arr[i][1], arr[i][2]])))
        nation_num.append(arr[i][1]) # 수상받은 학생의 지역 번호
        continue
    # 동메달 수상자
    if nation_num.count(arr[i][1])<2:
        print(" ".join(map(str, [arr[i][1], arr[i][2]])))
        break
    else:
        continue