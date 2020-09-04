import random

# 좀 더 간단하게 작성해보기


def qsort(data):
    if len(data) <= 1:
        return data

    pivot = data[0]

    # list comprehension을 사용해서 앞서 QuickSort에서 작성했던 코드보다
    # 간단하게 작성을 할 수 있다.
    left = [item for item in data[1:] if pivot > item]
    right = [item for item in data[1:] if pivot <= item]

    return qsort(left) + [pivot] + qsort(right)


def main():
    data_list = random.sample(range(100), 10)
    print("(Before)quick sort array : " + str(data_list))
    print("(After) quick sort result : " + str(qsort(data_list)))


if __name__ == "__main__":
    main()
