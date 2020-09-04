import random


def insertion_sort(data):
    for index in range(len(data)-1):
        # 1번까지 -1씩 줄여가면서 실행
        for index2 in range(index+1, 0, -1):
            # 앞의 index의 값이 더 크다면 swap이 발생
            if data[index2] < data[index2-1]:
                data[index2], data[index2-1] = data[index2-1], data[index2]
            else:
                break
    return data


def main():
    data_list = random.sample(range(100), 50)
    print("Before insertion sorting: " + str(data_list))
    print("After insertion sorting: " + str(insertion_sort(data_list)))


if __name__ == "__main__":
    main()
