"""
Найдите кратчайшее расстояние между парой вершин в неориентированном графе. Граф может быть несвязным.

Формат ввода
В первой строке дано количество вершин n (1 ≤ n ≤ 105) и рёбер m (1 ≤ m ≤ 105). Далее в m строках описаны рёбра графа.
Каждое ребро описывается номерами двух вершин u и v (1 ≤ u, v ≤ n). В последней строке дан номер стартовой
вершины s (1 ≤ s ≤ n) и конечной t (1 ≤ t ≤ n). Гарантируется, что в графе нет петель и кратных рёбер.

Формат вывода
Выведите длину кратчайшего пути (в рёбрах) между заданной парой вершин. Если пути не существует, то выведите -1.
"""

from queue import Queue


GraphAssoc = dict[int, list[int]]


class Colors:
    WHITE = 0
    GRAY = 1
    BLACK = 2


def get_vertices_distance(graph: GraphAssoc, start: int, end: int) -> int:
    distance: dict[int, int] = {start: 0}
    colors = dict.fromkeys(range(1, vertices_num + 1), Colors.WHITE)
    colors[start] = Colors.GRAY
    planned = Queue()
    planned.put(start)
    while not planned.empty():
        v = planned.get()
        if v == end:
            return distance[v]
        for neighbor in sorted(graph[v]):
            if colors[neighbor] == Colors.WHITE:
                colors[neighbor] = Colors.GRAY
                distance[neighbor] = distance[v] + 1
                planned.put(neighbor)
        colors[v] = Colors.BLACK
    return -1


def build_adjacency_list_undirected(vertices_num: int, edges: list[tuple[int, int]]) -> GraphAssoc:
    adjacents = {v: [] for v in range(1, vertices_num + 1)}
    for from_, to in edges:
        adjacents[from_].append(to)
        adjacents[to].append(from_)
    return adjacents


def read_input() -> tuple[int, list[tuple[int, int]], int, int]:
    vertices_num, edges_num = tuple(map(int, input().strip().split()))
    edges = []
    for _ in range(edges_num):
        edges.append(tuple(map(int, input().strip().split())))
    start_node, end_node = tuple(map(int, input().strip().split()))
    return vertices_num, edges, start_node, end_node


if __name__ == "__main__":
    vertices_num, edges, start, end = read_input()
    adjacents = build_adjacency_list_undirected(vertices_num, edges)
    print(get_vertices_distance(adjacents, start, end))
