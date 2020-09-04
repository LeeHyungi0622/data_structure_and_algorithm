import random


def binary_search(data, search):
    print(data)
    # 데이터가 1개 남았는데 해당 데이터가 찾는 데이터와 일치한다.
    if len(data) == 1 and search == data[0]:
        return True
    # 데이터가 1개 남았는데 해당 데이터가 찾는 데이터와 일치하지 않는다.
    if len(data) == 1 and search != data[0]:
        return False
    # 데이터가 없다.
    if len(data) == 0:
        return False

    # 중간값
    medium = len(data) // 2
    # 만약 찾는 데이터가 data[medium] (중간값)과 일치한다면, True를 반환
    if search == data[medium]:
        return True
    else:
        # 만약 찾는 값이 data[medium]보다 크다면 중간값보다 뒤쪽에 배치되어 있으므로,
        if search > data[medium]:
            # data에 medium 뒤쪽 배치되어있는데이터를 인자로 넣고, 두번째 인자로 search를 넣어 반환한다.
            return binary_search(data[medium:], search)
        else:
            return binary_search(data[:medium], search)


def main():
    data_list = random.sample(range(21), 10)
    # data_list를 정렬시켜줘야 한다.
    data_list.sort()
    print("sort result : "+str(data_list))
    print("search 20 :"+str(binary_search(data_list, 20)))


if __name__ == "__main__":
    main()
