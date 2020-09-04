def get_max_value(data_list, capacity):
    # 어떤 기준으로 정렬을 할 것인지 key부분에 넣어줄 수 있다.
    # key에 lambda 식을 작성해준다. x는 각각의 Tuple을 가르킨다.
    # x[1]:value(가치), x[0]:weight(무게)
    # x[1]/x[0] = 무게당 가치를 기준으로 data_list를 정렬한다.
    data_list = sorted(data_list, key=lambda x: x[1]/x[0], reverse=True)
    total_value = 0
    details = list()

    # 가치가 높은 순서로 data_list에서 꺼낸다.
    for data in data_list:
        # 가방의 최대무게(capacity)
        # capacity에 비해 data[0]의 무게를 채우지 못할 경우, 쪼개서 넣어야 하므로,
        # 위의 경우는 별도의 코드로 처리한다.
        if capacity - data[0] >= 0:  # capacity가 수용할 수 있는 크기
            capacity -= data[0]     # 통째로 넣는다.
            total_value += data[1]
            details.append([data[0], data[1], 1])
        else:
            fraction = capacity / data[0]
            total_value += data[1] * fraction
            details.append([data[0], data[1], fraction])
            break
    return total_value, details


def main():
    data_list = [(10, 10), (15, 12), (20, 10), (25, 8), (30, 5)]

    data_list = sorted(data_list, key=lambda x: x[1]/x[0], reverse=True)
    print(get_max_value(data_list, 30))


if __name__ == "__main__":
    main()
