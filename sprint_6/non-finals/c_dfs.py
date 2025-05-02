"""
Задан неориентированный граф. Обойдите с помощью DFS все вершины, достижимые из заданной вершины s,
и выведите их в порядке обхода, если начинать обход из s.

Формат ввода
В первой строке дано количество вершин n (1 ≤ n ≤ 105) и рёбер m (0 ≤ m ≤ 105). Далее в m строках описаны рёбра графа.
Каждое ребро описывается номерами двух вершин u и v (1 ≤ u, v ≤ n).
В последней строке дан номер стартовой вершины s (1 ≤ s ≤ n). В графе нет петель и кратных рёбер.

Формат вывода
Выведите вершины в порядке обхода, считая что при запуске от каждой конкретной вершины её соседи будут рассматриваться
в порядке возрастания (то есть если вершина 2 соединена с 1 и 3, то сначала обход пойдёт в 1, а уже потом в 3).
"""


class Colors:
    WHITE = 0
    GRAY = 1
    BLACK = 2


def dfs(graph: dict[int, list[int]], start: int) -> None:
    stack = [start]
    while stack:
        v = stack.pop()
        if colors[v] == Colors.WHITE:
            print(v, end=" ")
            colors[v] = Colors.GRAY
            stack.append(v)

            for adj in sorted(graph[v], reverse=True):
                if colors[adj] == Colors.WHITE:
                    stack.append(adj)
        elif colors[v] == Colors.GRAY:
            colors[v] = Colors.BLACK


def build_adjacency_list(vertices_num: int, edges: list[tuple[int, int]]) -> dict[int, list[int]]:
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
    adjacents = build_adjacency_list(vertices_num, edges)
    colors = dict.fromkeys(range(1, vertices_num + 1), Colors.WHITE)
    dfs(adjacents, start_node)
    print()
