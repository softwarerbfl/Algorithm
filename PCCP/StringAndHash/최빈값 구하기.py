def solution(array):
    s=set(array)
    d={i:0 for i in s} # 각 원소의 개수를 담는 딕셔너리

    for item in s:
        d[item]=array.count(item)

    max_count=max(d.values()) # 최빈값의 개수
    if list(d.values()).count(max_count)>=2:
        return -1
    else:
        for item in s:
            if d[item]==max_count:
                return item