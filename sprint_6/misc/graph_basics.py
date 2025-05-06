from typing import Self
from queue import Queue

Color = int


class GraphDirectionTypes:
    DIRECTED = "directed graph"
    UNDIRECTED = "undirected graph"


class GraphColors:
    WHITE = 0
    GRAY = 1
    BLACK = 2

    def __init__(self, graph: dict[int, list[int]]) -> None:
        self.graph = graph
        self.current: int | None = None
        self.values: dict[int, Color] = {}
        self.keys: list[int] = []
        self._build()

    def is_empty(self) -> bool:
        return len(self.values) == 0

    def is_white(self, vertex: int) -> bool:
        return self.values.get(vertex) == self.WHITE

    def is_gray(self, vertex: int) -> bool:
        return self.values.get(vertex) == self.GRAY

    def set_value(self, vertex: int, color: int) -> None:
        if self.values.get(vertex) is not None:
            self.values[vertex] = color

    def reset(self) -> None:
        self.values = {}
        self.keys = []
        self.current = None

    def _build(self) -> None:
        self.values = dict.fromkeys(range(1, len(self.graph) + 1), GraphColors.WHITE)
        if not self.is_empty():
            self.current = 0
        self.keys = list(self.values.keys())

    def __iter__(self) -> Self:
        return self

    def __next__(self) -> int:
        if self.current is None or self.current == len(self.values):
            raise StopIteration
        value = self.keys[self.current]
        self.current += 1
        return value

    def __repr__(self) -> str:
        return f"Colors({str(self.values)})"


class Graph:
    def __init__(self, graph: dict[int, list[int]]) -> None:
        self.graph = graph
        self._colors: GraphColors | None = None
        self._path = []

    def _init_colors(self) -> None:
        self._colors = GraphColors(self.graph)

    def _reset_colors(self) -> None:
        if self._colors:
            self._colors.reset()

    def get_adjacency_matrix(self) -> list[list[int]]:
        matrix = [[0] * len(self.graph) for _ in range(len(self.graph))]
        for from_, tos in self.graph.items():
            for to in tos:
                matrix[from_ - 1][to - 1] = 1
        return matrix

    def _dfs_recur_inner(self, vertex: int) -> None:
        if not self._colors:
            return
        self._colors.set_value(vertex, GraphColors.GRAY)
        self._path.append(vertex)
        for neighbour in self.graph[vertex]:
            if self._colors.is_white(neighbour):
                self._dfs_recur_inner(neighbour)
        self._colors.set_value(vertex, GraphColors.BLACK)
        print(f"Vertex {vertex} colored black")

    def dfs_recur(self) -> list[int]:
        self._path = []

        self._init_colors()
        if not self._colors:
            return []

        for vertex in self._colors:
            if self._colors.is_white(vertex):
                self._dfs_recur_inner(vertex)

        path = self._path
        self._path = []
        self._reset_colors()
        return path

    def dfs_iter(self) -> list[int]:
        self._path = []

        self._init_colors()
        if not self._colors:
            return []

        for start_vertex in self._colors:
            if self._colors.is_white(start_vertex):
                stack = [start_vertex]
                while stack:
                    vertex = stack.pop()
                    if self._colors.is_white(vertex):
                        self._colors.set_value(vertex, GraphColors.GRAY)
                        self._path.append(vertex)
                        stack.append(vertex)
                        for neighbor in self.graph[vertex]:
                            if self._colors.is_white(neighbor):
                                stack.append(neighbor)
                    elif self._colors.is_gray(vertex):
                        self._colors.set_value(vertex, GraphColors.BLACK)
                        print(f"Vertex {vertex} colored black")

        path = self._path
        self._path = []
        self._colors.reset()
        return path

    def bfs(self, start: int = 1) -> list[int]:
        path = []

        if start not in self.graph:
            return []

        self._init_colors()
        if not self._colors:
            return []

        planned = Queue()
        planned.put(start)

        while not planned.empty():
            vertex = planned.get()
            for neighbor in self.graph[vertex]:
                if self._colors.is_white(neighbor):
                    self._colors.set_value(neighbor, self._colors.GRAY)
                    planned.put(neighbor)
            self._colors.set_value(vertex, self._colors.BLACK)
            print(f"Vertex {vertex} colored black")
            path.append(vertex)

        self._reset_colors()
        return path

    def topology_sort(self) -> list[int]:
        result = []

        self._init_colors()
        if not self._colors:
            return []

        for start_vertex in self._colors:
            if self._colors.is_white(start_vertex):
                stack = [start_vertex]
                while stack:
                    vertex = stack.pop()
                    if self._colors.is_white(vertex):
                        self._colors.set_value(vertex, GraphColors.GRAY)
                        stack.append(vertex)
                        for neighbor in self.graph[vertex]:
                            if self._colors.is_white(neighbor):
                                stack.append(neighbor)
                    elif self._colors.is_gray(vertex):
                        result.append(vertex)
                        self._colors.set_value(vertex, GraphColors.BLACK)

        self._colors.reset()
        return result[::-1]

    def __repr__(self) -> str:
        rows: list[str] = []
        for vertex, neighbors in self.graph.items():
            rows.append(f"{vertex} => {' '.join(map(str, neighbors))}")
        return "\n".join(rows)


def test(test_graphs: list[tuple[str, Graph]]) -> None:
    for name, graph in test_graphs:
        test_title = f"Running tests for {name}"
        single_prefix, single_postfix = "| ", " |"
        double_prefix, double_postfix = "|| ", " ||"
        equals_sep_title = "=" * (len(test_title) + len(double_prefix) + len(double_postfix))
        recursive_title = "RECURSIVE"
        iterative_title = "ITERATIVE"
        adjacency_matrix_title = "ADJACENCY MATRIX"
        top_sorted_title = "TOPOLOGICALLY SORTED"
        graph_title = "ASSOCIATIVE LIST"
        dfs_title = " (DFS)"
        bfs_title = " (BFS)"
        dash_sep_adj_matrix = "—" * (len(adjacency_matrix_title) + len(single_prefix) + len(single_postfix))
        dash_sep_assoc = "—" * (len(graph_title) + len(single_prefix) + len(single_postfix))
        dash_sep_dfs_type = "—" * (len(recursive_title) + len(single_prefix) + len(single_postfix) + len(dfs_title))
        dash_sep_bfs_type = "—" * (len(recursive_title) + len(single_prefix) + len(single_postfix) + len(bfs_title))
        dash_sep_sorted = "—" * (len(top_sorted_title) + len(single_prefix) + len(single_postfix))

        print(f"\n{equals_sep_title}\n{double_prefix}{test_title}{double_postfix}\n{equals_sep_title}\n")
        print(f"{dash_sep_assoc}\n{single_prefix}{graph_title}{single_postfix}\n{dash_sep_assoc}")
        print(graph)
        print(f"{dash_sep_adj_matrix}\n{single_prefix}{adjacency_matrix_title}{single_postfix}\n{dash_sep_adj_matrix}")
        adjacency_matrix = graph.get_adjacency_matrix()
        for row in adjacency_matrix:
            print(" ".join(map(str, row)))
        print(f"{dash_sep_sorted}\n{single_prefix}{top_sorted_title}{single_postfix}\n{dash_sep_sorted}")
        print(" ".join(map(str, graph.topology_sort())))
        print(f"{dash_sep_dfs_type}\n{single_prefix}{recursive_title}{dfs_title}{single_postfix}\n{dash_sep_dfs_type}")
        path = graph.dfs_recur()
        print(f"PATH: {' -> '.join(map(str, path))}")
        print(f"{dash_sep_dfs_type}\n{single_prefix}{iterative_title}{dfs_title}{single_postfix}\n{dash_sep_dfs_type}")
        path = graph.dfs_iter()
        print(f"PATH: {' -> '.join(map(str, path))}")
        if name == GraphDirectionTypes.DIRECTED:
            print(
                f"{dash_sep_bfs_type}\n{single_prefix}{iterative_title}{bfs_title}{single_postfix}\n"
                f"{dash_sep_bfs_type}",
            )
            path = graph.bfs()
            print(f"PATH: {' -> '.join(map(str, path))}")


if __name__ == "__main__":
    directed_graph = {
        1: [3],
        2: [3],
        3: [4, 5],
        4: [],
        5: [2],
    }
    undirected_graph = {
        1: [3],
        2: [3, 5],
        3: [2, 4, 5],
        4: [3],
        5: [2, 3],
    }
    test(
        [
            (GraphDirectionTypes.DIRECTED, Graph(directed_graph)),
            (GraphDirectionTypes.UNDIRECTED, Graph(undirected_graph)),
        ],
    )
