hash_table = list([0 for i in range(8)])


def get_key(data):
    # hash 내장함수. 고정된 숫자값을 반환한다. 최근에는 사용되지 않는다.
    return hash(data)


def hash_function(key):
    return key % 8


def save_data(data, value):
    hash_address = hash_function(get_key(data))
    hash_table[hash_address] = value


def read_data(data):
    hash_address = hash_function(get_key(data))
    return hash_table[hash_address]


def main():
    save_data('MIKE', '01063204954')
    save_data('DAVE', '01020302000')
    print(read_data('MIKE'))
    print(hash_table)


if __name__ == "__main__":
    main()
