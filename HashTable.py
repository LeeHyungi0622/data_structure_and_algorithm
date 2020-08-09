# 사람의 전화번호를 저장하는 Hash Table관련 method

# Data[0]를 ord() method를 사용해서 ASCII code값으로 변환한다. 해당 ASCII code값이 바로 각 data의 key값이 된다.
# 데이터를 저장할때는 이 Key값과 Data가 한 쌍을 이뤄서 저장이 되어야 한다.

# HASH TABLE 생성
hash_table = list([i for i in range(10)])


def save_data(data, value):
    # data[0]문자를 ASCII code로 변환해서 key 변수에 저장
    key = ord(data[0])
    hash_addr = hash_func(key)
    hash_table[hash_addr] = value


def get_data(data):
    key = ord(data[0])
    hash_addr = hash_func(key)
    return hash_table[hash_addr]


# Hash function(key값을 hash address로 변환해주는 function)
def hash_func(key):
    return key % 5


def main():
    hash_table

    save_data('HYUNGI', '01063204954')
    save_data('PERSON_A', '01011111111')
    save_data('PERSON_B', '01022222222')
    save_data('PERSON_C', '01033333333')
    print("Phone number : "+(get_data('PERSON_B')))
    print("Hash Table(Size) : "+str(len(hash_table)))


if __name__ == "__main__":
    main()
