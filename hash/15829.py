import sys
n=int(sys.stdin.readline())
sentence=list(sys.stdin.readline())
hashVal=[]
for i in range(n):
    val=((31**i)*(ord(sentence[i])-96))
    hashVal.append(val)
print(sum(hashVal)%1234567891)