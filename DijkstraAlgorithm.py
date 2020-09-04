# heapq라이브러리 활용해 우선순위 큐 사용하기
import heapq


def dijkstra(graph, start):
    distances = {node: float('inf')for node in graph}
    distances[start] = 0
    queue = []
    # 거리, 노드 순서로 넣어주어야 한다.
    heapq.heappush(queue, [distances[start], start])
    # 위에까지가 초기화를 시켜준 부분이다.

    # 이제부터 우선순위 큐에서 데이터를 하나씩 꺼내서 배열과 최단거리를 비교해서 배열을 업데이트,
    # 큐에 더이상의 데이터가 없을때까지 비교한다.
    while queue:
        # 현재의 거리와 현재의 노드에 대한 정보를 우선순위 큐로부터 뽑아낸다.
        # 가장 작은 값이 pop으로 빠지게 된다. 힙(heap)구조
        current_distance, current_node = heapq.heappop(queue)

        if distances[current_node] < current_distance:
            continue

        for adjacent, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[adjacent]:
                distances[adjacent] = distance
                heapq.heappush(queue, [distance, adjacent])

    return distances


def main():
    mygraph = {
        'A': {'B': 8, 'C': 1, 'D': 2},
        'B': {},
        'C': {'B': 5, 'D': 2},
        'D': {'E': 3, 'F': 5},
        'E': {'F': 1},
        'F': {'A': 5}
    }

    print(dijkstra(mygraph, 'A'))
    # {'A': 0, 'B': 6, 'C': 1, 'D': 2, 'E': 5, 'F': 6}


if __name__ == "__main__":
    main()
