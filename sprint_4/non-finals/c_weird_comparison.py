"""
Жители Алгосского архипелага придумали новый способ сравнения строк.
Две строки считаются равными, если символы одной из них можно заменить на символы другой так,
что первая строка станет точной копией второй строки. При этом необходимо соблюдение двух условий:
- Порядок вхождения символов должен быть сохранён.
- Одинаковым символам первой строки должны соответствовать одинаковые символы второй строки. Разным символам —– разные.

Например, если строка s = «abacaba», то ей будет равна строка t = «xhxixhx», так как все вхождения «a» заменены на «x»,
«b» –— на «h», а «c» –— на «i». Если же первая строка s=«abc», а вторая t=«aaa», то строки уже не будут равны,
так как разные буквы первой строки соответствуют одинаковым буквам второй.

Формат ввода

В первой строке записана строка s, во второй –— строка t. Длины обеих строк не превосходят 106.
Обе строки содержат хотя бы по одному символу и состоят только из маленьких латинских букв.
Строки могут быть разной длины.
"""

import os
from dataclasses import dataclass

ENVIRONMENT = "ENVIRONMENT"
TEST = "TEST"


def solution(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False

    comp_map_s1 = {}
    comp_map_s2 = {}

    for i in range(len(s1)):
        left = s1[i]
        right = s2[i]

        if left in comp_map_s1:
            if comp_map_s1[left] != right:
                return False
        else:
            comp_map_s1[left] = right

        if right in comp_map_s2:
            if comp_map_s2[right] != left:
                return False
        else:
            comp_map_s2[right] = left

    return True


@dataclass
class TestData:
    s1: str
    s2: str
    expected: int


def test():
    tds = [
        TestData("mxyskaoghi", "qodfrgmslc", True),
        TestData("agg", "xdd", True),
        TestData("agg", "xda", False),
        TestData("aba", "xxx", False),
    ]
    for td in tds:
        result = solution(td.s1, td.s2)
        assert result == td.expected, f"expected={td.expected}, got={result}, input=(s1={td.s1} s2={td.s2})"


def read_input() -> tuple[str, str]:
    s1 = input()
    s2 = input()
    return s1, s2


if __name__ == "__main__":
    environment = os.environ.get(ENVIRONMENT)
    if environment and environment.upper() == TEST:
        test()
    else:
        res = solution(*read_input())
        print("YES" if res else "NO")
