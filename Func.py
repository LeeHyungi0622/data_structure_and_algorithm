# 재귀용법으로 풀기
def func(n):
    print(n)
    if n == 1:
        return n

    # 경우의 수를 나눠서 재귀호출
    if n % 2 == 1:
        return (func((3 * n) + 1))
    else:
        return (func(int(n/2)))


def main():
    print(func(3))


if __name__ == "__main__":
    main()
