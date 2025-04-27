from dataclasses import dataclass
from functools import total_ordering
from typing import Self


@dataclass(frozen=True, order=False)
@total_ordering
class Competitor:
    name: str
    solved: int
    penalty: int

    def __eq__(self, other: Self) -> bool:
        return self.solved == other.solved and self.penalty == other.penalty and self.name == other.name

    def __lt__(self, other: Self) -> bool:
        if self.solved != other.solved:
            return self.solved < other.solved
        if self.penalty != other.penalty:
            return self.penalty > other.penalty
        return self.name > other.name

    def __repr__(self) -> str:
        return f"Competitor({self.name!r}, {self.solved}, {self.penalty})"


class MaxHeap:
    DUMMY = Competitor("", -1, -1)
    FIRST_ELEMENT_IDX = 1

    def __init__(self, values: list[Competitor]) -> None:
        self.values: list[Competitor] = [self.DUMMY]
        if len(values) > 0:
            self.values.append(values[0])
        for val in values[1:]:
            self.add(val)
    
    def is_empty(self) -> bool:
        return len(self.values) <= 1

    def add(self, key: Competitor) -> None:
        self.values.append(key)
        self._sift_up(len(self.values) - 1)

    def pop_max(self) -> Competitor | None:
        if len(self.values) <= 1:
            return None
        result = self.values[self.FIRST_ELEMENT_IDX]
        last = self.values.pop()
        if len(self.values) > 1:
            self.values[self.FIRST_ELEMENT_IDX] = last
            self._sift_down(self.FIRST_ELEMENT_IDX)
        return result

    def _sift_up(self, index: int) -> None:
        if index == self.FIRST_ELEMENT_IDX:
            return

        parent_index = index // 2
        if self.values[index] > self.values[parent_index]:
            self.values[parent_index], self.values[index] = self.values[index], self.values[parent_index]
            self._sift_up(parent_index)

    def _sift_down(self, index: int) -> None:
        n = len(self.values) - 1
        left_index = 2 * index
        right_index = 2 * index + 1
        largest = index

        if left_index <= n and self.values[left_index] > self.values[largest]:
            largest = left_index
        if right_index <= n and self.values[right_index] > self.values[largest]:
            largest = right_index

        if largest != index:
            self.values[index], self.values[largest] = self.values[largest], self.values[index]
            self._sift_down(largest)


def heapsort(competitors: list[Competitor]) -> list[Competitor]:
    competitors_sorted = []
    mh = MaxHeap([])
    for cmp in competitors:
        mh.add(cmp)
    while not mh.is_empty():
        competitors_sorted.append(mh.pop_max())
    return competitors_sorted


def read_input() -> list[Competitor]:
    n = int(input())
    competitors = []
    for _ in range(n):
        name, solved, penalty = tuple(input().split())
        competitors.append(Competitor(name=name, solved=int(solved), penalty=int(penalty)))
    return competitors


if __name__ == "__main__":
    competitors = read_input()
    competitors_sorted = heapsort(competitors)
    for competitor in competitors_sorted:
        print(competitor.name)
