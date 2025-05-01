"""
На этот раз список рёбер ориентированного графа надо переводить в матрицу смежности.

Формат ввода
В первой строке дано число вершин n (1 ≤ n ≤ 100) и число рёбер m (1 ≤ m ≤ n(n-1)). В следующих m строках заданы ребра
в виде пар вершин (u,v), если ребро ведет от u к v.

Формат вывода
Выведите матрицу смежности n на n. На пересечении i-й строки и j-го столбца стоит единица,
если есть ребро, ведущее из i в j.
"""


def build_adjacency_matrix(vertices_num: int, edges: list[tuple[int, int]]) -> list[list[int]]:
    matrix = [[0] * vertices_num for _ in range(vertices_num)]
    for from_, to in edges:
        matrix[from_ - 1][to - 1] = 1
    return matrix


def read_input() -> tuple[int, list[tuple[int, int]]]:
    vertices_num, edges_num = tuple(map(int, input().strip().split()))
    edges = []
    for _ in range(edges_num):
        edges.append(tuple(map(int, input().strip().split())))
    return vertices_num, edges


if __name__ == "__main__":
    vertices_num, edges = read_input()
    matrix = build_adjacency_matrix(vertices_num, edges)
    for row in matrix:
        print(" ".join(map(str, row)))
