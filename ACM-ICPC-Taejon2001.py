def combineNumber(data):
    if data == 1:
        return 1
    elif data == 2:
        return 2
    elif data == 3:
        return 4

    return combineNumber(data-1) + combineNumber(data-2) + combineNumber(data-3)


def main():
    print(combineNumber(3))


if __name__ == "__main__":
    main()
