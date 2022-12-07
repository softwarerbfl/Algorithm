import sys
L,C=list(map(int,sys.stdin.readline().split()))
alp=sys.stdin.readline().split()
alp.sort() #알파벳 정렬
new_list=[]
Vowel=0 #모음
Consonant=0 #자음

def code(dep,new_alp,v,c):
    if len(new_alp)==L and v>=1 and c>=2:
        v=0
        c=0
        print("".join(new_alp))
        return
    for i in range(dep,C):
        if alp[i] not in new_list:
            if alp[i] in ['a','e','i','u','o']:
                v+=1
            else:
                c+=1
            new_list.append(alp[i])
            code(i+1,new_list,v,c)
            if alp[i] in ['a','e','i','u','o']:
                v-=1
            else:
                c-=1
            new_list.pop()
code(0,new_list,0,0)