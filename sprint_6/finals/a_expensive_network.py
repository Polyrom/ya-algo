from dataclasses import dataclass
from functools import total_ordering
import heapq

ERROR_MSG = "Oops! I did it again"


@dataclass(frozen=True, order=False)
@total_ordering
class EdgeWeighted:
    to: int
    weight: int

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, EdgeWeighted):
            return NotImplemented
        return self.to == other.to and self.weight == other.weight

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, EdgeWeighted):
            return NotImplemented
        return self.weight > other.weight

    def __repr__(self) -> str:
        return f"Edge({self.to}, {self.weight})"


GraphAssocWeighted = dict[int, list[EdgeWeighted]]


def add_vertex(
    v: int,
    graph: GraphAssocWeighted,
    added: set[int],
    not_added: set[int],
    heap: list[EdgeWeighted],
) -> tuple[set[int], set[int], list[EdgeWeighted]]:
    added.add(v)
    not_added.remove(v)
    for neighbor in graph[v]:
        if neighbor.to in not_added:
            heapq.heappush(heap, neighbor)
    return added, not_added, heap


def find_max_spanning_tree(graph: GraphAssocWeighted) -> int | None:
    max_sp_sum = 0
    if len(graph) == 0:
        return None
    added = set()
    not_added = set(graph.keys())
    heap = []
    added, not_added, heap = add_vertex(1, graph, added, not_added, heap)
    while not_added and heap:
        top = heapq.heappop(heap)
        if top.to in not_added:
            max_sp_sum += top.weight
            added, not_added, heap = add_vertex(top.to, graph, added, not_added, heap)

    return max_sp_sum if len(not_added) == 0 else None


def read_input() -> GraphAssocWeighted:
    vertices_num, edges_num = map(int, input().strip().split())

    temp_assoc: dict[int, dict[int, int]] = {v: {} for v in range(1, vertices_num + 1)}

    for _ in range(edges_num):
        from_, to, weight = map(int, input().strip().split())

        if to not in temp_assoc[from_] or temp_assoc[from_][to] < weight:
            temp_assoc[from_][to] = weight
            temp_assoc[to][from_] = weight

    assoc_list: GraphAssocWeighted = {
        v: [EdgeWeighted(to=to, weight=w) for to, w in neighbors.items()] for v, neighbors in temp_assoc.items()
    }

    return assoc_list


if __name__ == "__main__":
    adjacents = read_input()
    result = find_max_spanning_tree(adjacents)
    if result is None:
        print(ERROR_MSG)
    else:
        print(result)
