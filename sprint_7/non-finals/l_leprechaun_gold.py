"""
Лепреконы в данной задаче появились по соображениям общей морали, так как грабить банки — нехорошо.
Вам удалось заключить неплохую сделку с лепреконами, поэтому они пустили вас в своё хранилище золотых слитков.
Все слитки имеют единую пробу, то есть стоимость 1 грамма золота в двух разных слитках одинакова.
В хранилище есть n слитков, вес i-го слитка равен wi кг. У вас есть рюкзак, вместимость которого M килограмм.
Выясните максимальную суммарную массу золотых слитков, которую вы сможете унести.

Формат ввода
В первой строке дано число слитков —– натуральное число n (1 ≤ n ≤ 1000) и вместимость рюкзака –— целое число
M (0 ≤ M ≤ 104). Во второй строке записано n натуральных чисел wi (1 ≤ wi ≤ 104) -— массы слитков.

Формат вывода
Выведите единственное число — максимальную массу, которую можно забрать с собой.
"""


def solution(backpack_cap: int, gold_bars: list[int]) -> int:
    dp = [0] * (backpack_cap + 1)
    for gb in gold_bars:
        for j in range(backpack_cap, gb - 1, -1):
            candidate_weight = dp[j - gb] + gb
            if candidate_weight > dp[j]:
                dp[j] = candidate_weight
    return dp[backpack_cap]


def read_input() -> tuple[int, list[int]]:
    _, backpack_cap = tuple(map(int, input().strip().split()))
    gold_bars = list(map(int, input().strip().split()))
    return backpack_cap, gold_bars


if __name__ == "__main__":
    backpack_cap, gold_bars = read_input()
    print(solution(backpack_cap, gold_bars))
