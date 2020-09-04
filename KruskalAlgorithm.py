
# 초기화할때 사용되는 변수들
# 각각의 노드의 부모의 노드를 저장
parent = dict()
# 해당노드의 rank 정보를 저장
rank = dict()

graph = {
    'vertices': ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
    'edges': [
        # (간선, 시작노드, 끝노드)
        (7, 'A', 'B'),
        (5, 'A', 'D'),
        (7, 'B', 'A'),
        (8, 'B', 'C'),
        (9, 'B', 'D'),
        (7, 'B', 'E'),
        (5, 'C', 'E'),
        (8, 'C', 'B'),
        (5, 'D', 'A'),
        (9, 'D', 'B'),
        (7, 'D', 'E'),
        (6, 'D', 'F'),
        (7, 'E', 'B'),
        (5, 'E', 'C'),
        (7, 'E', 'D'),
        (8, 'E', 'F'),
        (9, 'E', 'G'),
        (6, 'F', 'D'),
        (8, 'F', 'E'),
        (11, 'F', 'G'),
        (9, 'G', 'E'),
        (11, 'G', 'F')
    ]
}

# Parent 노드를 찾는 함수


def find(node):
    # path compression
    if parent[node] != node:
        parent[node] = find(parent[node])
    return parent[node]


def union(node_v, node_u):
    root1 = find(node_v)
    root2 = find(node_u)

    # Union by rank 기법
    if rank[root1] > rank[root2]:
        parent[root2] = root1
    else:
        parent[root1] = root2
        if rank[root1] == rank[root2]:
            rank[root2] += 1


# 각 노드를 개별적인 부분집합으로 초기화
def make_set(node):
    # 노드가 자기자신 하나이므로 상위 노드가 없다. parent node = self
    parent[node] = node
    rank[node] = 0


def kruskal(graph):
    mst = list()
    # vertices list에 있는 node를 순회하면서 반복
    for node in graph['vertices']:
        # 초기화하는 함수 (make_set)
        make_set(node)

    edges = graph['edges']
    edges.sort()

    for edge in edges:
        weight, node_v, node_u = edge
        # node_v의 루트노드와 node_u의 루트노드가 다르다면,
        if find(node_v) != find(node_u):
            union(node_v, node_u)
            mst.append(edge)

    return mst


def main():
    print(kruskal(graph))
    # [(5, 'A', 'D'),
    # (5, 'C', 'E'),
    # (6, 'D', 'F'),
    # (7, 'A', 'B'),
    # (7, 'B', 'E'),
    # (9, 'E', 'G')]


if __name__ == "__main__":
    main()
