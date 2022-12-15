import sys
return_list=[] #경우의 수 리스트를 담을 이중 리스트
def C(dep, new_list,k,val_list):
    return_list=[]

    if len(new_list)==6: # 배열의 길이가 k가 되었을 경우
        return_list.append(new_list)
        print(" ".join(map(str,new_list)))
    for i in range(dep, k):
        if val_list[i] not in new_list:
            new_list.append(val_list[i])
            C(dep+1, new_list, k, val_list)
            new_list.pop()
        dep+=1
while True:
    val = list(map(int, sys.stdin.readline().split()))
    k = val[0]
    if len(val)==1 and k==0:
        break
    s = val[1:k + 1]
    C(0,[],k,s)
    print()
    return_list=[]
    count=0