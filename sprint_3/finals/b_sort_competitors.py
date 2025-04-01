import os
import random
from collections import namedtuple
from copy import deepcopy
from dataclasses import dataclass

ENVIRONMENT = "ENVIRONMENT"
TEST = "TEST"


Competitor = namedtuple("Competitor", ["solved", "penalty", "name"])


def compare_competitors(comp1: Competitor, comp2: Competitor) -> int:  # noqa: PLR0911
    if comp1.solved > comp2.solved:
        return -1
    if comp1.solved < comp2.solved:
        return 1
    if comp1.penalty < comp2.penalty:
        return -1
    if comp1.penalty > comp2.penalty:
        return 1
    if comp1.name > comp2.name:
        return 1
    if comp1.name < comp2.name:
        return -1
    return 0


def partition(competitors: list[Competitor], left: int, right: int) -> int:
    pivot_idx = random.randint(left, right)  # noqa: S311
    pivot = competitors[pivot_idx]
    low = left - 1
    high = right + 1
    while True:
        low += 1
        high -= 1
        while compare_competitors(competitors[low], pivot) == -1:
            low += 1
        while compare_competitors(competitors[high], pivot) == 1:
            high -= 1
        if low >= high:
            return high

        competitors[low], competitors[high] = competitors[high], competitors[low]


def quick_sort(competitors: list[Competitor], left: int, right: int):
    if left < right:
        pivot_idx = partition(competitors, left, right)
        quick_sort(competitors, left, pivot_idx)
        quick_sort(competitors, pivot_idx + 1, right)


def sort_competitors(competitors: list[Competitor]) -> list[Competitor]:
    if len(competitors) <= 1:
        return competitors
    quick_sort(competitors, 0, len(competitors) - 1)
    return competitors


def read_input() -> list[Competitor]:
    competitors_num = int(input())
    competitors = []
    for _ in range(competitors_num):
        comp_raw = input().strip().split()
        competitors.append(Competitor(int(comp_raw[1]), int(comp_raw[2]), str(comp_raw[0])))
    return competitors


@dataclass
class TestData:
    comps: list[Competitor]
    expected: list[Competitor]


def test():
    tds = [
        TestData(
            [
                Competitor(4, 100, "alla"),
                Competitor(6, 1000, "gena"),
                Competitor(2, 90, "gosha"),
                Competitor(2, 90, "rita"),
                Competitor(4, 80, "timofey"),
            ],
            [
                Competitor(6, 1000, "gena"),
                Competitor(4, 80, "timofey"),
                Competitor(4, 100, "alla"),
                Competitor(2, 90, "gosha"),
                Competitor(2, 90, "rita"),
            ],
        ),
    ]
    for td in tds:
        original_array = deepcopy(td.comps)
        sort_competitors(td.comps)
        assert td.comps == td.expected, f"expected {td.expected}, got {td.comps}, input: {original_array}"


if __name__ == "__main__":
    environment = os.environ.get(ENVIRONMENT)
    if environment and environment.upper() == TEST:
        test()
    else:
        competitors = read_input()
        sort_competitors(competitors)
        print("\n".join([comp[2] for comp in competitors]))
