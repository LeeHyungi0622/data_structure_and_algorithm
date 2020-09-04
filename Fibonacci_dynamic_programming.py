def fibo_dp(num):
    # memorization 기법을 사용
    # list comprehension으로 만들기
    # 0이 채워진 list생성
    cache = [0 for index in range(num+1)]
    cache[0] = 0
    cache[1] = 1

    for index in range(2, num+1):
        cache[index] = cache[index-1] + cache[index-2]
    return cache[num]


def main():
    print(fibo_dp(10))


if __name__ == "__main__":
    main()
