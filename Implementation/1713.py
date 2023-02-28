import sys
n=int(sys.stdin.readline())
recommend=int(sys.stdin.readline())
rec_stu=list(map(int, sys.stdin.readline().split()))
stu_num={}
for i in range(recommend):

    # 후보로 등록되어 있는 경우
    if rec_stu[i] in stu_num.keys():
        stu_num[rec_stu[i]]+=1
    else:
        # 사진 틀에 자리가 있는 경우
        if len(stu_num)<n:
            stu_num[rec_stu[i]]=1
        # 사진 틀 자리가 없는 경우
        else:
            value = list(stu_num.values())  # 추천 수
            key = list(stu_num.keys())  # 학생 번호
            min_recommend = min(value)  # 최소 투표 수
            idx = value.index(min_recommend)
            stu_num.pop(key[idx])

            # 새로 추천받은 학생 등록시키기
            stu_num[rec_stu[i]] = 1

print(" ".join(map(str, sorted(list(stu_num.keys())))))