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

    # 아래 pop method의 while self.move_down(popped_idx): 부분에 작성한 부분과 동일
    def move_down(self, popped_idx):
        # 왼쪽 자신의 노드
        left_child_popped_idx = popped_idx * 2
        right_child_popped_idx = popped_idx * 2 + 1
        # CASE1: 왼쪽 자식 노드도 없을 때
        # Array -1 한 곳까지 데이터가 들어가있다.
        # length값 이상이면 없는 곳을 가르키고 있는 것을 의미한다.
        if left_child_popped_idx >= len(self.heap_array):
            return False
        # CASE2: 오른쪽 자식 노드만 없을때 (왼쪽 자식 노드는 있고,)
        elif right_child_popped_idx >= len(self.heap_array):
            if self.heap_array[popped_idx] < self.heap_array[left_child_popped_idx]:
                return True
            else:
                return False
        # CASE3: 왼쪽, 오른쪽 자식 노드 모두 있을 때
        else:
            # 자식노드끼리 비교
            # 왼쪽 노드의 크기가 더 큰 경우
            if self.heap_array[left_child_popped_idx] > self.heap_array[right_child_popped_idx]:
                # heap_array[popped_index]:부모노드 보다 left_child_popped_node가 크다면 True를 반환
                if self.heap_array[popped_idx] < self.heap_array[left_child_popped_idx]:
                    return True
                else:
                    return False
            else:
                if self.heap_array[popped_idx] < self.heap_array[right_child_popped_idx]:
                    return True
                else:
                    return False

    # 최상위 1번 인덱스의 노드값을 빼간다.

    def pop(self):
        if len(self.heap_array) <= 1:
            return None

        # [0]은 None으로 [1]번 인덱스부터 상요하기로 했으므로
        returned_data = self.heap_array[1]
        # -1 인덱스는 리스트의 가장 마지막에 있는 데이터를 의미한다.
        self.heap_array[1] = self.heap_array[-1]
        # 제일 마지막 array의 공간을 삭제
        del self.heap_array[-1]
        popped_idx = 1

        while self.move_down(popped_idx):
            # 왼쪽 자신의 노드
            left_child_popped_idx = popped_idx * 2
            right_child_popped_idx = popped_idx * 2 + 1
            # CASE1: 왼쪽 자식 노드도 없을 때
            # Array -1 한 곳까지 데이터가 들어가있다.
            # length값 이상이면 없는 곳을 가르키고 있는 것을 의미한다.
            if left_child_popped_idx >= len(self.heap_array):
                return False
            # CASE2: 오른쪽 자식 노드만 없을때 (왼쪽 자식 노드는 있고,)
            if right_child_popped_idx >= len(self.heap_array):
                if self.heap_array[popped_idx] < self.heap_array[left_child_popped_idx]:
                    self.heap_array[popped_idx], self.heap_array[left_child_popped_idx] = self.heap_array[
                        left_child_popped_idx], self.heap_array[popped_idx]
                    # 바뀌어진 데이터의 index를 popped_indx변수에 넣어준다.
                    popped_idx = left_child_popped_idx
            # CASE3: 왼쪽, 오른쪽 자식 노드 모두 있을 때
            else:
                # 자식노드끼리 비교
                # 왼쪽 노드의 크기가 더 큰 경우
                if self.heap_array[left_child_popped_idx] > self.heap_array[right_child_popped_idx]:
                    # heap_array[popped_index]:부모노드 보다 left_child_popped_node가 크다면 True를 반환
                    if self.heap_array[popped_idx] < self.heap_array[left_child_popped_idx]:
                        self.heap_array[popped_idx], self.heap_array[left_child_popped_idx] = self.heap_array[
                            left_child_popped_idx], self.heap_array[popped_idx]
                        # 바뀌어진 데이터의 index를 popped_indx변수에 넣어준다.
                        popped_idx = left_child_popped_idx
                else:
                    if self.heap_array[popped_idx] < self.heap_array[right_child_popped_idx]:
                        self.heap_array[popped_idx], self.heap_array[right_child_popped_idx] = self.heap_array[
                            right_child_popped_idx], self.heap_array[popped_idx]
                        # 바뀌어진 데이터의 index를 popped_indx변수에 넣어준다.
                        popped_idx = right_child_popped_idx
            return returned_data

    # 가장 마지막 인덱스에 들어간 노드의 값을 삭제한 최상위 루트노드에 넣고
    # 하위 자식노드 2개와 루트노드의 값을 비교해서 큰 값을 루트노드의 값과 SWAP한다.
    # 자식노드가 없을때까지 지속한다.


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
    print(heap.pop())
    print("result : "+str(heap.heap_array))


if __name__ == "__main__":
    main()
