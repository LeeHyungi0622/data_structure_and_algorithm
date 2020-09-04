import random


def selection_sort(data):
    for stand in range(len(data)-1):
        lowest = stand
        for index in range(stand+1, len(data)):
            if data[lowest] > data[index]:
                lowest = index
        # 가장작은 숫자의 index와 기준점(stand)를 swap해준다.
        data[lowest], data[stand] = data[stand], data[lowest]
    return data


def main():
    data_list = random.sample(range(100), 10)
    print("Before selection sorting : "+str(data_list))
    print("After selection sorting : "+str(selection_sort(data_list)))


if __name__ == "__main__":
    main()
