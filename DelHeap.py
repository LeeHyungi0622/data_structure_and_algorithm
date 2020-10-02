class Heap:
    def __init__(self, data):
        self.heap_array = list()
        self.heap_array.append(None)
        self.heap_array.append(data)

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
