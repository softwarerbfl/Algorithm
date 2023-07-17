def solution(numbers, hand):
    answer=''
    left=[3,0]
    right=[3,2]
    key_pad=[[1,2,3],
             [4,5,6],
             [7,8,9],
             [-1,0,-1]]
    for num in numbers:
        for i in range(4):
            for j in range(3):
                if key_pad[i][j]==num:
                    # 찾아야 할 수의 위치
                    find_r = i
                    find_c = j
        if num in [1,4,7]:
            left=[find_r,find_c]
            answer+="L"
            continue
        elif num in [3,6,9]:
            right=[find_r,find_c]
            answer+="R"
            continue

        # 눌러야 하는 숫자가 2 5 8 0 중에 하나인 경우
        dist_l=abs(left[0]-find_r)+abs(left[1]-find_c)
        dist_r=abs(right[0]-find_r)+abs(right[1]-find_c)
        # 왼손이 더 가까운 경우
        if dist_l<dist_r:
            left=[find_r,find_c]
            answer+="L"
        # 오른손이 더 가까운 경우
        elif dist_r<dist_l:
            right=[find_r,find_c]
            answer += "R"
        # 거리가 같은 경우
        else:
            # 오른손 잡이
            if hand=="right":
                right=[find_r,find_c]
                answer += "R"
            # 왼손 잡이
            else:
                left=[find_r,find_c]
                answer += "L"


    return answer