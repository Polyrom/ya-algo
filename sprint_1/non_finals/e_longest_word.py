def get_longest_word(line: str) -> str:
    longest = ""
    for word in line.strip().split():
        if len(word) > len(longest):
            longest = word
    return longest


def read_input() -> str:
    _ = input()
    return input().strip()


def print_result(result: str) -> None:
    print(result)
    print(len(result))


print_result(get_longest_word(read_input()))
