"""
Вам дан ориентированный граф. Известно, что все его вершины достижимы из вершины s=1.
Найдите время входа и выхода при обходе в глубину, производя первый запуск из вершины s.
Считайте, что время входа в стартовую вершину равно 0. Соседей каждой вершины обходите в порядке увеличения номеров.

Формат ввода
В первой строке дано число вершин n (1 ≤ n ≤ 2 * 105) и рёбер (0 ≤ m ≤ 2 * 105).
В каждой из следующих m строк записаны рёбра графа в виде пар (from, to), 1 ≤ from ≤ n — начало ребра,
1 ≤ to ≤ n — его конец. Гарантируется, что в графе нет петель и кратных рёбер.

Формат вывода
Выведите n строк, в каждой из которых записана пара чисел tin_i, tout_i — время входа и выхода для вершины i.
"""

GraphAssoc = dict[int, list[int]]


class Colors:
    WHITE = 0
    GRAY = 1
    BLACK = 2


def time_to_leave(graph: GraphAssoc) -> list[tuple[int, int]]:
    time = -1
    entry, leave = [0] * len(graph), [0] * len(graph)
    for vertex, color in colors.items():
        if color == Colors.WHITE:
            stack: list[int] = [vertex]

            while stack:
                v = stack.pop()
                if colors[v] == Colors.WHITE:
                    time += 1
                    entry[v - 1] = time
                    colors[v] = Colors.GRAY
                    stack.append(v)
                    for neighbor in sorted(graph[v], reverse=True):
                        if colors[neighbor] == Colors.WHITE:
                            stack.append(neighbor)

                elif colors[v] == Colors.GRAY:
                    time += 1
                    leave[v - 1] = time
                    colors[v] = Colors.BLACK

    return list(zip(entry, leave))


def build_adjacency_list(vertices_num: int, edges: list[tuple[int, int]]) -> GraphAssoc:
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
    adjacents = build_adjacency_list(vertices_num, edges)
    colors = dict.fromkeys(range(1, vertices_num + 1), Colors.WHITE)
    times = time_to_leave(adjacents)
    for t_in, t_out in times:
        print(t_in, t_out)
