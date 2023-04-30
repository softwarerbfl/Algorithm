import sys
n, m = map(int, sys.stdin.readline().split())
dna=[[] for i in range(m)]
result=0
for j in range(n):
    d=list(sys.stdin.readline())
    d=d[:m]
    for i in range(m):
        dna[i].append(d[i])
word=[]
for i in range(m):
    count_t = dna[i].count('T')
    count_a = dna[i].count('A')
    count_g = dna[i].count('G')
    count_c = dna[i].count('C')
    max_val=max([count_c,count_g,count_a,count_t])
    result+=(n-max_val)
    if count_a==max_val:
        word.append('A')
        continue
    elif count_c==max_val:
        word.append('C')
        continue
    elif count_g==max_val:
        word.append('G')
        continue
    else:
        word.append('T')

print(''.join(word))
print(result)