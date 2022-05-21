# 처음에 히스토그램의 가로 길이를 입력받아 width에 저장
width = int(input())
count = 0
# ' '로 구분된 숫자들을 입력받아 height라는 이름의 list에 저장
a = input().split(' ')
height = list(map(int, a))


def max_rect(l_end, r_end):
    # l_end는 왼쪽 끝의 인덱스, r_end는 오른쪽 끝의 인덱스

    # 가로가 한 칸이라면 1 * 높이이므로 그냥 높이 반환 (왼쪽 끝이든 오른쪽 끝이든 같은 높이)
    if (l_end == r_end):
        return height[l_end]

    # mid index를 왼쪽 끝 인덱스와 오른쪽 끝 인덱스의 평균을 내림한 값으로 선언
    m_ind = (l_end + r_end) // 2

    # 이 함수에서 반환해줄 값인 result 선언, 히스토그램을 절반으로 왼쪽과 오른쪽으로 분할해서
    # 더 큰 값을 일단 result에 저장해줌
    result = max(max_rect(l_end, m_ind), max_rect(m_ind + 1, r_end))

    # 가운데서부터 좌우로 나아갈 현재 위치를 나타내는 변수 선언 및 초기화
    # (이후 주석에서는 왼쪽 현 위치, 오른쪽 현 위치라고 작성하겠습니다.)
    l_cur = m_ind
    r_cur = m_ind + 1

    # 현재 높이를 충분히 큰 숫자로 지정
    h_cur = 100000000

    # 양쪽 현 위치가 각각 끝에 도달하기 전 상태
    while ((l_end <= l_cur) and (r_end >= r_cur)):
        # 현재 왼쪽 현 위치, 오른쪽 현 위치, 이전까지의 높이 중 가장 작은 값으로 높이를 초기화
        # 만약 그렇지 않으면 직사각형이 히스토그램 밖으로 벗어남
        # 이 과정을 위해 처음 h_cur을 충분히 큰 숫자로 초기화 한 것
        h_cur = min([height[l_cur], height[r_cur], h_cur])

        # 위에서 계산한 좌 우 히스토그램 중 큰 값과 여기서 계산한 직사각형 크기를 비교해 더 큰 것으로 result를 갱신
        result = max(result, h_cur * (r_cur - l_cur + 1))

        # 왼쪽 현 위치가 끝까지 간 경우, 오른쪽 현 위치를 옮길 수 밖에 없음
        if (l_end == l_cur):
            r_cur += 1

        # 오른쪽 현 위치가 끝까지 간 경우, 왼쪽 현 위치를 옮길 수 밖에 없음
        elif (r_end == r_cur):
            l_cur -= 1

        # 오른쪽 현 위치가 옮길 곳의 높이가 더 높으면 오른쪽 현 위치를 옮겨줌 (탐욕적인 방식에 의해)
        elif (height[l_cur - 1] < height[r_cur + 1]):
            r_cur += 1

        # 왼쪽 현 위치가 옮길 곳의 높이가 더 높으면 왼쪽 현 위치를 옮겨줌 (탐욕적인 방식에 의해)
        elif (height[l_cur - 1] >= height[r_cur + 1]):
            l_cur -= 1

    return result


print(max_rect(0, width - 1))