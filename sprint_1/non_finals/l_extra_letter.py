from typing import Tuple


def get_excessive_letter(shorter: str, longer: str) -> str:
    shorted_sorted, longer_sorted = sorted(shorter), sorted(longer)
    for i, j in zip(shorted_sorted, longer_sorted):
        if i != j:
            return j
    return longer_sorted[-1]


def read_input() -> Tuple[str, str]:
    shorter = input().strip()
    longer = input().strip()
    return shorter, longer


shorter, longer = read_input()
print(get_excessive_letter(shorter, longer))
