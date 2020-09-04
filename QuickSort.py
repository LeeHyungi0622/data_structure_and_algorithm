import random


def qsort(data):
    if len(data) <= 1:
        return data

    left, right = list(), list()
    pivot = data[0]

    for index in range(1, len(data)):
        if pivot > data[index]:
            left.append(data[index])
        else:
            right.append(data[index])

    return qsort(left) + [pivot] + qsort(right)


def main():
    data_list = random.sample(range(100), 10)
    print("(Before)quick sort array : " + str(data_list))
    print("(After) quick sort result : " + str(qsort(data_list)))


if __name__ == "__main__":
    main()
