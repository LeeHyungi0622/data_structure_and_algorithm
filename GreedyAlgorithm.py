coin_list = [500, 100, 50, 1]


def min_coin_count(value, coin_list):
    total_coin_count = 0
    details = list()
    coin_list.sort(reverse=True)
    for coin in coin_list:
        coin_num = value // coin  # coin_list의 첫번째 index의 값으로 나눈값.
        # 몫 : 갯수
        total_coin_count += coin_num  # 나눠서 나온 몫을 total_coin_count에 더해준다.
        value -= coin_num * coin  # 최종 값에서 coin_num(코인갯수) * coin(코인단위)를 빼준다.
        details.append([coin, coin_num])
    return total_coin_count, details


def main():
    print(min_coin_count(4720, coin_list))
    # (31, [[500, 9], [100, 2], [50, 0], [1, 20]])


if __name__ == "__main__":
    main()
