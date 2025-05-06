"""
Под расстоянием между двумя вершинами в графе будем понимать длину кратчайшего пути между ними в рёбрах.
Для данной вершины s определите максимальное расстояние от неё до другой вершины неориентированного графа.

Формат ввода
В первой строке дано количество вершин n (1 ≤ n ≤ 105) и рёбер m (0 ≤ m ≤ 105). Далее в m строках описаны рёбра графа.
Каждое ребро описывается номерами двух вершин u и v (1 ≤ u, v ≤ n). В последней строке дан номер вершины s (1 ≤ s ≤ n).
Гарантируется, что граф связный и что в нём нет петель и кратных рёбер.

Формат вывода
Выведите длину наибольшего пути от s до одной из вершин графа.
"""

from queue import Queue


GraphAssoc = dict[int, list[int]]


class Colors:
    WHITE = 0
    GRAY = 1
    BLACK = 2


def get_max_distance(graph: GraphAssoc, start_vertex: int) -> int:
    distance: dict[int, int] = {start_vertex: 0}
    colors = dict.fromkeys(range(1, vertices_num + 1), Colors.WHITE)
    colors[start_vertex] = Colors.GRAY
    planned = Queue()
    planned.put(start_vertex)
    while not planned.empty():
        v = planned.get()
        for neighbor in sorted(graph[v]):
            if colors[neighbor] == Colors.WHITE:
                colors[neighbor] = Colors.GRAY
                distance[neighbor] = distance[v] + 1
                planned.put(neighbor)
        colors[v] = Colors.BLACK
    return max(distance.values())


def build_adjacency_list_undirected(vertices_num: int, edges: list[tuple[int, int]]) -> GraphAssoc:
    adjacents = {v: [] for v in range(1, vertices_num + 1)}
    for from_, to in edges:
        adjacents[from_].append(to)
        adjacents[to].append(from_)
    return adjacents


def read_input() -> tuple[int, list[tuple[int, int]], int]:
    vertices_num, edges_num = tuple(map(int, input().strip().split()))
    edges = []
    for _ in range(edges_num):
        edges.append(tuple(map(int, input().strip().split())))
    start_node = int(input().strip())
    return vertices_num, edges, start_node


if __name__ == "__main__":
    vertices_num, edges, start_node = read_input()
    adjacents = build_adjacency_list_undirected(vertices_num, edges)
    print(get_max_distance(adjacents, start_node))
