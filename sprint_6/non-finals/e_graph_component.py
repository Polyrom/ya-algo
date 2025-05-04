"""
Вам дан неориентированный граф. Найдите его компоненты связности.

Формат ввода
В первой строке дано количество вершин n (1≤ n ≤ 105) и рёбер m (0 ≤ m ≤ 2 * 105).
В каждой из следующих m строк записано по ребру в виде пары вершин 1 ≤ u, v ≤ n.
Гарантируется, что в графе нет петель и кратных рёбер.

Формат вывода
Выведите все компоненты связности в следующем формате: в первой строке выведите общее количество компонент.
Затем на отдельных строках выведите вершины каждой компоненты, отсортированные по возрастанию номеров.
Компоненты между собой упорядочивайте по номеру первой вершины.
"""

START_COLOR = -1
GraphAssoc = dict[int, list[int]]


def find_components(graph: GraphAssoc) -> dict[int, int]:
    visited = set()
    colors: dict[int, int] = dict.fromkeys(range(1, len(graph) + 1), START_COLOR)
    component_count = 1

    for vertex in graph:
        if colors[vertex] == START_COLOR:
            stack = [vertex]
            while stack:
                v = stack.pop()
                if v not in visited:
                    visited.add(v)
                    stack.append(v)
                    for neighbor in graph.get(v, []):
                        if neighbor not in visited:
                            stack.append(neighbor)
                else:
                    colors[v] = component_count

            component_count += 1

    return colors


def build_adjacency_list_unoriented(vertices_num: int, edges: list[tuple[int, int]]) -> GraphAssoc:
    adjacents = {v: [] for v in range(1, vertices_num + 1)}
    for from_, to in edges:
        adjacents[from_].append(to)
        adjacents[to].append(from_)
    return adjacents


def read_input() -> tuple[int, list[tuple[int, int]]]:
    vertices_num, edges_num = tuple(map(int, input().strip().split()))
    edges = []
    for _ in range(edges_num):
        edges.append(tuple(map(int, input().strip().split())))
    return vertices_num, edges


if __name__ == "__main__":
    vertices_num, edges = read_input()
    adjacents = build_adjacency_list_unoriented(vertices_num, edges)
    d = find_components(adjacents)

    print(max(d.values()))
    print("\n".join(" ".join(map(str, sorted(k for k in d if d[k] == v))) for v in sorted(set(d.values()))))
