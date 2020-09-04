import random

# 단순 slicing method


def split(data):
    medium = int(len(data)/2)
    # :2 -> 0~1 끝 2번 index는 포함하지 않으므로,
    left = data[:medium]
    # 2: -> 2번 index를 포함한 부분부터 끝까지 slicing
    right = data[medium:]
    print(left, right)

# 재귀용법을 이용한 slicing 처리와 slicing처리후에 merge처리


def mergesplit(data):
    if len(data) <= 1:
        return data
    medium = int(len(data)/2)
    # left와 right가 내부에서 또 다시 분리가 가능하므로,
    left = mergesplit(data[:medium])
    right = mergesplit(data[medium:])
    return merge(left, right)


def merge(left, right):
    merged = list()
    left_point, right_point = 0, 0

    # case1: left/right 아직 남아있을때
    while len(left) > left_point and len(right) > right_point:
        if left[left_point] > right[right_point]:
            merged.append(right[right_point])
            right_point += 1
        else:
            merged.append(left[left_point])
            left_point += 1

    # case2: left만 남아있을때
    while len(left) > left_point:
        merged.append(left[left_point])
        left_point += 1

    # case3: right만 남아있을때
    while len(right) > right_point:
        merged.append(right[right_point])
        right_point += 1

    return merged


def main():
    data_list = random.sample(range(100), 10)
    print(mergesplit(data_list))


if __name__ == "__main__":
    main()
