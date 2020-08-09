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
        # 링크드 리스트의 구현 대신에 python에서 리스트에 append로 덫붙이면 같은 효과가 난다.
        # len(hash_table[hash_address] : 해당 hash_address 주소 내에 몇 개의 데이터가 들어가 있는지 확인하기 위한 처리)
        for index in range(len(hash_table[hash_address])):
            # hash_table[hash_address][index][0]의 index key값을 찾고 있는 index_key와 같은지 확인
            # 같으면 해당 hash_table[hash_address][index][1]의 value값에 value를 넣어준다.(덮어쓴다)
            if hash_table[hash_address][index][0] == index_key:
                hash_table[hash_address][index][1] = value
                return
        # index_key값이 같은 것이 없다면, 해당 hash_table[hash_address]에 [index_key, value]를 append 해준다.
        hash_table[hash_address].append([index_key, value])
    else:
        # 데이터가 아예 없다는 의미
        # list([index_key, value])데이터를 넣어준다.
        hash_table[hash_address] = [[index_key, value]]


def read_data(data):
    index_key = get_key(data)
    hash_address = hash_function(get_key(data))
    if hash_table[hash_address] != 0:
        for index in range(len(hash_table[hash_address])):
            if hash_table[hash_address][index][0] == index_key:
                return hash_table[hash_address][index][1]
        # 키값에 해당하는 값이 없는 경우 None을 반환한다.
        return None
    else:
        return None
    return hash_table[hash_address]


def main():
    hash_table.clear
    save_data('Dd', '010203020012')
    save_data('Data', '01020302000')
    print(read_data('Dd'))
    print(hash_table)


if __name__ == "__main__":
    main()
