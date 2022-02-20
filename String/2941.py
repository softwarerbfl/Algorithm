import re
arr=["c=","c-","dz=","d-","lj","nj","s=","z="]
user=input()
count=0
i=0
while(True):
    if user.find(arr[i])>=0 :
        count+=1
        user = re.sub(arr[i], " ", user, 1)
        i -= 1
    i+=1
    if(i>=len(arr)) : break

user=user.replace(" ","")
count+=len(user)
print(count)
# 좋은 풀이
# croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
# word = input()
#
# for i in croatia :
#     word = word.replace(i, '*')  # input 변수와 동일한 이름의 변수
# print(len(word))