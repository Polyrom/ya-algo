"""
Задан неориентированный граф. Обойдите поиском в ширину все вершины, достижимые из заданной вершины s,
и выведите их в порядке обхода, если начинать обход из s.

Формат ввода
В первой строке дано количество вершин n (1 ≤ n ≤ 105) и рёбер m (0 ≤ m ≤ 105). Далее в m строках описаны рёбра графа.
Каждое ребро описывается номерами двух вершин u и v (1 ≤ u, v ≤ n).
В последней строке дан номер стартовой вершины s (1 ≤ s ≤ n).
Гарантируется, что в графе нет петель и кратных рёбер.

Формат вывода
Выведите вершины в порядке обхода, считая что при запуске от каждой конкретной вершины её соседи будут рассматриваться в
порядке возрастания (то есть если вершина 2 соединена с 1 и 3, то сначала обход пойдёт в 1, а уже потом в 3).
"""

from queue import Queue


GraphAssoc = dict[int, list[int]]


class Colors:
    WHITE = 0
    GRAY = 1
    BLACK = 2


def bfs(graph: GraphAssoc, start_vertex: int) -> list[int]:
    path = []
    colors = dict.fromkeys(range(1, vertices_num + 1), Colors.WHITE)
    planned = Queue()
    colors[start_vertex] = Colors.GRAY
    planned.put(start_vertex)
    while not planned.empty():
        v = planned.get()
        for neighbor in sorted(graph[v]):
            if colors[neighbor] == Colors.WHITE:
                colors[neighbor] = Colors.GRAY
                planned.put(neighbor)
        colors[v] = Colors.BLACK
        path.append(v)
    return path


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
    path = bfs(adjacents, start_node)
    print(" ".join(map(str, path)))
