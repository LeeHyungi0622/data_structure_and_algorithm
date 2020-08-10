import hashlib


def sha1Func():
    # encode() : byte로 바꿔준다는 의미
    data = 'test'.encode()
    hash_object = hashlib.sha1()
    hash_object.update(data)
    # hash_object.update(b'test')
    # string은 unicode는 코드 체계에 기반해서 연결이 되어있기 때문에 바이트 형태로 문자데이터를 풀어준다음에 hash함수에 넣어주어야 해쉬값이 추출이 된다.

    # 16진수로 보통 추출하기 때문에 hexdigest()를 써서 추출한다.
    hex_dig = hash_object.hexdigest()
    print("Hex result : ", hex_dig)


def main():
    sha1Func()


if __name__ == "__main__":
    main()
