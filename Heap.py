class Heap:
    def __init__(self, data):
        # 파이썬에서는 array를 ㅣist로 사용
        self.heap_array = list()
        # 맨 처음 index를 0부터 시작하지 않고 1부터 시작하도록 한다.
        self.heap_array.append(None)
        self.heap_array.append(data)

    # 상위노드와 하위노드를 비교해서 위치를 바꿔야하는지 비교하는 메소드
    def move_up(self, inserted_idx):
        # Root node인지 아닌지 체크
        if inserted_idx <= 1:
            return False

        parent_idx = inserted_idx // 2
        # parent 노드의 값보다 하위 노드의 값이 큰경우 True를 반환해준다.
        if self.heap_array[inserted_idx] > self.heap_array[parent_idx]:
            return True
        else:
            return False

    def insert(self, data):
        if len(self.heap_array) == 0:
            self.heap_array.append(None)
            self.heap_array.append(data)
            return True

        # 0이 아니라면,
        # 리스트상에서 append() 메서드가 리스트의 맨 끝에 붙여주는 메서드이므로,
        self.heap_array.append(data)
        # 들어간 index번호를 체크
        # 실제 들어간 데이터보다 +1 만큼 length가 체크되므로, -1을 해준다.
        inserted_idx = len(self.heap_array) - 1

        # 부모노드랑 바꿔줘야한다는 조건
        while self.move_up(inserted_idx):
            # 현재 부모노드를 알아내기 위한 수식 (2로나눈 몫)
            parent_idx = inserted_idx // 2
            # SWAP 수식
            # ([1]inserted_idx, [2]parent_idx) =
            # ([1]parent_idx, [2]inserted_idx)
            self.heap_array[inserted_idx], self.heap_array[parent_idx] = self.heap_array[parent_idx], self.heap_array[inserted_idx]
            # move_up메소드에서 inserted_idx의 인자값으로 while문에서 반복해가면서 값을 비교해야하므로 parent_idx를 inserted_idx 변수에 담는다.
            inserted_idx = parent_idx

        return True


def main():
    # heap = Heap(1)
    # print("Heap array : "+str(heap.heap_array))
    # print("len(heap.heap_array) : "+str(len(heap.heap_array)))
    heap = Heap(15)
    heap.insert(10)
    heap.insert(8)
    heap.insert(5)
    heap.insert(4)
    heap.insert(20)
    print("result : "+str(heap.heap_array))


if __name__ == "__main__":
    main()
