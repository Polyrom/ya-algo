from typing import Self

Color = int


class Colors:
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

    def _build(self) -> None:
        self.values = dict.fromkeys(range(1, len(self.graph) + 1), Colors.WHITE)
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


def dfs_recur(graph: dict[int, list[int]]) -> None:
    path = []

    def dfs_recur_inner(graph: dict[int, list[int]], colors: Colors, vertex: int) -> None:
        colors.set_value(vertex, Colors.GRAY)
        print(f"Vertex {vertex} colored gray")
        path.append(vertex)
        for neighbour in graph[vertex]:
            if colors.is_white(neighbour):
                dfs_recur_inner(graph, colors, neighbour)
        colors.set_value(vertex, Colors.BLACK)
        print(f"Vertex {vertex} colored black")

    colors = Colors(graph)
    for vertex in colors:
        if colors.is_white(vertex):
            dfs_recur_inner(graph, colors, vertex)

    print(f"FORWARD PATH: {' '.join(map(str, path))}")


def dfs_iter(graph: dict[int, list[int]]) -> None:
    path = []

    colors = Colors(graph)
    for start_vertex in colors:
        if colors.is_white(start_vertex):
            stack = [start_vertex]
            while stack:
                vertex = stack.pop()
                if colors.is_white(vertex):
                    colors.set_value(vertex, Colors.GRAY)
                    path.append(vertex)
                    print(f"Vertex {vertex} colored gray")
                    stack.append(vertex)
                    for neighbor in graph[vertex]:
                        if colors.is_white(neighbor):
                            stack.append(neighbor)
                elif colors.is_gray(vertex):
                    colors.set_value(vertex, Colors.BLACK)
                    print(f"Vertex {vertex} colored black")

    print(f"FORWARD PATH: {' '.join(map(str, path))}")


def test(test_graphs: list[tuple[str, dict[int, list[int]]]]) -> None:
    for name, graph in test_graphs:
        test_title = f"Running tests for {name}"
        single_prefix, single_postfix = "| ", " |"
        double_prefix, double_postfix = "|| ", " ||"
        hor_equals_sep = "=" * (len(test_title) + len(double_prefix) + len(double_postfix))
        recursive_title = "RECURSIVE"
        iterative_title = "ITERATIVE"
        dfs_title = " (DFS)"
        hor_hyphen_sep = "—" * (len(recursive_title) + len(single_prefix) + len(single_postfix) + len(dfs_title))

        print(f"\n{hor_equals_sep}\n{double_prefix}{test_title}{double_postfix}\n{hor_equals_sep}\n")
        print(f"{hor_hyphen_sep}\n{single_prefix}{recursive_title}{dfs_title}{single_postfix}\n{hor_hyphen_sep}")
        dfs_recur(graph)
        print(f"{hor_hyphen_sep}\n{single_prefix}{iterative_title}{dfs_title}{single_postfix}\n{hor_hyphen_sep}")
        dfs_iter(graph)


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
            ("directed graph", directed_graph),
            ("undirected graph", undirected_graph),
        ],
    )
