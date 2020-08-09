class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class NodeMgmt:
    def __init__(self, data):
        # 맨 앞의 head를 알고 있어야 전체 링크드 리스트의 정보를 알고 추가/삭제를 할 수 있으므로,
        self.head = Node(data)

    # 해당 링크드 리스트의 맨 끝에 새로운 노드를 추가하는 함수
    def add(self, data):
        if self.head == '':
            self.head = Node(data)
        else:
            # 첫 시작은 self.head의 데이터를 node에 넣어주고
            node = self.head
            # 그 다음의 데이터부터는 다음 노드가 있는지를 체크해가면서 노드의 값을 넣어준다.
            while node.next:
                node = node.next
            # node.next가 null이라면 마지막 노드에는 추가해주려고 하는 노드의 데이터 Node(data)를 추가해준다.
            node.next = Node(data)

        # 해당 링크드 리스트의 전체 데이터를 출력할 수 있는 함수
    def desc(self):
        node = self.head
        # 순회하면서 데이터를 출력
        while node:
            print(node.data)
            node = node.next


def main():
    linkedlist1 = NodeMgmt(0)
    # linkedlist1.desc()

    for data in range(1, 10):
        linkedlist1.add(data)
    linkedlist1.desc()


if __name__ == "__main__":
    main()
