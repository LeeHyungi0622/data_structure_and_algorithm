class Node:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next


class NodeMgmt:
    def __init__(self, data):
        self.head = Node(data)
        self.tail = self.head

    def insert(self, data):
        if self.head == None:
            self.head = Node(data)
            self.tail = self.head
        else:
            node = self.head
            while node.next:
                node = node.next
            # 반복문이 끝나면 노드의 끝을 가르킨다
            new = Node(data)
            node.next = new
            new.prev = node
            self.tail = new

    # head부터 search하는 함수
    def search_from_head(self, data):
        if self.head == None:
            return False

        node = self.head
        while node:
            # 만약 node.data가 우리가 찾던 data이면,
            if node.data == data:
                return node
            else:
                node = node.next
        return False

    # tail부터 search하는 함수
    def search_from_tail(self, data):
        if self.head == None:
            return False

        node = self.tail
        while node:
            if node.data == data:
                return node
            else:
                node = node.prev
        return False

    def insert_before(self, data, before_data):
        if self.head == None:
            # head가 없으면 Node를 만들어주면 된다.
            self.head = Node(data)
            return True
        else:
            node = self.tail
            while node.data != before_data:
                node = node.prev
                if node == None:
                    return False
            new = Node(data)
            before_new = node.prev
            before_new.next = new
            new.prev = before_new
            new.next = node
            node.prev = new

    def desc(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next


def main():
    double_linked_list = NodeMgmt(0)
    for data in range(4, 11):
        double_linked_list.insert(data)
    node_3 = double_linked_list.search_from_head(3)
    node_10 = double_linked_list.search_from_tail(10)
    # insert_before(1.5, 4)
    double_linked_list.insert_before(1.5, 4)
    double_linked_list.desc()

    if(node_3):
        print(node_3.data)
    else:
        print("No Data")

    if(node_10):
        print(node_10.data)
    else:
        print("No Data")


if __name__ == "__main__":
    main()
