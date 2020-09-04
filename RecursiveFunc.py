def multiple(num):
    return_value = 1
    for index in range(1, num + 1):
        return_value = return_value * index
    return return_value


def recursiveMultiple(num):
    if num <= 1:
        return num
    return num * multiple(num - 1)


def main():
    print(recursiveMultiple(10))


if __name__ == "__main__":
    main()
