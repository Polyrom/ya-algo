"""
Алла пошла на стажировку в студию графического дизайна, где ей дали такое задание: для очень большого числа
ориентированных графов преобразовать их список рёбер в список смежности. Чтобы побыстрее решить эту задачу,
она решила автоматизировать процесс.
Помогите Алле написать программу, которая по списку рёбер графа будет строить его список смежности.

Формат ввода
В первой строке дано число вершин n (1 ≤ n ≤ 100) и число ребер m (1 ≤ m ≤ n(n-1)).
В следующих m строках заданы ребра в виде пар вершин (u,v), если ребро ведет от u к v.

Формат вывода
Выведите информацию о рёбрах, исходящих из каждой вершины.
В строке i надо написать число рёбер, исходящих из вершины i, а затем перечислить вершины,
в которые ведут эти рёбра –— в порядке возрастания их номеров.
"""


def build_adjacency_list(vertices_num: int, edges: list[tuple[int, int]]) -> dict[int, list[int]]:
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
    adj_list = build_adjacency_list(vertices_num, edges)
    for _, adjacents in adj_list.items():
        print(len(adjacents), " ".join(list(map(str, adjacents))))
