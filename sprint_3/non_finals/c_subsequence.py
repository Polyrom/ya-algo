import os

ENVIRONMENT = "ENVIRONMENT"
TEST = "TEST"


def solution(string: str, substring: str) -> bool:
    if len(substring) > len(string):
        return False
    i, j = 0, 0
    while i != len(string) and j != len(substring):
        if string[i] == substring[j]:
            j += 1
        i += 1
    return j == len(substring)


def read_input() -> tuple[str, str]:
    substring = input()
    string = input()
    return substring, string


def test():
    ins = [
        ("ahbgdcu", "abc", True),
        ("ahpc", "abcp", False),
        (
            "hmrqvftefyixinahlzgbkidroxiptbbkjmtwpsujevkulgrjiwiwzyhngulrodiwyg",
            "ijha",
            False,
        ),
        (
            "zzkqxfdxbbjqhatygmtmpgbhumicrhtjkrfblwwnjlebsfdawznznxwyzehpubvdukmgwrivygosfkdquwnhfnxprjwnzdjvtclcfsf",
            "m",
            True,
        ),
    ]
    for s, ss, expected in ins:
        result = solution(s, ss)
        assert result == expected, f"expected {expected}, got {result}, inputs: {s} {ss}"


if __name__ == "__main__":
    environment = os.environ.get(ENVIRONMENT)
    if environment == TEST:
        test()
    else:
        substring, string = read_input()
        print(solution(string, substring))
