import random


def bubblesort(data):
    for index in range(len(data)-1):
        swap = False
        for index2 in range(len(data)-index-1):
            # data[index2](뒤쪽 데이터) data[index2+1](앞쪽 데이터)
            if data[index2] > data[index2+1]:
                data[index2], data[index2+1] = data[index2+1], data[index2]
                # swap이 일어나면 True로 교체
                swap = True

        if swap == False:
            break
    return data


def main():
    data_list = random.sample(range(100), 50)
    print(bubblesort(data_list))


if __name__ == "__main__":
    main()
