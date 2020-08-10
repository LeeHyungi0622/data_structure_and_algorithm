import hashlib


def sha256Func():
    data = 'data'.encode()
    hash_object = hashlib.sha256()
    hash_object.update(data)
    hex_dig = hash_object.hexdigest()
    return int(hex_dig, 16)


def main():
    print("Result(SHA256) : ", sha256Func())


if __name__ == "__main__":
    main()
