import random


def sum_list(data):
    if len(data) == 1:
        return data[0]

    return "------------------------------------"


def recursive_sum_list(data):
    if len(data) <= 1:
        return data[0]
        # data의 1번 index의 값부터의 값을 전부 인자로 전달.
    return data[0]+sum_list(data[1:])


def main():
    data = random.sample(range(100), 10)
    print(recursive_sum_list(data))


if __name__ == "__main__":
    main()
