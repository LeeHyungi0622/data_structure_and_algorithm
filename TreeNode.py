import random


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class NodeMgmt:
    def __init__(self, head):
        # head == root node
        self.head = head

    def insert(self, value):
        self.current_node = self.head
        while True:
            # 왼쪽으로 노드를 배치해야되는 상황에
            if value < self.current_node.value:
                # 만약 이미 노드가 있다면
                if self.current_node.left != None:
                    #  비교할 대상을 바꾼다
                    self.current_node = self.current_node.left
                else:
                    # 없다면 새로운 노드를 붙여준다.
                    self.current_node.left = Node(value)
                    break
            else:
                # 같을 경우도 오른쪽에 배치한다.
                if self.current_node.right != None:
                    self.current_node = self.current_node.right
                else:
                    self.current_node.right = Node(value)
                    break

    def search(self, value):
        self.current_node = self.head
        while self.current_node:
            if self.current_node.value == value:
                return True
            elif value < self.current_node.value:
                self.current_node = self.current_node.left
            else:
                self.current_node = self.current_node.right
        return False

    def delete(self, value):
        searched = False
        # current_node : 삭제할 노드를 지칭하도록 처리
        # parent_node : 삭제할 노드의 위에 있는 노드를 지칭하도록 처리
        self.current_node = self.head
        self.parent = self.head
        while self.current_node:
            if self.current_node.value == value:
                searched = True
                break
            # 찾는 value가 작다면 왼쪽으로
            elif value < self.current_node.value:
                # 현재 노드　→ 부모 노드
                self.parent = self.current_node
                # 현재 노드의 왼쪽 노드 → 현재 노드
                self.current_node = self.current_node.left
                # left가 없다면 while이 종료가 되고,
            else:
                # 같거나 크다
                self.parent = self.current_node
                self.current_node = self.current_node.right

            # 1. 해당 노드를 찾은 경우 (searched=True, current_node는 삭제할 노드, parent_node는 삭제할 노드의 부모노드)
            # 2. 노드가 존재하지 않는 경우(searched=False)
        if searched == False:
            return False

        # CASE 1 / CASE 2 / CASE 3
        # 이후부터 CASE들을 분리해서 코드 작성

        # CASE 1: 삭제할 Node가 Leaf Node인 경우
        # self.current_node가 삭제할 Node, self.parent는 삭제할 Node의 parent Node인 상태
        if self.current_node.left == None and self.current_node.right == None:
            if value < self.parent.value:
                self.parent.left = None
            else:
                self.parent.right = None
            del self.current_node

        # CASE 2: 삭제할 Node가 1개의 Child Node를 가지고 있는 경우
        # child의 왼쪽에만 노드가 있는 경우
        elif self.current_node.left != None and self.current_node.right == None:
            if value < self.parent.value:
                self.parent.left = self.current_node.left
            else:
                self.parent.right = self.current_node.right

        # child의 오른쪽에만 노드가 있는 경우
        elif self.current_node.left == None and self.current_node.right != None:
            if value < self.parent.value:
                self.parent.left = self.current_node.right
            else:
                self.parent.right = self.current_node.right

        # CASE 3: 삭제할 Node가 2개의 Child Node를 가지고 있는 경우
        elif self.current_node.left != None and self.current_node != None:  # case 3
            if value < self.parent.value:  # case 3-1
                # 처음에는 change_node, change_node_parent node 둘 다 self.current_node.right의 노드를 가르킨다.
                self.change_node = self.current_node.right
                self.change_node_parent = self.current_node.right
                while self.change_node.left != None:
                    self.change_node_parent = self.change_node
                    self.change_node = self.change_node.left
                # 만약에 마지막 change_node에 오른쪽 child_node가 존재하는 경우,
                # change_node_parent node의 왼쪽 child노드로써 배속시킨다.
                if self.change_node.right != None:
                    self.change_node_parent.left = self.change_node.right
                else:
                    # 고리를 끊기 (삭제노드 left node와의 연결)
                    self.change_node_parent.left = None

                # change node를 parent node로 이동
                self.parent.left = self.change_node
                # change node를 기존의 current node가 연결되어 있던 node들과 연결시켜주는 작업
                self.change_node.right = self.current_node.right
                self.change_node.left = self.current_node.left

            else:  # case 3-2
                self.change_node = self.current_node.right
                self.change_node_parent = self.current_node.right
                while self.current_node.left != None:
                    self.change_node_parent = self.change_node
                    self.change_node = self.change_node.left
                if self.change_node.right != None:
                    self.change_node_parent.left = self.change_node.right
                else:
                    self.change_node_parent.left = None
                self.parent.right = self.change_node
                self.change_node.left = self.current_node.left
                self.change_node.right = self.current_node.right

        return True


def main():
    head = Node(1)
    # BST(Binary Search Tree)
    BST = NodeMgmt(head)
    BST.insert(2)
    BST.insert(3)
    BST.insert(0)
    BST.insert(4)
    BST.insert(8)
    # print(BST.search(8))
    # print(BST.search(-1))

    # 1~1000 숫자 중에서 임의로 100개를 추출해서 이진 탐색 트리에 입력,ㅡ 검색, 삭제

    # 1~ 1000 중 100 개의 숫자 랜덤으로 선택
    # 집합으로, 중복되는 숫자는 제거하고 순수 100개 숫자를 추출
    bst_nums = set()
    while len(bst_nums) != 100:
        bst_nums.add(random.randint(0, 999))
    # print(bst_nums)

    # 선택된 100개의 숫자를 이진 탐색 트리에 입력, 임의로 루트노드는 500을 넣기로 한다.
    head = Node(500)
    # binary search tree에 데이터 넣기
    binary_tree = NodeMgmt(head)
    for num in bst_nums:
        binary_tree.insert(num)

    # 입력한 100개의 숫자 검색(검색 기능 확인)
    for num in bst_nums:
        if binary_tree.search(num) == False:
            print('search failed', num)

    # 입력한 100개의 숫자 중 10개의 숫자를 랜덤 선택
    delete_nums = set()
    # set()을 list()타입으로 변경
    bst_nums = list(bst_nums)
    while len(delete_nums) != 10:
        delete_nums.add(bst_nums[random.randint(0, 99)])

    # 선택한 10개의 숫자를 삭제 (삭제 기능 확인)
    for del_num in delete_nums:
        if binary_tree.delete(del_num) == False:
            print('delete failed', del_num)


if __name__ == "__main__":
    main()
