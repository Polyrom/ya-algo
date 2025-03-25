"""
К Васе в гости пришли одноклассники. Его мама решила угостить ребят печеньем.
Но не всё так просто. Печенья могут быть разного размера.
А у каждого ребёнка есть фактор жадности —– минимальный размер печенья, которое он возьмёт.
Нужно выяснить, сколько ребят останутся довольными в лучшем случае, когда они действуют оптимально.
Каждый ребёнок может взять не больше одного печенья."
"""

import os

ENVIRONMENT = "ENVIRONMENT"
TEST = "TEST"


def solution(kids_greed: list[int], cookies: list[int]) -> int:
    kids_greed.sort()
    cookies.sort()
    res, i, j = 0, 0, 0
    while i != len(kids_greed) and j != len(cookies):
        if kids_greed[i] <= cookies[j]:
            res += 1
            i += 1
        j += 1
    return res


def test():
    ins = [
        ([1, 2], [2, 1, 3], 2),
        ([2, 1, 3], [1, 1], 1),
        ([3, 4, 8], [4, 4, 6], 2),
        ([3, 4, 4, 8], [3, 4, 6, 7], 3),
        ([4], [1, 4, 7, 10, 2, 2, 7, 8], 1),
    ]
    for kg, ck, expected in ins:
        result = solution(kg, ck)
        assert result == expected, f"expected {expected}, got {result}, inputs: {kg} {ck}"


def read_input() -> tuple[list[int], list[int]]:
    _ = input()
    kids_greed = list(map(int, input().strip().split()))
    _ = input()
    cookies = list(map(int, input().strip().split()))
    return kids_greed, cookies


if __name__ == "__main__":
    environment = os.environ.get(ENVIRONMENT)
    if environment == TEST:
        test()
    else:
        kids_greed, cookies = read_input()
        print(solution(kids_greed, cookies))
