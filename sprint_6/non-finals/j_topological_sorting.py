"""
Дан ациклический ориентированный граф (так называемый DAG, directed acyclic graph).
Найдите его топологическую сортировку, то есть выведите его вершины в таком порядке,
что все рёбра графа идут слева направо. У графа может быть несколько подходящих перестановок вершин.
Вам надо найти любую топологическую сортировку.

Формат ввода
В первой строке даны два числа – количество вершин n (1 ≤ n ≤ 105) и количество рёбер m (0 ≤ m ≤ 105).
В каждой из следующих m строк описаны рёбра по одному на строке. Каждое ребро представлено парой вершин
(from, to), 1≤ from, to ≤ n, соответственно номерами вершин начала и конца.

Формат вывода
Выведите номера вершин в требуемом порядке.
"""

GraphAssoc = dict[int, list[int]]


class Colors:
    WHITE = 0
    GRAY = 1
    BLACK = 2


def topology_sort(graph: GraphAssoc) -> list[int]:
    colors = dict.fromkeys(range(1, vertices_num + 1), Colors.WHITE)
    result = []

    for start_vertex in colors:
        if colors[start_vertex] == Colors.WHITE:
            stack = [start_vertex]
            while stack:
                vertex = stack.pop()
                if colors[vertex] == Colors.WHITE:
                    colors[vertex] = Colors.GRAY
                    stack.append(vertex)
                    for neighbor in sorted(graph.get(vertex, []), reverse=True):
                        if colors[neighbor] == Colors.WHITE:
                            stack.append(neighbor)
                elif colors[vertex] == Colors.GRAY:
                    colors[vertex] = Colors.BLACK
                    result.append(vertex)

    return result[::-1]


def build_adjacency_list_oriented(vertices_num: int, edges: list[tuple[int, int]]) -> GraphAssoc:
    adjacents = {v: [] for v in range(1, vertices_num + 1)}
    for from_, to in edges:
        adjacents[from_].append(to)
    return adjacents


def read_input() -> tuple[int, list[tuple[int, int]]]:
    vertices_num, edges_num = tuple(map(int, input().strip().split()))
    edges = []
    for _ in range(edges_num):
        edges.append(tuple(map(int, input().strip().split())))
    return vertices_num, edges


if __name__ == "__main__":
    vertices_num, edges = read_input()
    adjacents = build_adjacency_list_oriented(vertices_num, edges)
    sorted_graph = topology_sort(adjacents)
    print(" ".join(map(str, sorted_graph)))
