import sys
n,m=list(map(int,sys.stdin.readline().split()))

def permut(dep, new_list):
    if len(new_list)==m:
        print(" ".join(map(str,new_list)))
        return
    for i in range(dep,n+1):
        new_list.append(i)
        permut(max(new_list), new_list)
        new_list.pop()
permut(1,[])