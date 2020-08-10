# Chaining 기법으로 충돌해결하는 코드를 추가

hash_table = list([0 for i in range(8)])


def get_key(data):
    # hash 내장함수. 고정된 숫자값을 반환한다. 최근에는 사용되지 않는다.
    return hash(data)


def hash_function(key):
    return key % 8


def save_data(data, value):
    index_key = get_key(data)
    hash_address = hash_function(index_key)
    # 데이터가 들어가 있다는 의미 (!=0)
    if hash_table[hash_address] != 0:
        # 현재 hash address부터 순회를 하면서 돈다.
        for index in range(hash_address, len(hash_table)):
            # 현재 hash_table에 data가 들어가 있지 않은 상태이기 때문에 데이터를 넣어주어야 한다.
            if hash_table[index] == 0:
                hash_table[index] = [index_key, value]
                return
            # 키가 같다면 value를 업데이트 한다.
            elif hash_table[index][0] == index_key:
                hash_table[index][1] = value
                return
    else:
        hash_table[hash_address] = [index_key, value]


def read_data(data):
    index_key = get_key(data)
    hash_address = hash_function(index_key)
    if hash_table[hash_address] != 0:
        for index in range(hash_address, len(hash_table)):
            if hash_table[index] == 0:
                # 빈 slot이 나타난다는 것은 데이터가 저장된 적이 없다는 의미이므로 None을 반환한다.
                return None
            elif hash_table[index][0] == index_key:
                # 값을 return
                return hash_table[index][1]
    else:
        # data가 저장되어 있지 않다.
        return None


def main():
    # print(hash('dk') % 8)
    # print(hash('dk') % 8)
    save_data('dk', '0123231421')
    save_data('da', '0123141230')
    print(read_data('dc'))
    # print(hash_table)


if __name__ == "__main__":
    main()
