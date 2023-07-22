import sys
from collections import defaultdict
from collections import Counter
word=list(sys.stdin.readline())
word=word[:len(word)-1]
word_count=Counter(word)
word_dict=defaultdict(list)
# 단어들의 집합
word_set=list(word_count.keys())
word_set.sort()
for i in range(len(word_count)):
    word_dict[word_set[i]] = [word_count[word_set[i]], word_set[i]]

result=''

# 단어의 개수가 짝수인 경우
if len(word)%2==0:
    for i in range(len(word_set)):
        # 만약 한 단어의 개수가 홀수이면 불가능
        if word_count[word_set[i]]%2==1:
            print("I\'m Sorry Hansoo")
            exit()
        result+=word_set[i]*int(word_count[word_set[i]]/2)
    result+=result[::-1]
# 단어의 개수가 홀수인 경우
else:
    odd_count=0 # 홀수 개수
    odd_word=''
    for i in range(len(word_set)):
        # 단어의 개수가 홀수인 경우
        if word_count[word_set[i]]%2==1:
            odd_count+=1
            odd_word=word_set[i]
            result+=word_set[i]*int((word_count[word_set[i]]-1)/2)
            if odd_count>=2:
                print("I\'m Sorry Hansoo")
                exit()
        else:
            result+=word_set[i]*int(word_count[word_set[i]]/2)
    result+=(odd_word+result[::-1])
print(result)
