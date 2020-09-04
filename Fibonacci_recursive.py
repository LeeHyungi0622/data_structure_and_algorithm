def fibo(num):
    # recursive call 활용
    if num <= 1:
        return num
    return fibo(num-1) + fibo(num-2)


def main():
    print(fibo(4))


if __name__ == "__main__":
    main()
