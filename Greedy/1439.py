import sys
word=sys.stdin.readline()
word_0=word.split("0")
word_1=word.split("1")
count_0=0
count_1=0
for w0 in word_0:
    if w0=='' or w0=='\n':
        continue
    else:
        count_0+=1
for w1 in word_1:
    if w1=='' or w1=='\n':
        continue
    else:
        count_1+=1

print(min([count_1, count_0]))