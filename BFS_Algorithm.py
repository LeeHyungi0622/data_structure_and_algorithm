def bfs(graph, start_node):
    visited = list()
    need_visit = list()

    # start_node를 need_visit 큐에 넣어주고 시작
    need_visit.append(start_node)
    count = 0
    # need_visit에 값이 있을때까지 순회
    while need_visit:
        count += 1
        node = need_visit.pop(0)
        if node not in visited:
            visited.append(node)
            # pop한 node를 key로 갖는 values를 need_visit 리스트의 뒤에 extend로 붙여준다.
            need_visit.extend(graph[node])
    print(count)
    return visited


def main():
    graph = dict()
    # 각 노드를 key값으로 넣어주고, 인접노드를 value로 넣는다.
    graph['A'] = ['B', 'C']
    graph['B'] = ['A', 'D']
    graph['C'] = ['A', 'G', 'H', 'I']
    graph['D'] = ['B', 'E', 'F']
    graph['E'] = ['D']
    graph['F'] = ['D']
    graph['G'] = ['C']
    graph['H'] = ['C']
    graph['I'] = ['C', 'J']
    graph['J'] = ['I']
    print(bfs(graph, 'A'))


if __name__ == "__main__":
    main()
